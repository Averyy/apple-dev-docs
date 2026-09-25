# Interpreting Platform Single Sign-on authorization scopes

**Framework**: Authentication Services

Use authorization scopes to apply authentication policies.

#### Overview

When Platform Single Sign-on (Platform SSO) requests tokens from your identity provider, it can include the authorization scope in the request. The scope tells you why the user is authenticating, so you can apply the correct policy. For example, you can require multifactor authentication at login but not at screen unlock.

#### Request Authorization Scopes

To receive authorization scopes when Platform SSO sends a login or key request, set [`includePlatformSSOAuthorizationScopes`](asauthorizationproviderextensionloginconfiguration/includeplatformssoauthorizationscopes.md) to `true` in your [`ASAuthorizationProviderExtensionLoginConfiguration`](asauthorizationproviderextensionloginconfiguration.md).

Platform SSO sends those scopes to your [`keyEndpointURL`](asauthorizationproviderextensionloginconfiguration/keyendpointurl.md) and [`tokenEndpointURL`](asauthorizationproviderextensionloginconfiguration/tokenendpointurl.md).

For web-based authentication, Platform SSO sends the scopes to the [`authorizationURL`](asauthorizationproviderextensionloginconfiguration/authorizationurl.md) when you use a static OAuth URL. When you use a dynamic OAuth URL, Platform SSO sends the scopes to the `authorizationURL` that a pre-authentication request returns. For more information on the login request and web-based authentication, see [`Creating and validating a login request`](creating-and-validating-a-login-request.md) and [`Implementing web-based authentication with Platform Single Sign-on`](implementing-web-based-authentication.md).

#### Receive Authorization Scopes

All authorization scopes that Platform SSO provides use the prefix `urn:apple:platformsso:auth:`:

| Scope | Usage |
| --- | --- |
| `auth-prompt` | An in-session authentication prompt; for example, background re-authentication at session start, after a network change, or on a token-refresh timer. |
| `create-user` | Platform SSO creates a new local account at the login window using credentials from the identity provider. |
| `elevation` | Platform SSO prompts the user to re-authenticate to elevate privileges (administrator authorization prompt). |
| `fallback` | Platform SSO falls back to OpenID because the primary credential (for example, Touch ID) isn’t usable. Platform SSO sends this scope on both the authorization request and the corresponding token verification. |
| `login` | The user logs in at the login window or unlocks FileVault. Also the default scope when no other context applies. |
| `password-change` | The user is in the password-change flow. |
| `refresh` | A silent token refresh with no user interaction. If refresh fails and falls back to a real login, the scope reverts to the originating caller’s scope (for example, `auth-prompt`). |
| `setup-assistant` | An authentication during initial device setup in Setup Assistant. This includes embedded system-session authentication that isn’t an elevation prompt. |
| `temporary-session` | An authentication for an Authenticated Guest Mode session. |
| `unlock` | The user unlocks their Mac from the screen-locked state when they’re already logged in. |

> **Note**: Platform SSO adds exactly one of these scopes per request. The scopes are mutually exclusive based on the originating user action.

For most session-driven flows, Platform SSO selects the scope from the session type:

| Session type | Resulting scope |
| --- | --- |
| Elevation prompt | `elevation` |
| In-session prompt | `auth-prompt` |
| Login window or FileVault unlock | `login` |
| Password change | `password-change` |
| Setup Assistant | `setup-assistant` |
| Screen unlock | `unlock` |

A few scopes fall outside the session-type mapping:

- Platform SSO applies the special-purpose scopes (`create-user`, `temporary-session`, `fallback`, and `refresh`) based on the specific feature path instead of the session type.
- When Platform SSO has no specific context, it uses `login` as the default. Treat `login` as the safe baseline and reserve stricter policy for the more specific scopes.
- For fallback, Platform SSO sends the same scope on both legs of the OpenID handshake — the initial authorization request and the subsequent token verification. Sending the same scope lets your identity provider apply policy decisions consistently across both requests.

## See Also

- [Configuring authentication with the identity provider (IdP)](configuring-authentication-with-the-identity-provider-idp.md)
  Specify how Platform SSO authenticates with the identity provider.
- [class ASAuthorizationProviderExtensionLoginConfiguration](asauthorizationproviderextensionloginconfiguration.md)
  An interface for configuring platform single sign-on.
- [class ASAuthorizationProviderExtensionLoginManager](asauthorizationproviderextensionloginmanager.md)
  An interface to maintain platform single sign-on (SSO) during authentication and registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/interpreting-platform-single-sign-on-authorization-scopes)*