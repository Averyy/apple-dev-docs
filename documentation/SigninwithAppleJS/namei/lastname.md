# lastName

**Framework**: SigninwithAppleJS  
**Kind**: property  
**Role**: Instance Property

The user’s last name.

**Availability**:
- Sign in with Apple JS 1.4.1+

## Declaration

```
attribute string lastName;
```

## Discussion

Apple doesn’t receive the user’s full name shared with the system UI. The raw data is passed directly to your app from the browser and is not included in the user’s identity token. To help prevent cross-site scripting attacks, validate and sanitize the user-submitted first and last name values before storing on your app servers.

## See Also

### Identifying the user by name
- [firstName](./firstname.md)
  The user’s first name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs/namei/lastname)*