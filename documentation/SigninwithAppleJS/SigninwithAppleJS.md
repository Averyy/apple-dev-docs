# Sign in with Apple JS

**Framework**: SigninwithAppleJS  
**Kind**: module  
**Role**: Framework

Provide users a fast, secure way to sign in to your web service with their Apple Account.

## Mentions

- [Configuring your environment for Sign in with Apple](../SigninwithApple/configuring-your-environment-for-sign-in-with-apple.md)
- [Incorporating Sign in with Apple into other platforms](../SigninwithApple/incorporating-sign-in-with-apple-into-other-platforms.md)

#### Overview

[Sign in with Apple](../SigninwithApple/SigninwithApple.md) is the fastest way to onboard new users securely and provides two-factor authentication. Using Sign in with Apple JS, users can to log into your website with their Apple Account rather than creating a new account and password.

Enabling Sign in with Apple for your app begins with registering your app in your Apple Developer account. When integrating the API with your app, consider button presentation style, notification options, server integration, and what kind of user information to request.

## Topics

### Essentials
- [Configuring your webpage for Sign in with Apple](../SigninwithApple/configuring-your-webpage-for-sign-in-with-apple.md)
  Prepare your webpage to authorize users through Sign in with Apple.
- [Communicating using the private email relay service](../SigninwithApple/communicating-using-the-private-email-relay-service.md)
  Stay in touch with users who opt for an anonymous email address with Sign in with Apple.
### Authentication and configuration
- [SignInResponseI](./signinresponsei.md)
  An object that contains the response to a sign-in request.
- [SignInErrorI](./signinerrori.md)
  An object that contains error information.
- [AuthorizationI](./authorizationi.md)
  An object that contains a user’s authorization information.
- [AuthI](./authi.md)
  The interface used to authenticate a user.
- [ClientConfigI](./clientconfigi.md)
  An object that contains a user’s configuration information.
### Multiplatform use
- [Incorporating Sign in with Apple into other platforms](../SigninwithApple/incorporating-sign-in-with-apple-into-other-platforms.md)
  Add Sign in with Apple capabilities to apps that can’t directly access Sign in with Apple JS.
### User identification
- [NameI](./namei.md)
  An object that contains the user’s full name from their Apple Account or a user-submitted value provided from the Sign in with Apple UI.
- [UserI](./useri.md)
  An object that contains the user’s name and email address.

## See Also

### Web support
- [Sign in with Apple REST API](https://developer.apple.com/documentation/signinwithapplerestapi)
  Communicate between your app servers and Apple’s authentication servers.
- [Displaying Sign in with Apple buttons on the web](../SigninwithApple/displaying-sign-in-with-apple-buttons-on-the-web.md)
  Configure the appearance of Sign in with Apple buttons with CSS styles.
- [Configuring your environment for Sign in with Apple](../SigninwithApple/configuring-your-environment-for-sign-in-with-apple.md)
  Authenticate users with your web service by associating an existing app with a Services ID and private key.
- [Processing changes for Sign in with Apple accounts](../SigninwithApple/processing-changes-for-sign-in-with-apple-accounts.md)
  Manage user-initiated modifications to maintain privacy with server-to-server notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs)*