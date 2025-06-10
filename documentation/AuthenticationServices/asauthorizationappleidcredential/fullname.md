# fullName

**Framework**: Authentication Services  
**Kind**: property

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

#### Discussion

Apple doesn’t receive the user’s full name shared with the system UI. The raw data is passed directly to your app from the browser and is not included in the user’s identity token. For more information, visit doc://com.apple.documentation/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple.

> 💡 **Tip**:  To help prevent cross-site scripting attacks, validate and sanitize the user-submitted first and last name values before storing on your app servers.

## See Also

- [var authorizedScopes: [ASAuthorization.Scope]](asauthorizationappleidcredential/authorizedscopes.md)
  The contact information the user authorized your app to access.
- [var email: String?](asauthorizationappleidcredential/email.md)
  The user’s email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/fullname)*