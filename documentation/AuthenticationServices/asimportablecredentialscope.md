# ASImportableCredentialScope

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

The scope for where a credential should be usable.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ASImportableCredentialScope
```

## Topics

### Structures
- [ASImportableCredentialScope.AndroidAppCertificationFingerprint](./asimportablecredentialscope/androidappcertificationfingerprint.md)
- [ASImportableCredentialScope.AndroidAppID](./asimportablecredentialscope/androidappid.md)
  An identifier for an Android app.
### Initializers
- [init(urls: [URL], androidApps: [ASImportableCredentialScope.AndroidAppID])](./asimportablecredentialscope/init%28urls,androidapps%29.md)
### Instance Properties
- [var androidApps: [ASImportableCredentialScope.AndroidAppID]](./asimportablecredentialscope/androidapps.md)
  Android apps that are associated with this credential.
- [var urls: [URL]](./asimportablecredentialscope/urls.md)
  URLs where that are associated with this credential.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredentialscope)*