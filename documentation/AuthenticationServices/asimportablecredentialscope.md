# ASImportableCredentialScope

**Framework**: Authentication Services  
**Kind**: struct

The scope for where a credential should be usable.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ASImportableCredentialScope
```

## Topics

### Structures
- [ASImportableCredentialScope.AndroidAppCertificationFingerprint](asimportablecredentialscope/androidappcertificationfingerprint.md)
- [ASImportableCredentialScope.AndroidAppID](asimportablecredentialscope/androidappid.md)
  An identifier for an Android app.
### Initializers
- [init(urls: [URL], androidApps: [ASImportableCredentialScope.AndroidAppID])](asimportablecredentialscope/init(urls:androidapps:).md)
### Instance Properties
- [var androidApps: [ASImportableCredentialScope.AndroidAppID]](asimportablecredentialscope/androidapps.md)
  Android apps that are associated with this credential.
- [var urls: [URL]](asimportablecredentialscope/urls.md)
  URLs where that are associated with this credential.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredentialscope)*