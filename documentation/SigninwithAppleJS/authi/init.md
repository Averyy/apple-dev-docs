# init

**Framework**: SigninwithAppleJS  
**Kind**: method  
**Role**: Instance Method

Initialize the authentication object with a configuration object.

**Availability**:
- Sign in with Apple JS 1.0+

## Declaration

```
void init(
	ClientConfigI config
);
```

## Mentions

- [Configuring your webpage for Sign in with Apple](../../SigninwithApple/configuring-your-webpage-for-sign-in-with-apple.md)

## Discussion

Use this method to configure the authentication object. Alternatively, you can use meta tags on your website to configure the authentication object.

```html
<head>
   <meta name="appleid-signin-client-id" content="[CLIENT_ID]">
   <meta name="appleid-signin-scope" content="[SCOPES]">
   <meta name="appleid-signin-redirect-uri" content="[REDIRECT_URI]">
   <meta name="appleid-signin-state" content="[STATE]">
</head>
```

## Parameters

- `config`: The client configuration object used for initialization.

## See Also

### Initializing the sign in process
- [signIn](./signin.md)
  Sign in using the configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs/authi/init)*