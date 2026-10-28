# signIn

**Framework**: SigninwithAppleJS  
**Kind**: method  
**Role**: Instance Method

Sign in using the configuration object.

**Availability**:
- Sign in with Apple JS 1.0+

## Declaration

```
Promise<SignInResponseI|SignInErrorI>|void signIn(
	optional ClientConfigI signInConfig
);
```

## Mentions

- [Configuring your webpage for Sign in with Apple](../../SigninwithApple/configuring-your-webpage-for-sign-in-with-apple.md)

## Discussion

By default, the [`signIn`](./signin.md) method uses the configuration object created during initialization. However, you can override the initialization values by passing in a new configuration object.

## Parameters

- `signInConfig`: The configuration object used to sign in the user.

## See Also

### Initializing the sign in process
- [init](./init.md)
  Initialize the authentication object with a configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs/authi/signin)*