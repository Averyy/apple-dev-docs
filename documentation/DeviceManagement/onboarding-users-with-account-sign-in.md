# Onboarding users with account sign-in

**Framework**: Device Management

Implement user-initiated, identity-focused authentication flows.

#### Overview

The account-driven enrollment flow is a user identity-focused flow that a person initiates as an account sign-in behavior. An advantage of this flow is that the server is able to authenticate the person who’s attempting to enroll before sending any data, and can perform ongoing authentication to ensure the person is still associated with the enrolled device.

MDM has traditionally offered two enrollments modes:

- Device enrollment: For organization-owned devices
- User enrollment: For user-owned devices, such as BYOD (bring your own device) situations

Each mode results in an MDM enrollment with unique characteristics that govern which commands and profiles are available to use, and determine whether data separation is in place. Previously, the system triggered these enrollments with a profile-based installation flow, which is deprecated in favor of the account-driven flows.

The account-driven flow supports authenticating both device and user enrollments through a web-based authentication. This authentication uses Apple’s Authentication Services framework, providing you with either a simple access, token-based authentication method, or an OAuth 2 method. It also supports the Enrollment SSO option that allows a full single sign-on experience for MDM enrollment, running enterprise apps, and providing access to enterprise websites and other resources.

There are five key elements to the flow:

- Service discovery: The client uses a user account identifier to determine which MDM server to connect to when beginning the enrollment flow. The server determines whether to use a device or a user enrollment.
- User authentication: The client and server perform an authentication protocol to authenticate the user to the server.
- Access token: The authentication protocol returns an access token to the client, which stores it and uses it for subsequent authorization of HTTP requests.
- Enrollment: The client uses the access token to complete the MDM enrollment, which requires the user to sign in to a Managed Apple Account.
- Ongoing authorization: The client sends the access token in each MDM HTTP request to the server. The server can opt to invalidate the token and force the client to perform another authentication protocol operation to reauthenticate the user and retrieve a new access token. In the case of the OAuth 2 protocol, a silent refresh option is also available.

> **Note**:  The ongoing authorization is associated with the current user of the device. That means in macOS, the access token isn’t present in MDM device channel HTTP requests, but is present in user channel HTTP requests. In iOS, the access tokens are present on all MDM HTTP requests because there’s no distinction between device and user channels (except for Shared iPad, which doesn’t support this enrollment mode).

The account-driven flow is supported in iOS 15 for user enrollments, and in iOS 16, macOS 14, and visionOS 1.1, and later for both device and user enrollments.

##### Implement the Simple Authentication Flow

For the simple access token method, the device follows these steps:

1. It fetches an access (authorization) token from the MDM server’s web-auth service after it successfully authenticates the user.
2. It then uses the access token to authorize subsequent requests to the MDM server to fetch the enrollment profile and the ongoing MDM requests for managing the device after enrollment.

The server can opt to invalidate the access token at any point, requiring the user to reauthenticate as proof that they’re still actively using the device. For information on the simple authentication enrollment flow, see [`Implementing the simple authentication account-driven enrollment flow`](implementing-the-simple-authentication-user-enrollment-flow.md).

##### Implement the Oauth 2 Flow

The OAuth 2 method follows these steps:

1. The device uses the standard OAuth 2 authorization grant flow to authenticate the user.
2. It fetches an access token and an optional refresh token. It then uses the access token to authorize subsequent requests to the MDM server to fetch the enrollment profile and the ongoing MDM requests for managing the device after enrollment.

The access token can have a short lifetime, and the server can also opt to treat it as invalid at any time. If the device has a refresh token from the OAuth 2 authorization server, the device can silently refresh the short-lived access token. If it doesn’t have a refresh token, or the refresh request fails, the system requires the user to reauthenticate as proof that they’re still actively using the device. For more information on the OAuth 2 enrollment flow, see [`Implementing the OAuth 2 authentication account-driven enrollment flow`](implementing-the-oauth2-authentication-user-enrollment-flow.md).

##### Implement Enrollment Sso

For Enrollment SSO, use one of the two authentication methods described above (preferably, OAuth 2). The initial authentication challenge from the server includes an HTTP header (`X-Apple-MDM-ESSO`), indicating that Enrollment SSO is available and the device needs to use it. That header has a URL as its value, and the client downloads a JSON document from that URL. The JSON document contains details about an App Store-hosted extensible SSO app that the client downloads, installs, and configures. That app intercepts the subsequent authentication requests to perform the custom single sign-on. After the system presents the app, the regular account-driven enrollment authentication flow proceeds. The system asks the SSO app to return the appropriate tokens for the corresponding authentication method. For more information on the Enrollment SSO enrollment flow, see [`Implementing the Enrollment SSO flow`](implementing-the-enrollment-sso-flow.md).

## Topics

### Detailed flow instructions
- [Implementing the simple authentication account-driven enrollment flow](implementing-the-simple-authentication-user-enrollment-flow.md)
  Examine the steps between the user, client, server, and Apple services in the simple authentication flow.
- [Implementing the OAuth 2 authentication account-driven enrollment flow](implementing-the-oauth2-authentication-user-enrollment-flow.md)
  Examine the steps between the user, client, server, and Apple services in the OAuth 2 flow.
- [Implementing the Enrollment SSO flow](implementing-the-enrollment-sso-flow.md)
  Examine the steps between the user, client, and server in the Enrollment SSO flow.

## See Also

- [Enrolling with Platform Single Sign-on](enrolling-with-platform-single-sign-on.md)
  Authenticate users during device enrollment using Platform Single Sign-on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/onboarding-users-with-account-sign-in)*