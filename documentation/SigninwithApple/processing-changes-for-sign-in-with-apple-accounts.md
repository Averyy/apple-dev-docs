# Processing changes for Sign in with Apple accounts

**Framework**: Sign in with Apple

Manage user-initiated modifications to maintain privacy with server-to-server notifications.

#### Overview

Sign in with Apple users can modify their accounts, including deleting or disabling their Apple Accounts. If your app or website hosts such an account, Apple can alert you when these changes occur by delivering developer notifications to your server. To learn how your users manage their account preferences for your app, see [`Manage the apps that you use with Sign in with Apple`](https://developer.apple.comhttps://support.apple.com/en-us/HT210426).

##### Set Up Your Server

To receive server notifications for Sign in with Apple, your server must support the Transport Layer Security (TLS) 1.2 protocol or later. When determining the endpoint URL on your server to receive notifications, you may use the same URL for multiple developer teams and apps. To configure your Sign in with Apple service to receive notifications, see [`Enabling server-to-server notifications`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/enabling-server-to-server-notifications).

##### Decode and Validate the Notifications

These notifications contain a cryptographically signed payload, in JSON Web Signature (JWS) format, signed by Apple’s private key. After your server receives a notification, examine the JWS payload and use the algorithm specified in the header’s `alg` parameter to validate the signature. For more information, see [`Fetch Apple’s public key to verify token signatures`](https://developer.apple.com/documentation/signinwithapplerestapi/fetch-apple's-public-key-for-verifying-token-signature).

After validating the token signature, your server performs work according to the `type` value in the `events` claim of the token. The notification payload object contains information about user-initiated account modification events. The event types include the following:

Expect an HTTP POST response similar to the following example:

```console
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
    "payload": "<SERVER_TO_SERVER_NOTIFICATION_JWT>"
}
```

##### Process a Users Email Forwarding Change

Users can enable or disable email forwarding to your app or website. When a user enables email forwarding, Apple sends a JWT to your registered endpoint URL with the `type` value of `email-enabled` in the `events` claim. A decoded payload for an email-enabled notification has the following format:

```json
{
    "iss": "https://appleid.apple.com",
    "aud": "com.mytest.app",
    "iat": 1508184845,
    "jti": "abede...67890",
    "events": {
        "type": "email-enabled",
        "sub": "820417.faa325acbc78e1be1668ba852d492d8a.0219",
        "email": "ep9ks2tnph@privaterelay.appleid.com",
        "is_private_email": "true"
        "event_time": 1508184845
    }
}
```

When a user disables email forwarding, Apple sends a JWT to your registered endpoint URL with the `type` value of `email-disabled` in the `events` claim. A decoded payload for an email-disabled notification has the following format:

```json
{
    "iss": "https://appleid.apple.com",
    "aud": "com.mytest.app",
    "iat": 1508184845,
    "jti": "abede...67890",
    "events": {
        "type": "email-disabled",
        "sub": "820417.faa325acbc78e1be1668ba852d492d8a.0219",
        "email": "ep9ks2tnph@privaterelay.appleid.com",
        "is_private_email": "true"
        "event_time": 1508184845
    }
}
```

To allow or prevent sending emails to the email address, be sure to update your server’s records according to your process. For more information, see [`Communicating using the private email relay service`](communicating-using-the-private-email-relay-service.md).

##### Process Disabling and Deleting a Users Apple Account

Users can disable their Apple Account for a specific primary app ID, or delete their Apple Account account entirely. When a user disables their Apple Account for an app or app group, Apple sends a JWT to your registered endpoint URL with the `type` value of `consent-revoked` in the `events` claim. A decoded payload for a consent-revoked notification has the following format:

```json
{
    "iss": "https://appleid.apple.com",
    "aud": "com.mytest.app",
    "iat": 1508184845,
    "jti": "abede...67890",
    "events": {
        "type": "consent-revoked",
        "sub": "820417.faa325acbc78e1be1668ba852d492d8a.0219",
        "event_time": 1508184845
    }
}
```

When a user requests for Apple to permanently delete their Apple Account, Apple sends a JWT to your registered endpoint URL with the `type` value of `account-delete` in the `events` claim. A decoded payload for an account-delete notification has the following format:

```json
{
    "iss": "https://appleid.apple.com",
    "aud": "com.mytest.app",
    "iat": 1508184845,
    "jti": "abede...67890",
    "events": {
        "type": "account-delete",
        "sub": "820417.faa325acbc78e1be1668ba852d492d8a.0219",
        "event_time": 1508184845
    }
}
```

> ❗ **Important**:  When a user permanently deletes their Apple Account, Sign in with Apple invalidates all user tokens and disables email forwarding for all associated apps. For native apps, the system doesn’t send a [`credentialRevokedNotification`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDProvider/credentialRevokedNotification). Use [`getCredentialState(forUserID:completion:)`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDProvider/getCredentialState(forUserID:completion:)) to respond to account deletion events.

To indicate when the user disables or permanently deletes their Apple Account, be sure to update your server’s records according to your process. For more information about handling Managed Apple Accounts, see [`Obtaining information about people and classes`](https://developer.apple.com/documentation/RosterAPI/obtaining-information-about-people-and-classes).

## See Also

- [Sign in with Apple JS](../signinwithapplejs/signinwithapplejs.md)
  Provide users a fast, secure way to sign in to your web service with their Apple Account.
- [Sign in with Apple REST API](../signinwithapplerestapi/signinwithapplerestapi.md)
  Communicate between your app servers and Apple’s authentication servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts)*