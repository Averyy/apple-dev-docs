# Reauthenticating a person to manage apps

**Framework**: MarketplaceKit

Renew your app’s authorization when an app needs updating or when a device restores from backup.

#### Overview

If your marketplace app restricts the download of apps according to specific criteria, such as signing in, or purchasing a subscription, you issue an access token that the system includes in communication with your server. When the access token expires, the system prompts a person to sign in to retrieve a new token. This reauthentication occurs in the following situations:

- Reinstallation of your marketplace app, when a person restores their device from a backup and your alternative app marketplace is one of the apps to restore. This situation differs from the original install because it lacks the context of an existing marketplace website session.
- App updates, when a person interacts with your marketplace app’s UI, for example, by tapping an app’s Update button. It can also happen, when Automatic Updates are on, as the system periodically checks your server for newer versions of the installed apps.

> **Note**: [`MarketplaceKit`](MarketplaceKit.md) implements the OAuth2.0 specification for reauthentication described in [`RFC 8693`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc8693).

[`MarketplaceKit`](MarketplaceKit.md) implements the OAuth2.0 specification for reauthentication described in [`RFC 8693`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc8693).

#### Reinstall an Alternative Marketplace From a Backup

If a person restores their device from a backup, a previously installed alternative marketplace app and its apps display as darkened placeholders on the Home Screen. When the person taps a placeholder, the system attempts to reinstall the apps beginning with the alternative marketplace. The system calls the `restores` endpoint in your `marketplace-kit` configuration file (see [`Installing your app from your website`](installing-your-app-from-your-website.md)) but the communication lacks an access or bearer token. When you restrict your alternative marketplace app’s downloads to qualified users, notice the missing access token and replace it by reauthenticating the person. Respond with `HTTP` code `401` or `403` and the system instructs the person to log in by presenting a Home Screen prompt that reads:

```None
Verification Required 
Tap Continue and sign in to install this app.
```

The system calls your `authorization_endpoint` endpoint, as specified in your server’s `oauth-authorization-server` configuration. For more information about the `oauth-authorization-server` configuration, see [`Installing your app from your website`](installing-your-app-from-your-website.md).

An example `authorization_endpoint` call follows, where “example.com/authorize” is the marketplace server’s authorization endpoint:

```None
https://example.com/authorize
    ?login_hint=user-name@example.com
    &client_id=D4C1C937-D9B4-4BB6-BCD3-5E0850143EF5
    &code_challenge_method=S256
    &response_type=code
    &code_challenge=sib4eJtJBmkL312KjyoNlSFeDrpCOKnUwheZGipfnUY[...]
    &state=EE01F1C6-5123-402E-909D-71E596780759
    &redirect_uri=app-distribution-oauth://
```

| `authorization_endpoint` parameter | Description |
| --- | --- |
| `login_hint` | A value that the system provides to identify a person’s account ID or user name on the login page. |
| `client_id` | A value that uniquely identifies the account, device, and marketplace combination. The system provides this value during the initial authentication and download. |
| `code_challenge_method` | The type of code challenge among Plain or SHA256. |
| `response_type` | The authorization processing flow; `"code"`, for this purpose. |
| `code_challenge` | A Base64-URL-encoded string of the SHA256 hash of the code verifier. The system provides the code verifier to your token endpoint later on in the flow. |
| `state` | A value that enhances security. Return it in your authorization response. |
| `redirect_uri` | A special URL scheme at which the system confirms authorization. |

> 💡 **Tip**: For more information about: - Login hints, response types, or redirect URI, see [`OpenID Connect Core`](https://developer.apple.comhttps://openid.net/specs/openid-connect-core-1_0.html).
- Code challenges, see the [`RFC7636 - Proof Key for Code Exchange`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7636).

For more information about:

- Login hints, response types, or redirect URI, see [`OpenID Connect Core`](https://developer.apple.comhttps://openid.net/specs/openid-connect-core-1_0.html).
- Code challenges, see the [`RFC7636 - Proof Key for Code Exchange`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7636).

In response to the call, your authorization endpoint provides a login page for the person to enter their credentials. On the login page, display the account based on the `login_hint` request parameter.

After your server validates the person’s credentials, your login page routes to the `redirect_uri` request parameter. Add an authorization code into the call by setting a `code` parameter to a one-time, generated value. For example:

```None
app-distribution-oauth:?code=sib4eJtJBmkL312KjyoNlSFeDrpCOKnUwheZGip[...]
```

For more information on generating an authorization response, see [`OAuth 2.0 Authorization Code Grant`](https://developer.apple.comhttps://oauth.net/2/grant-types/authorization-code).

Next, the system calls your `token_endpoint` and provides the authorization code. Here’s an example POST body:

```http
code=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJvZGVnYS1rZXlpZCJ[...]
&code_verifier=7SJJJc6vi1D7x.SKZ4SuEijHA9C.FkASXVUo9E25ns1[...]
&client_id=D4C1C937-D9B4-4BB6-BCD3-5E0850143EF5
&grant_type=authorization_code
```

| `token_endpoint` parameter | Description |
| --- | --- |
| `code` | A one-time code for the authorization. |
| `code_verifier` | A cryptographically random string of characters from which the system creates the `code_challenge`. |
| `client_id` | A value that uniquely identifies the account, device, and marketplace combination. The system provides this value during the initial authentication and download. |
| `grant_type` | The grant type; `authorization_code`, for this purpose. |

In response, your token endpoint sends an access token and an optional refresh token:

```None
{
    "token_type": "Bearer",
    "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
    "expires_in": 86400,
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImt[...]",
    "scope": "all",
    "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im[...]"
}
```

Completion of the authentication flow authorizes the system to reinstall the app on the person’s behalf. Next, the system again calls the marketplace’s `"restores"` endpoint that the `marketplace-kit` configuration specifies. This time, the system provides the access or bearer token in the header. For more information about serving the `"restores"` request, see [`Installing your app from your website`](installing-your-app-from-your-website.md).

#### Reinstall an App From a Backup

After the system restores your alternative marketplace app from a backup, it proceeds to reinstall the other apps from your marketplace. The system sends a POST to your `restores` endpoint with a header decorated with the access token. Your marketplace app adds the token to the header by implementing the [`MarketplaceExtension`](marketplaceextension.md) method [`additionalHeaders(for:account:)`](marketplaceextension/additionalheaders(for:account:).md). Then, your server reads the token in the request and determines the response:

- If the access token is valid and the apps are available, return the apps for installation.
- If the token is missing, respond from your marketplace server with an HTTP `401`.
- If the token is present but invalid, respond with an HTTP `403`.

In any of these cases, the system routes the person from the darkened app icon on the Home Screen into your alternative marketplace app to reauthenticate with a prompt that reads:

```None
Verification Required 
To install "App 1", you need to verify your account in Megabyte Mart.
```

When your marketplace app launches, check for a missing or invalid access token. In either case, you can reauthenticate the person by presenting a webpage with [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) that enables the person to enter their credentials.

After the person signs in, store the renewed access token locally. Call [`didAuthenticate(account:)`](applibrary/didauthenticate(account:).md), which instructs the system to retry the app installation. This time, your marketplace extension decorates the header of the restores endpoint POST with a renewed access token for the system to complete the reinstallation.

#### Reauthenticate a Person in Your Marketplace App or Extension

If your marketplace app is running while your marketplace server encounters an invalid access token, the system calls your extension’s [`requestFailed(with:)`](marketplaceextension/requestfailed(with:).md) implementation. In this callback, your marketplace app can correct the issue by reauthenticating the person. For example, you can set a flag to present a webpage in your app with [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) that enables the person to enter their credentials before retrying the update.

[`MarketplaceExtension`](marketplaceextension.md) can’t present UI, so if your marketplace isn’t running, you can explore reauthenticating another way, such as by exchanging a refresh token for a renewed access token with your token endpoint.

For example, if the system encounters an invalid access token while performing automatic background app updates, reauthorize the device in [`requestFailed(with:)`](marketplaceextension/requestfailed(with:).md) and return `true` to instruct the system to call your `restores` endpoint again. The system calls your marketplace extension’s [`additionalHeaders(for:account:)`](marketplaceextension/additionalheaders(for:account:).md) implementation and you supply the renewed access token to complete the update.

## See Also

- [com.apple.developer.marketplace.app-installation](../BundleResources/Entitlements/com.apple.developer.marketplace.app-installation.md)
  The entitlement that enables an app to vend other apps as an alternative app marketplace.
- [com.apple.developer.browser.app-installation](../BundleResources/Entitlements/com.apple.developer.browser.app-installation.md)
  The entitlement that enables a browser to install alternative-distribution apps from a website.
- [App License Delivery SDK](../AppLicenseDeliverySDK/AppLicenseDeliverySDK.md)
  Secure the installation of alternative distribution apps on iOS or iPadOS devices by vending licenses from your web server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/reauthenticating-a-person-to-manage-apps)*