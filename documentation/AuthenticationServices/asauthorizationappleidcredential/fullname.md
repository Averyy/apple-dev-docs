# fullName

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The user’s full name from their Apple ID or a user-submitted value provided from the Sign in with Apple UI.

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
var fullName: PersonNameComponents? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSPersonNameComponents * fullName;
```

## Discussion

Apple doesn’t receive the user’s full name shared with the system UI. The raw data is passed directly to your app from the browser and is not included in the user’s identity token. For more information, visit [Authenticating users with Sign in with Apple](../../SigninwithApple/authenticating-users-with-sign-in-with-apple.md).

> 💡 **Tip**:  To help prevent cross-site scripting attacks, validate and sanitize the user-submitted first and last name values before storing on your app servers.

## See Also

### Getting Contact Information
- [var authorizedScopes: [ASAuthorization.Scope]](./authorizedscopes.md)
  The contact information the user authorized your app to access.
- [var email: String?](./email.md)
  The user’s email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/fullname)*