# name

**Framework**: SigninwithAppleJS  
**Kind**: property  
**Role**: Instance Property

The user’s full name from their Apple Account or a user-submitted value provided from the Sign in with Apple UI.

**Availability**:
- Sign in with Apple JS 1.4.1+

## Declaration

```
attribute NameI name;
```

## Discussion

Apple doesn’t receive the user’s full name shared with the system UI. The raw data is passed directly to your app from the browser and is not included in the user’s identity token. For more information, visit [Authenticating users with Sign in with Apple](../../SigninwithApple/authenticating-users-with-sign-in-with-apple.md).

> 💡 **Tip**:  To help prevent cross-site scripting attacks, validate and sanitize the user-submitted first and last name values before storing on your app servers.

## See Also

### Identifying the user by email address
- [email](./email.md)
  The user’s email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs/useri/name)*