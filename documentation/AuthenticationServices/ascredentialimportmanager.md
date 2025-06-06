# ASCredentialImportManager

**Framework**: Authentication Services  
**Kind**: class

A class to manage importing credentials.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
class ASCredentialImportManager
```

#### Overview

`ASCredentialImportManager` allows your app to exchange authentication credentials such as passwords and passkeys with other apps. Participating apps, such as password managers, export credentials to your app by using the [`ASCredentialExportManager`](ascredentialexportmanager.md) class.

##### Configuring Your App

To participate in credential exchange, edit your credential provider extension’s Info.plist and add the following key with a Boolean value of `YES`:

`NSExtension > NSExtensionAttributes > ASCredentialProviderExtensionCapabilities`

For iOS 18.2, visionOS 2.2, and macOS 15.2, you also need to explicitly enable credential exchange, like this:

- In iOS or visionOS, open the Settings app and enable the Settings > Developer > Credential Exchange switch.
- In macOS, enter the following command in Terminal:

`defaults write com.apple.AuthenticationServices.Developer CredentialExchangeEnabled -bool YES`

##### Importing Credentials

Credential export begins when another app calls [`exportCredentials(_:)`](ascredentialexportmanager/exportcredentials(_:).md), which brings up a system UI to choose an app to export to. When the person using the export app chooses your app to receive the credentials, the system launches your app and sends an  [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) whose [`activityType`](https://developer.apple.com/documentation/foundation/nsuseractivity/1409611-activitytype) is `ASCredentialExchangeActivity`. In order to support this process, add the [`NSUserActivityTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserActivityTypes) array to your app’s Info.plist and add the item `ASCredentialExchangeActivityType` to the array.

Your app needs to handle being launched from this activity by fetching the `ASCredentialImportToken` from the activity’s  [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary. The value of this key is a [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) token; create an instance of [`ASCredentialImportManager`](ascredentialimportmanager.md) and pass the token to [`importCredentials(token:)`](ascredentialimportmanager/importcredentials(token:).md) to begin the import process.

The following example shows how a SwiftUI app handles launching from the user activity and beginning the credential import process.

```swift
 struct CredentialImportManagerExample: View {
     @Environment(\.credentialImportManager) private var credentialImportManager

     var body: some View {
         content // Defined elsewhere.
             .onContinueUserActivity(ASCredentialExchangeActivityType) { activity in
                 Task {
                     do {
                         guard let token = activity.userInfo?[ASCredentialImportToken] as? UUID else { return }
                         let credentialData = try await credentialImportManager.importCredentials(token: token)
                         // Do something with the data.
                     } catch {
                         // Handle the import error.
                     }
                 }
             }
     }
 }
```

For a corresponding export code example, see [`ASCredentialExportManager`](ascredentialexportmanager.md).

## Topics

### Creating an import manager
- [init()](ascredentialimportmanager/init.md)
  Creates an import manager instance.
### Importing credentials
- [func importCredentials(token: UUID) async throws -> ASExportedCredentialData](ascredentialimportmanager/importcredentials(token:).md)
  Begins the credential import process.
- [struct ASExportedCredentialData](asexportedcredentialdata.md)
  A container for credential data that your app provides to an exporter or receives from an importer.

## See Also

- [class ASCredentialExportManager](ascredentialexportmanager.md)
  A class to manage exporting credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialimportmanager)*