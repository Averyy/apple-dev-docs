# Configuring your environment for Sign in with Apple

**Framework**: Sign in with Apple

Authenticate users with your web service by associating an existing app with a Services ID and private key.

#### Overview

To support Sign in with Apple on your website, or in your app on another platform, configure your developer account to associate a Sign in with Apple-enabled app with a Services ID and a private key. To support email communication with your users, register your domain names and outbound email sources. Your server can register for notifications for user account changes that affect your developer account. After configuration, use the Services ID as the client identifier when authenticating or validating users with [`Sign in with Apple JS`](https://developer.apple.com/documentation/signinwithapplejs) and [`Sign in with Apple REST API`](https://developer.apple.com/documentation/signinwithapplerestapi).

##### Enable an App Id

For users to authenticate with your web service, you must have an existing app in the App Store that uses Sign in with Apple. To enable an existing app, see [`Implementing User Authentication with Sign in with Apple`](https://developer.apple.com/documentation/AuthenticationServices/implementing-user-authentication-with-sign-in-with-apple). Enable the Sign in with Apple capability for an app in Xcode, or by editing an App ID configuration in [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources). When configuring your App ID, you have the following options:

- Enable the App ID as a primary App ID
- Enable the App ID and group with an existing primary App ID

Choose to enable as a primary App ID if you’re enabling a new app, or an existing app for the first time. You can use primary App IDs on their own, or to enable identifiers for related apps and websites through app grouping.

Choose to group with an existing primary App ID if you’re associating an App ID with a related app, such as an App ID for the iOS version of your Mac app. App grouping ensures that users need to provide consent to share their information only once for each group of apps and websites. For more information about grouping apps, see [`Group Apps for Sign in with Apple`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/group-apps-for-sign-in-with-apple).

##### Create a Services Id

You must use a unique identifier — a Services ID — to register each web service that supports Sign in with Apple authentication. You configure the Services ID with the registered domains and return URLs for a primary app. When configuring your web service in Certificates, Identifiers & Profiles, you must register and verify all top-level domains and subdomains that incorporate Sign in with Apple. Domains associate with your Apple Developer Team ID. As a result, for each Services ID you enable for Sign in with Apple, the following applies:

- Organizations can register up to 100 website URLs
- Individuals can register up to 10 website URLs

The Sign in with Apple servers use return URLs, also known as , to provide your web service with an authorization response, or to validate tokens. Because of this, each registered URL must be absolute and must include the scheme, host, and path. The following is an example return URL:

```console
https://example.com/path/to/endpoint
```

For more information about configuring your Services ID, see [`Configure Sign in with Apple for the web`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-sign-in-with-apple-for-the-web).

##### Create a Private Key

Apple associates your Sign in with Apple private key with a primary app, and its app group, if available. You use a private key to sign developer tokens when communicating with the Sign in with Apple servers. For example, when generating and validating tokens for user authentication, app transfer, and user migration to a newly transferred developer team, you use the private key ID in the token header, and the private key signs the token. To validate your web service, Sign in with Apple requires you to create a JSON web token (JWT) with the key identifier (`kid`) in the header. For information on getting a key identifier, see [`Get a key identifier`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-keys/get-a-key-identifier). For information on generating the JWT, see [`Creating a client secret`](https://developer.apple.com/documentation/AccountOrganizationalDataSharing/creating-a-client-secret).

Each primary app can have a maximum of two private keys.

> ❗ **Important**:  Never share your private keys outside of your developer team. If a private key becomes compromised, create a new private key for the primary app. Then, after transitioning to the new key, revoke the old private key. For more information, see [`Create a Sign in with Apple private key`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/create-a-sign-in-with-apple-private-key).

##### Register Email Sources for Communication

To communicate with users who opt to use an anonymous email address with Sign in with Apple, you must register your outbound email domains, subdomains, or email addresses as email sources for the Private Email Relay Service. Email sources associate with your Apple Developer Team ID, and have the following parameters:

- Organizations can register up to 100 outbound email sources
- Individuals can register up to 32 outbound email sources

You must authenticate all registered domains with the Sender Policy Framework (SPF), the DomainKeys Identified Mail (DKIM) protocol, or both to deliver your outbound emails. Authenticate outbound emails using both SPF and DKIM whenever possible.

When the Private Email Relay Service detects undelivered emails from your account, it notifies your developer team account holders and administrators by email. For more information about registering outbound email domains or handling email notifications, see [`Configure Private Email Relay Service`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service).

##### Register a Server to Server Notification Endpoint

To receive important updates about your users and their accounts, enable the Sign in with Apple server-to-server notification endpoint. Your server must support TLS 1.2 or later to receive notifications. Configure the endpoint by editing your App ID configurations in [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources). Each app group receives a notification when users take any of the following actions:

- Change email forwarding preferences
- Delete their app account
- Permanently delete their Apple ID

Each app group registers one absolute URL that includes the scheme, host, and path. The following is an example endpoint:

```console
https://example.com/path/to/endpoint
```

For more information about server-to-server notifications, see [`Processing changes for Sign in with Apple accounts`](processing-changes-for-sign-in-with-apple-accounts.md).

## See Also

- [Displaying Sign in with Apple buttons on the web](displaying-sign-in-with-apple-buttons-on-the-web.md)
  Configure the appearance of Sign in with Apple buttons with CSS styles.
- [Processing changes for Sign in with Apple accounts](processing-changes-for-sign-in-with-apple-accounts.md)
  Manage user-initiated modifications to maintain privacy with server-to-server notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapple/configuring-your-environment-for-sign-in-with-apple)*