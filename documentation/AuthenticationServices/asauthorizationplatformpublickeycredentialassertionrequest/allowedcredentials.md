# allowedCredentials

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The array of allowed credentials.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var allowedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor] { get set }
```

```objc
@property (nonatomic, copy) NSArray<ASAuthorizationPlatformPublicKeyCredentialDescriptor *> * allowedCredentials;
```

## Mentions

- [Authenticating people by using passkeys in browser apps](../authenticating-people-by-using-passkeys-in-browser-apps.md)

## See Also

### Accessing request properties
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput?](./largeblob-9kvvl.md)
  The request’s binary large object value.
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput?](./prf-47uoa.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialassertionrequest/allowedcredentials)*