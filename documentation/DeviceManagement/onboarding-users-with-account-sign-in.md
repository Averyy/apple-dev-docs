# Onboarding users with account sign-in

**Framework**: Device Management

Examine new, user-initiated, identity-focused flows.

#### Overview

In iOS 15, users can sign in with an identity focused flow. This flow differs from the profile based enrollment introduced in iOS 13. An advantage of this flow is that the server is able to authenticate the user attempting to enroll, before having to send any data, and being able to carry out on-going authentication to ensure the user is still associated with the enrolled device.

The protocol supports authenticating user enrollments through a web-based authentication. This authentication uses Apple’s Web-based Authentication Services framework, providing you with a simple access token based authentication method, or an OAuth2 method. It also supports the Enrollment SSO option, that allows a full single-sign-on experience for MDM enrollment, running enterprise apps, and access to enterprise websites and other resources.

##### Implement the Simple Authentication Flow

For the simple access token method, the device follows these steps:

1. It fetches an access (authorization) token from the MDM server’s web-auth service after it has successfully authenticated the user.
2. This access token is then used to authorize subsequent requests to the MDM server to fetch the enrollment profile, and the on-going MDM requests used to manage the device after enrollment.

The server can choose to invalidate the access token at any point, requiring the user to re-authenticate as proof that they’re still actively using the device. This method was introduced in iOS 15. For information on the simple authentication enrollment flow, see [`Implementing the simple authentication user-enrollment flow`](implementing-the-simple-authentication-user-enrollment-flow.md).

##### Implement the Oauth2 Flow

For the OAuth2 method follow these steps,

1. The device uses the standard OAuth2 authorization grant flow to authenticate the user.
2. It fetches an access token and an optional refresh token. This access token is then used to authorize subsequent requests to the MDM server to fetch the enrollment profile, and the on-going MDM requests used to manage the device after enrollment.

The access token can have a short lifetime, and the server can also choose to treat it as invalidate at any time. If the device has a refresh token supplied by the OAuth2 authorization server, the device can silently refresh the short-lived access token. If a refresh token wasn’t supplied, or the refresh request fails, the system requires the user to re-authenticate as proof that they’re still actively using the device. This method was introduced in iOS 16. For more information on the OAuth2 enrollment flow, see [`Implementing the OAuth2 authentication user-enrollment flow`](implementing-the-oauth2-authentication-user-enrollment-flow.md).

##### Implement Enrollment Sso

For Enrollment SSO, use one of the two authentication methods described above (preferably, OAuth2). However, when the device receives the initial authentication challenge from the server, an HTTP header (`X-Apple-MDM-ESSO`) is present indicating that Enrollment SSO is available and the device needs to use it. That header has a URL as its value, and the client downloads a JSON document from that URL. The JSON document contains details about an AppStore-hosted extensible SSO app that the client downloads, installs, and configures. That app intercepts the subsequent authentication requests to carry out the custom single-sign-on. Once the app is present, the normal user enrollment authentication flow proceeds. The system expects the SSO app to return the appropriate tokens for the corresponding authentication method.

There are five key elements to the SSO flow:

- Service discovery: the client uses a user account identifier to determine which MDM server to connect to, to start the enrollment flow.
- User authentication: the client and server carry out an authentication protocol to authenticate the user to the server.
- Access token: the authentication protocol returns an access token to the client, which stores the token and uses it for subsequent authorization of HTTP requests.
- Enrollment: the client uses the access token to complete the MDM enrollment, including the user having to sign in to a Managed Apple ID account.
- Ongoing authorization: the client sends the access token in every MDM HTTP request sent to the server. The server can choose to invalidate the token and force the client to carry out another authentication protocol operation to re-authenticate the user and retrieve a new access token. In the case of the OAuth2 protocol, a silent refresh option is also available.

## Topics

### Detailed flow instructions
- [Implementing the simple authentication user-enrollment flow](implementing-the-simple-authentication-user-enrollment-flow.md)
  Understand the steps of the authentication flow between the user, client, server, and Apple services.
- [Implementing the OAuth2 authentication user-enrollment flow](implementing-the-oauth2-authentication-user-enrollment-flow.md)
  Understand the steps of the OAuth2 flow between the user, client, server, and Apple services.

## See Also

- [object EnrollmentSSODocument](enrollmentssodocument.md)
  Enrollment SSO streamlines the MDM enrollment process, reduces sign-ins, and improves security.
- [Discover Authentication Servers](get-.well-known-com.apple.remotemanagement.md)
  Get a list of available authentication servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/onboarding-users-with-account-sign-in)*