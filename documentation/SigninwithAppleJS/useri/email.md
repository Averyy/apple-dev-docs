# email

**Framework**: SigninwithAppleJS  
**Kind**: property  
**Role**: Instance Property

The user’s email address.

**Availability**:
- Sign in with Apple JS 1.4.1+

## Declaration

```
attribute string email;
```

#### Discussion

Validate and persist this information from your app to your server. Subsequent authorization requests do not contain the user object, however, the user’s email is provided in the identity token for all requests. For more information, visit [Authenticating users with Sign in with Apple](../../SigninwithApple/authenticating-users-with-sign-in-with-apple.md).

## See Also

### Identifying the user by email address
- [name](./name.md)
  The user’s full name from their Apple Account or a user-submitted value provided from the Sign in with Apple UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs/useri/email)*