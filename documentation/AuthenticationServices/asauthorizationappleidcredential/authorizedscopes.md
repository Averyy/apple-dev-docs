# authorizedScopes

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The contact information the user authorized your app to access.

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
var authorizedScopes: [ASAuthorization.Scope] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * authorizedScopes;
```

## See Also

### Getting Contact Information
- [var fullName: PersonNameComponents?](./fullname.md)
  The user’s full name from their Apple ID or a user-submitted value provided from the Sign in with Apple UI.
- [var email: String?](./email.md)
  The user’s email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/authorizedscopes)*