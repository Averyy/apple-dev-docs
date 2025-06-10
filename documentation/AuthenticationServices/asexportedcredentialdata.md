# ASExportedCredentialData

**Framework**: Authentication Services  
**Kind**: struct

A container for credential data that your app provides to an exporter or receives from an importer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ASExportedCredentialData
```

#### Overview

This type is a wrapper object for multiple [`ASImportableAccount`](asimportableaccount.md) objects.

## Topics

### Accessing accounts
- [var accounts: [ASImportableAccount]](asexportedcredentialdata/accounts.md)
  An array of importable accounts.
- [struct ASImportableAccount](asimportableaccount.md)
  An account for use in importing and exporting credentials.
### Initializers
- [init(accounts: [ASImportableAccount], formatVersion: ASExportedCredentialData.FormatVersion, exporterRelyingPartyIdentifier: String, exporterDisplayName: String, timestamp: Date)](asexportedcredentialdata/init(accounts:formatversion:exporterrelyingpartyidentifier:exporterdisplayname:timestamp:).md)
### Instance Properties
- [let exporterDisplayName: String](asexportedcredentialdata/exporterdisplayname.md)
- [let exporterRelyingPartyIdentifier: String](asexportedcredentialdata/exporterrelyingpartyidentifier.md)
- [let formatVersion: ASExportedCredentialData.FormatVersion](asexportedcredentialdata/formatversion-swift.property.md)
- [let timestamp: Date](asexportedcredentialdata/timestamp.md)
### Enumerations
- [ASExportedCredentialData.FormatVersion](asexportedcredentialdata/formatversion-swift.enum.md)
  The Credential Exchange Format version for `ASExportedCredentialData`.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func exportCredentials(ASExportedCredentialData) async throws](ascredentialexportmanager/exportcredentials(_:).md)
  Begins the credential export process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asexportedcredentialdata)*