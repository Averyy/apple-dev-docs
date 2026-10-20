# ASExportedCredentialData

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A container for credential data that your app provides to an exporter or receives from an importer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ASExportedCredentialData
```

#### Overview

This type is a wrapper object for multiple [`ASImportableAccount`](./asimportableaccount.md) objects.

## Topics

### Accessing accounts
- [var accounts: [ASImportableAccount]](./asexportedcredentialdata/accounts.md)
  An array of importable accounts.
- [struct ASImportableAccount](./asimportableaccount.md)
  An account for use in importing and exporting credentials.
### Initializers
- [init(accounts: [ASImportableAccount], formatVersion: ASExportedCredentialData.FormatVersion, exporterRelyingPartyIdentifier: String, exporterDisplayName: String, timestamp: Date)](./asexportedcredentialdata/init%28accounts,formatversion,exporterrelyingpartyidentifier,exporterdisplayname,timestamp%29.md)
### Instance Properties
- [let exporterDisplayName: String](./asexportedcredentialdata/exporterdisplayname.md)
- [let exporterRelyingPartyIdentifier: String](./asexportedcredentialdata/exporterrelyingpartyidentifier.md)
- [let formatVersion: ASExportedCredentialData.FormatVersion](./asexportedcredentialdata/formatversion-swift.property.md)
- [let timestamp: Date](./asexportedcredentialdata/timestamp.md)
### Enumerations
- [ASExportedCredentialData.FormatVersion](./asexportedcredentialdata/formatversion-swift.enum.md)
  The Credential Exchange Format version for `ASExportedCredentialData`.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Exporting credentials
- [func requestExport(for: String?) async throws -> ASCredentialExportManager.ExportOptions](./ascredentialexportmanager/requestexport%28for%29.md)
  Begins the export process.
- [ASCredentialExportManager.ExportOptions](./ascredentialexportmanager/exportoptions.md)
  Options that configure the behavior of a credential export operation.
- [func exportCredentials(ASExportedCredentialData) async throws](./ascredentialexportmanager/exportcredentials%28_%29.md)
  Exports the provided credential data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asexportedcredentialdata)*