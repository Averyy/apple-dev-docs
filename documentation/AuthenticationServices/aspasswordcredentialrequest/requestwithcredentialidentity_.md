# requestWithCredentialIdentity:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Type Method

Creates and initializes a password credential request object.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) requestWithCredentialIdentity:(ASPasswordCredentialIdentity *) credentialIdentity;
```

#### Return Value

The created object.

## Parameters

- `credentialIdentity`: The credential identity for the requested password.

## See Also

### Creating password credential requests
- [init(credentialIdentity: ASPasswordCredentialIdentity)](./init%28credentialidentity%29.md)
  Initializes a password credential request object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasswordcredentialrequest/requestwithcredentialidentity:)*