# ASCredentialExportManager.ExportOptions

**Framework**: Authentication Services  
**Kind**: struct

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
- [let formatVersion: ASExportedCredentialData.FormatVersion](ascredentialexportmanager/exportoptions/formatversion.md)
  The version of the Credential Exchange Format standard used by the export manager.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func requestExport(for: String?) async throws -> ASCredentialExportManager.ExportOptions](ascredentialexportmanager/requestexport(for:).md)
  Begins the export process.
- [func exportCredentials(ASExportedCredentialData) async throws](ascredentialexportmanager/exportcredentials(_:).md)
  Exports the provided credential data.
- [struct ASExportedCredentialData](asexportedcredentialdata.md)
  A container for credential data that your app provides to an exporter or receives from an importer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager/exportoptions)*