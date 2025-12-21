# ASCredentialExportManager

**Framework**: Authentication Services  
**Kind**: class

A class to manage exporting credentials.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class ASCredentialExportManager
```

#### Overview

`ASCredentialExportManager` allows your app to exchange authentication credentials like passwords and passkeys with other apps. Participating apps such as password managers can receive your exported credentials by using the [`ASCredentialImportManager`](ascredentialimportmanager.md) class.

##### Configure Your App

To participate in credential exchange, edit your credential provider extension’s information property list and add the following key with a Boolean value of `YES`:

`NSExtension > NSExtensionAttributes > ASCredentialProviderExtensionCapabilities > SupportsCredentialExchange`

Also, declare the versions of the credential data format your app supports using the following key:

`NSExtension > NSExtensionAttributes > ASCredentialProviderExtensionCapabilities > SupportedCredentialExchangeVersions`

The value is an array of strings containing every version your app supports. Currently the only available version is `1.0`.

##### Export Credentials

To export credentials, your app’s interface needs to allow the person using it to select the credentials they want to export. To begin the process, call the [`requestExport(for:)`](ascredentialexportmanager/requestexport(for:).md) method on an instance of this class. Calling this method brings up an out-of-process system UI that guides the person through the export procedure. The system UI explains the risks of exporting credentials, and then allows them to choose an app to export to. The operating system acts as an intermediary to establish the identities of the password manager apps involved and performs the exchange; this process doesn’t write any data to the file system.

When a person chooses an importer app, the system launches it, sending an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) whose [`activityType`](https://developer.apple.com/documentation/Foundation/NSUserActivity/activityType) is `ASCredentialExchangeActivity`. The importing app responds to the launch activity by calling the [`ASCredentialImportManager`](ascredentialimportmanager.md) method [`importCredentials(token:)`](ascredentialimportmanager/importcredentials(token:).md) to receive the exported credentials.

When a person chooses an importer app, the [`requestExport(for:)`](ascredentialexportmanager/requestexport(for:).md) method returns an [`ASCredentialExportManager.ExportOptions`](ascredentialexportmanager/exportoptions.md) structure that describes the credential data format version you should use to ensure the importer app can successfully decode the data. Use this version to construct your [`ASExportedCredentialData`](asexportedcredentialdata.md) object, then call [`exportCredentials(_:)`](ascredentialexportmanager/exportcredentials(_:).md) with it. After the system receives your data, the system launches the importer app, sending the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) `ASCredentialExchangeActivity`. The importing app responds to the launch activity by calling the [`ASCredentialImportManager`](ascredentialimportmanager.md) method [`importCredentials(token:)`](ascredentialimportmanager/importcredentials(token:).md) to receive the exported credentials.

The following example shows how to perform an export from a SwiftUI view. The example assumes the typical case where the app has a single credential provider extension, which means it can pass `nil` to [`requestExport(for:)`](ascredentialexportmanager/requestexport(for:).md).

```swift
struct CredentialExportManagerExample: View {
    @Environment(\.credentialExportManager) private var credentialExportManager

    var body: some View {
        Button("Export Credentials") {
            Task {
                do {
                    let exportOptions = try await credentialExportManager.requestExport()
                    let credentialData = getCredentialData(exportOptions: exportOptions) // defined elsewhere
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
- [convenience init(presentationAnchor: ASPresentationAnchor)](ascredentialexportmanager/init(presentationanchor:)-56ki6.md)
  Creates an export manager, anchored by the given AppKit window.
- [convenience init(presentationAnchor: ASPresentationAnchor)](ascredentialexportmanager/init(presentationanchor:)-904gt.md)
  Creates an export manager, anchored by the given UIKit window.
- [typealias ASPresentationAnchor](aspresentationanchor.md)
  A platform-specific type that indicates the kind of user interface element to use as a presentation anchor.
### Exporting credentials
- [func requestExport(for: String?) async throws -> ASCredentialExportManager.ExportOptions](ascredentialexportmanager/requestexport(for:).md)
  Begins the export process.
- [ASCredentialExportManager.ExportOptions](ascredentialexportmanager/exportoptions.md)
  Options that configure the behavior of a credential export operation.
- [func exportCredentials(ASExportedCredentialData) async throws](ascredentialexportmanager/exportcredentials(_:).md)
  Exports the provided credential data.
- [struct ASExportedCredentialData](asexportedcredentialdata.md)
  A container for credential data that your app provides to an exporter or receives from an importer.

## See Also

- [class ASCredentialImportManager](ascredentialimportmanager.md)
  A class to manage importing credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager)*