# email

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The user’s email address.

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
var email: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * email;
```

## See Also

### Getting Contact Information
- [var authorizedScopes: [ASAuthorization.Scope]](./authorizedscopes.md)
  The contact information the user authorized your app to access.
- [var fullName: PersonNameComponents?](./fullname.md)
  The user’s full name from their Apple ID or a user-submitted value provided from the Sign in with Apple UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/email)*