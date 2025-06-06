# exportCredentials(_:)

**Framework**: Authentication Services  
**Kind**: method

Begins the credential export process.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
func exportCredentials(_ credentialData: ASExportedCredentialData) async throws
```

#### Discussion

After the person using your app selects the credentials to export, pack those credentials into an [`ASExportedCredentialData`](asexportedcredentialdata.md) object and call this method. The `exportCredentials(_:)` call brings up the out-of-process system UI that guides the user through the rest of the export flow. Use `await` to wait for the system UI flow to complete.

This method throws an error if the export can’t proceed, which occurs if there are no import apps available, or if the device isn’t configured with a passcode, Touch ID, or Face ID.

## Parameters

- `credentialData`: The credential data to export.

## See Also

- [struct ASExportedCredentialData](asexportedcredentialdata.md)
  A container for credential data that your app provides to an exporter or receives from an importer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager/exportcredentials(_:))*