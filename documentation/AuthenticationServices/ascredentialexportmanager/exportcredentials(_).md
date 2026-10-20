# exportCredentials(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Exports the provided credential data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func exportCredentials(_ credentialData: ASExportedCredentialData) async throws
```

#### Discussion

After you call the [`requestExport(for:)`](./requestexport%28for%29.md) method and collect the credentials to export, pack the credentials into an [`ASExportedCredentialData`](../asexportedcredentialdata.md) object and call this method.

## Parameters

- `credentialData`: The credential data to export.

## See Also

### Exporting credentials
- [func requestExport(for: String?) async throws -> ASCredentialExportManager.ExportOptions](./requestexport%28for%29.md)
  Begins the export process.
- [ASCredentialExportManager.ExportOptions](./exportoptions.md)
  Options that configure the behavior of a credential export operation.
- [struct ASExportedCredentialData](../asexportedcredentialdata.md)
  A container for credential data that your app provides to an exporter or receives from an importer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager/exportcredentials(_:))*