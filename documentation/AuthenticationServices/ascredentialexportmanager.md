# ASCredentialExportManager

**Framework**: Authentication Services  
**Kind**: class

A class to manage exporting credentials.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class ASCredentialExportManager
```

#### Overview

`ASCredentialExportManager` allows your app to exchange authentication credentials like passwords and passkeys with other apps. Participating apps such as password managers can receive your exported credentials by using the [`ASCredentialImportManager`](ascredentialimportmanager.md) class.

##### Configure Your App

To participate in credential exchange, edit your credential provider extension’s Info.plist and add the following key with a Boolean value of `YES`:

`NSExtension > NSExtensionAttributes > ASCredentialProviderExtensionCapabilities > SupportsCredentialExchange`

For iOS 18.2, visionOS 2.2, and macOS 15.2, you also need to explicitly enable credential exchange, like this:

- In iOS or visionOS, open the Settings app and enable the Settings > Developer > Credential Exchange switch.
- In macOS, enter the following command in Terminal:

`defaults write com.apple.AuthenticationServices.Developer CredentialExchangeEnabled -bool YES`

##### Export Credentials

To export credentials, your app’s interface needs to allow the person using it to select the credentials they want to export. To begin the process, call the [`exportCredentials(_:)`](ascredentialexportmanager/exportcredentials(_:).md) method on an instance of this class. Calling this method brings up an out-of-process system UI that guides the person through the export procedure. The system UI explains the risks of exporting credentials, and then allows them to choose an app to export to. The operating system acts as an intermediary to establish the identities of the password manager apps involved and performs the exchange; this process doesn’t write any data to the file system.

When a person chooses an importer app, the system launches it, sending the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) `ASCredentialExchangeActivity`. The importing app responds to the launch activity by calling the [`ASCredentialImportManager`](ascredentialimportmanager.md) method [`importCredentials(token:)`](ascredentialimportmanager/importcredentials(token:).md) to receive the exported credentials.

The following example shows how to perform an export from a SwiftUI view.

```swift
struct CredentialExportManagerExample: View {
    @Environment(\.credentialExportManager) private var credentialExportManager

    var body: some View {
        Button("Export Credentials") {
            Task {
                do {
                    let credentialData = getCredentialData() // defined elsewhere
                    try await credentialExportManager.exportCredentials(credentialData)
                } catch {
                    // Handle the export error.
                }
            }
        }
    }
}
```

For a corresponding import code example, see [`ASCredentialImportManager`](ascredentialimportmanager.md).

## Topics

### Creating an export manager
- [typealias ASPresentationAnchor](aspresentationanchor.md)
  A platform-specific type that indicates the kind of user interface element to use as a presentation anchor.
### Exporting credentials
- [func exportCredentials(ASExportedCredentialData) async throws](ascredentialexportmanager/exportcredentials(_:).md)
  Begins the credential export process.
- [struct ASExportedCredentialData](asexportedcredentialdata.md)
  A container for credential data that your app provides to an exporter or receives from an importer.
### Structures
- [ASCredentialExportManager.ExportOptions](ascredentialexportmanager/exportoptions.md)
### Initializers
- [convenience init(presentationAnchor: ASPresentationAnchor)](ascredentialexportmanager/init(presentationanchor:)-56ki6.md)
- [convenience init(presentationAnchor: ASPresentationAnchor)](ascredentialexportmanager/init(presentationanchor:)-904gt.md)
### Instance Methods
- [func requestExport(for: String?) async throws -> ASCredentialExportManager.ExportOptions](ascredentialexportmanager/requestexport(for:).md)
  Call this method to begin the export process. This will bring up the out of process system UI that will guide the user through the rest of the export flow. Once the necessary options have been determined, they will be returned here. After receiving the export options, call `exportCredentials(_:)` with the exported credentials in the specified format.

## See Also

- [class ASCredentialImportManager](ascredentialimportmanager.md)
  A class to manage importing credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager)*