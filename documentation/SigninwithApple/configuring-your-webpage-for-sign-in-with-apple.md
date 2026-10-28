# Configuring your webpage for Sign in with Apple

**Framework**: Sign in with Apple  
**Role**: Article

Prepare your webpage to authorize users through Sign in with Apple.

## Overview

You can use HTML and JavaScript to add Sign in with Apple to your webpage. Configure an authorization object and add a button that allows users to sign in to your webpage with their Apple Account.

### Embed Sign in with Apple JS

Include the script tag and link to Apple’s hosted version of the Sign in with Apple JS framework in your web page:

```javascript
<script type="text/javascript" src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"></script>
```

Embedding the framework gives you access to the Sign in with Apple authorization features.

### Configure the Authorization Object

To get started quickly, configure Sign in with Apple JS with a default markup setup. Alternatively, use JavaScript to configure the authorization object, or use a combination of the two.

Configure the authorization object using only markup by setting the meta tags in the header section and displaying a Sign in with Apple button. For more information about the client configuration, see [`ClientConfigI`](../SigninwithAppleJS/clientconfigi.md).

```html
<html>
    <head>
        <meta name="appleid-signin-client-id" content="[CLIENT_ID]">
        <meta name="appleid-signin-scope" content="[SCOPES]">
        <meta name="appleid-signin-redirect-uri" content="[REDIRECT_URI]">
        <meta name="appleid-signin-state" content="[STATE]">
        <meta name="appleid-signin-nonce" content="[NONCE]">
        <meta name="appleid-signin-use-popup" content="true">
    </head>
    <body>
        <div id="appleid-signin" data-color="black" data-border="true" data-type="sign in"></div>
        <script type="text/javascript" src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"></script>
    </body>
</html>
```

> ❗ **Important**:  The host specified in `appleid-signin-redirect-uri` must include a domain name. It can’t be an IP address or `localhost`, and must not contain a fragment identifer (#). For more information, see [Configuring your environment for Sign in with Apple](./configuring-your-environment-for-sign-in-with-apple.md).

You can also configure the authorization object using the JavaScript APIs and display a Sign in with Apple button.

```javascript
<html>
    <head>
    </head>
    <body>
        <script type="text/javascript" src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"></script>
        <div id="appleid-signin" data-color="black" data-border="true" data-type="sign in"></div>
        <script type="text/javascript">
            AppleID.auth.init({
                clientId : '[CLIENT_ID]',
                scope : '[SCOPES]',
                redirectURI : '[REDIRECT_URI]',
                state : '[STATE]',
                nonce : '[NONCE]',
                usePopup : true
            });
        </script>
    </body>
</html>
```

Additionally, you can combine the two configuration options: you can set the meta tags in the header, while at the same time using JavaScript APIs. This configuration provides a default implementation through the meta tags, but gives you the ability to override the initial information using the JavaScript APIs.

> **Note**:  Use space separation when requesting multiple scopes; for example, `"scope=name email"`.

### Handle the Authorization Response

After the user clicks the Sign in with Apple button, the framework sends the authorization information to Apple. Apple processes the authorization request, and sends an HTTP POST request containing the results of the authorization to the URL provided in [`redirectURI`](../SigninwithAppleJS/clientconfigi/redirecturi.md). The HTTP body contains the result parameters with a content-type of `application/x-www-form-urlencoded`. A successful response contains the following parameters:

- **`code`**: A single-use authentication code that expires after five minutes. To learn how to validate this code to obtain user tokens, see [`Token validation`](../SigninwithAppleRESTAPI/generate-and-validate-tokens.md).
- **`id_token`**: A JSON web token (JWT) containing the user’s identification information. For more information, see [`id_token`](../SigninwithAppleJS/authorizationi/id_token.md).
- **`state`**: An arbitrary string  passed by the [`init`](../SigninwithAppleJS/authi/init.md) function, representing the current state of the authorization request. This value is also used to mitigate cross-site request forgery attacks, by comparing against the state value contained in the authorization response.
- **`user`**: A JSON string containing the data requested in the [`scope`](../SigninwithAppleJS/clientconfigi/scope.md) property. The returned data is in the following format:

`{ "name": { "firstName": string, "lastName": string }, "email": string }`

> ❗ **Important**:  Apple only returns the user object the first time the user authorizes the app. Validate and persist this information from your app to your server. Subsequent authorization requests do not contain the user object, however, the user’s email is provided in the identity token for all requests. For more information, see [Authenticating users with Sign in with Apple](./authenticating-users-with-sign-in-with-apple.md).

If an error occurs, the HTTP body contains the following parameters:

- **`error`**: The returned error code.
- **`state`**: The state passed by the [`init`](../SigninwithAppleJS/authi/init.md) function. Compare against the state value provided in the initial authorization request to mitigate cross-site request forgery attacks.

> **Note**:  Currently, the only error code returned is `user_cancelled_authorize`. The framework returns this error code when the user clicks the Cancel button.

If you use the pop-up option, your app sends the authorization information to Apple when the user clicks the Sign in with Apple button. After Apple’s server processes the authorization request, it dispatches a Domain Object Model (DOM) event containing the results of the authorization: `AppleIDSignInOnSuccess` on success, or `AppleIDSignInOnFailure` on failure.

To handle the response, add an event listener:

```javascript
// Listen for authorization success.
document.addEventListener('AppleIDSignInOnSuccess', (event) => {
    // Handle successful response.
    console.log(event.detail.data);
});

// Listen for authorization failures.
document.addEventListener('AppleIDSignInOnFailure', (event) => {
     // Handle error.
     console.log(event.detail.error);
});
```

If the [`signIn`](../SigninwithAppleJS/authi/signin.md) function started the authorization process, the function returns a promise object that resolves if the authorization succeeds. If the authorization fails, the function rejects the promise object.

Here’s an example of how to handle the response when using the [`signIn`](../SigninwithAppleJS/authi/signin.md) function.

```javascript
try {
     const data = await AppleID.auth.signIn()
     // Handle successful response.
} catch ( error ) {
     // Handle error.
}
```

Upon authorization success, the server returns the following data object:

```javascript
{
     "authorization": {
       "code": "[CODE]",
       "id_token": "[ID_TOKEN]",
       "state": "[STATE]"
     },
     "user": {
       "email": "[EMAIL]",
       "name": {
         "firstName": "[FIRST_NAME]",
         "lastName": "[LAST_NAME]"
       }
     }
}
```

Upon failure, the server returns the following data object:

```javascript
{
    "error": "[ERROR_CODE]"
}
```

## See Also

### Essentials
- [Communicating using the private email relay service](./communicating-using-the-private-email-relay-service.md)
  Stay in touch with users who opt for an anonymous email address with Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapple/configuring-your-webpage-for-sign-in-with-apple)*