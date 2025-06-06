# ASExportedCredentialData

**Framework**: Authentication Services  
**Kind**: struct

A container for credential data that your app provides to an exporter or receives from an importer.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
struct ASExportedCredentialData
```

#### Overview

This type is a wrapper object for multiple [`ASImportableAccount`](asimportableaccount.md) objects.

## Topics

### Creating a credential data instance
- [init(accounts: [ASImportableAccount])](asexportedcredentialdata/init(accounts:).md)
  Creates a credential data instance from an array of importable accounts.
### Accessing accounts
- [var accounts: [ASImportableAccount]](asexportedcredentialdata/accounts.md)
  An array of importable accounts.
- [struct ASImportableAccount](asimportableaccount.md)
  An account for use in importing and exporting credentials.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func exportCredentials(ASExportedCredentialData) async throws](ascredentialexportmanager/exportcredentials(_:).md)
  Begins the credential export process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asexportedcredentialdata)*