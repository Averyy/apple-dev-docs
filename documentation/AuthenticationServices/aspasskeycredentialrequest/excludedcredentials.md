# excludedCredentials

**Framework**: Authentication Services  
**Kind**: property

A list of IDs that represent existing passkeys for the account, to prevent creation of duplicate passkeys.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var excludedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]? { get }
```

#### Discussion

This value corresponds to the WebAuthn parameter `excludeCredentials`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/excludedcredentials)*