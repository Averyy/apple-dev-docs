# ASAuthorizationProvider

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

An interface that authorization providers must implement.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol ASAuthorizationProvider : NSObjectProtocol
```

```objc
@protocol ASAuthorizationProvider <NSObject>
```

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [ASAuthorizationAccountCreationProvider](./asauthorizationaccountcreationprovider.md)
- [ASAuthorizationAppleIDProvider](./asauthorizationappleidprovider.md)
- [ASAuthorizationPasswordProvider](./asauthorizationpasswordprovider.md)
- [ASAuthorizationPlatformPublicKeyCredentialProvider](./asauthorizationplatformpublickeycredentialprovider.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialProvider](./asauthorizationsecuritykeypublickeycredentialprovider.md)
- [ASAuthorizationSingleSignOnProvider](./asauthorizationsinglesignonprovider.md)

## See Also

### Inspecting the Provider
- [var provider: any ASAuthorizationProvider](./asauthorizationrequest/provider.md)
  The provider servicing the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationprovider)*