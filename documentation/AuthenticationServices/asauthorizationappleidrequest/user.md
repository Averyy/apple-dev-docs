# user

**Framework**: Authentication Services  
**Kind**: property

An identifier associated with the user’s Apple ID.

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
var user: String? { get set }
```

#### Discussion

Typically you leave this property set to `nil` the first time you authenticate a user. Otherwise, if you previously received an authorization containing an [`ASAuthorizationAppleIDCredential`](asauthorizationappleidcredential.md) instance, set this property to the value from the credential’s [`user`](asauthorizationappleidcredential/user.md) property.

The value is an arbitrary string that’s portable among apps from a single developer, but not between apps from different developers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidrequest/user)*