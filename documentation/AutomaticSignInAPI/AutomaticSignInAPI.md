# Automatic Sign-In API

**Framework**: Automatic Sign-In API  
**Kind**: module

Manage sign-in tokens from your web server that facilitate single sign-on across the devices of your media-streaming service customers.

**Availability**:
- Automatic Sign-In API 1.0+

## Mentions

- [Signing people in to their media accounts automatically](../videosubscriberaccount/signing-people-in-to-media-apps-automatically.md)

#### Overview

The Automatic Sign-In feature offers a single sign-on experience for media-streaming apps. The first time a person signs in to your media-streaming service through your app, your app calls the [`Video Subscriber Account`](https://developer.apple.com/documentation/videosubscriberaccount) framework to prompt the person to opt in to Automatic Sign-In. If they agree, your app generates a string value token, or . You provide the token to the [`Video Subscriber Account`](https://developer.apple.com/documentation/videosubscriberaccount) framework, which stores it on the person’s Apple Account to sign the them in across all of their devices. When the person runs your app on another device, the operating system supplies the sign-in token from their Apple Account, which your app uses to sign them in automatically. To implement Automatic Sign-In for your media-streaming app on Apple devices, see [`Signing people in to their media accounts automatically`](https://developer.apple.com/documentation/videosubscriberaccount/signing-people-in-to-media-apps-automatically).

This API works in conjunction with [`Video Subscriber Account`](https://developer.apple.com/documentation/videosubscriberaccount) to update or delete sign-in tokens from your web server. You might update or delete sign-in tokens from your web server in the following conditions:

- Your website offers UI to let the person opt out of Automatic Sign-In, or to flag a specific log in as unauthorized.
- The person changes their password and wants to sign out from all of their devices.

##### Authenticate Your Requests

The web service needs to know which tokens to operate on and to certify the authenticity of your requests, which you facilitate by adding a bearer token in your request header. See [`Authorizing API calls using bearer tokens`](https://developer.apple.com/documentation/videosubscriberaccount/authorizing-api-calls-using-bearer-tokens).

##### Test in the Sandbox Environment

To test the API on your web server during development, you can operate on test data by sending endpoint requests to the sandbox environment. From your web server, direct your test calls using the sandbox base URL: `https://api.storekit-sandbox.itunes.apple.com/`. For example, to call [`Update Sign-In Token`](update-this-token-for-all-associated-users.md) in the sandbox environment, send a request using the URL:

```other
https://api.storekit-sandbox.itunes.apple.com/account/v1/autoSignIn/update
```

To generate test data to operate on:

- Sign into your testing device with a Sandbox Apple Account (see [`Create a Sandbox Apple Account`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-a-sandbox-apple-account)).
- Run a development or Ad Hoc build on your testing device. Any sign-in token your app provides the operating system (via [`updateAutoSignInToken(_:updateContext:)`](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/updateautosignintoken(_:updatecontext:))) creates test data in the sandbox environment when the interaction occurs in any development or Ad Hoc deployment of your app.

## Topics

### Authorization
- [Authorizing API calls using bearer tokens](../videosubscriberaccount/authorizing-api-calls-using-bearer-tokens.md)
  Authenticate your endpoint calls by including a signed JWT token in the header of your requests.
### Token updates
- [Update Sign-In Token](update-this-token-for-all-associated-users.md)
  Updates a specific sign-in token to a new value.
- [object UpdateAutoSignInTokenRequest](updateautosignintokenrequest.md)
  The request body that contains the old sign-in token and the new sign-in token.
### Token deletion
- [Delete Sign-In Token](delete-this-token-for-all-associated-users.md)
  Deletes a specific sign-in token.
- [object DeleteAutoSignInTokenRequest](deleteautosignintokenrequest.md)
  The request body that contains the sign-in token to be deleted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AutomaticSignInAPI)*