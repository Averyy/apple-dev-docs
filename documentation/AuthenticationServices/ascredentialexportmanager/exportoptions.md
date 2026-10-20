# ASCredentialExportManager.ExportOptions

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

Options that configure the behavior of a credential export operation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ExportOptions
```

## Topics

### Working with export options
- [let formatVersion: ASExportedCredentialData.FormatVersion](./exportoptions/formatversion.md)
  The version of the Credential Exchange Format standard used by the export manager.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Exporting credentials
- [func requestExport(for: String?) async throws -> ASCredentialExportManager.ExportOptions](./requestexport%28for%29.md)
  Begins the export process.
- [func exportCredentials(ASExportedCredentialData) async throws](./exportcredentials%28_%29.md)
  Exports the provided credential data.
- [struct ASExportedCredentialData](../asexportedcredentialdata.md)
  A container for credential data that your app provides to an exporter or receives from an importer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager/exportoptions)*