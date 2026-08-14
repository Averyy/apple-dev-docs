# Implementing web-based authentication with Platform Single Sign-on

**Framework**: Authentication Services

Support modern, phishing-resistant, and flexible authentication methods.

#### Overview

With web-based authentication, Platform Single Sign-on (Platform SSO) presents a built-in web view that loads your identity provider’s OAuth 2.0/OpenID Connect (OIDC) authorization endpoint. You define the content of the web view and any required authentication steps.

#### Prepare the Sso Extension

Web-based authentication uses the Platform SSO 2.0 protocol and specifically requires support of the key service and shared device keys. For more information, see [`Creating extensions that support Platform SSO`](creating-extensions-that-support-platform-sso.md).

The SSO extension needs to support the [`tokenExchange`](asauthorizationproviderextensionsupportedgranttypes/tokenexchange.md) grant type and return this value from [`supportedGrantTypes()`](asauthorizationproviderextensionregistrationhandler/supportedgranttypes().md) during device registration.

#### Provide a Login Configuration

When you set [`ASAuthorizationProviderExtensionAuthenticationMethod.openID`](asauthorizationproviderextensionauthenticationmethod/openid.md), or when the options include [`ASAuthorizationProviderExtensionRequestOptionsOpenIDFallback`](asauthorizationproviderextensionrequestoptions/asauthorizationproviderextensionrequestoptionsopenidfallback.md), the SSO extension needs to provide a login configuration for web-based authentication.

During web-based authentication, Platform SSO displays a web view that loads content from the authorization endpoint. The URL of the authorization endpoint can be static or dynamic. In both cases, the SSO extension needs to provide information to Platform SSO as part of the login configuration when performing the registration.

Regardless of how you provide the URL, Platform SSO makes the following changes in the login request:

| Key | Change |
| --- | --- |
| `redirect_uri` | Removed if already present and set to `com.apple.platformsso://callback`. |
| `login_hint` | Removed if already present and set to the identity provider username. |
| `scope` | Removed if already present and re-added as a whitespace-deduplicated merge of the URL’s scope and the Platform SSO specific login scope. If the login request includes a request object, Platform SSO updates the scope to the same value before signing. |

##### Use a Static Oauth Url

This method uses a static URL for the authorization endpoint:

- Set [`federationType`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.property.md) or [`fallbackFederationType`](asauthorizationproviderextensionloginconfiguration/fallbackfederationtype.md) to [`ASAuthorizationProviderExtensionLoginConfiguration.FederationType.openID`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.enum/openid.md).
- Set [`authorizationURL`](asauthorizationproviderextensionloginconfiguration/authorizationurl.md) to the full static URL to use for login.

##### Use a Dynamic Oauth Url

This method retrieves the authorization URL from the authorization endpoint using the federation pre-authentication request and uses it for authentication:

- Set [`federationType`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.property.md) or [`fallbackFederationType`](asauthorizationproviderextensionloginconfiguration/fallbackfederationtype.md) to [`ASAuthorizationProviderExtensionLoginConfiguration.FederationType.dynamicOpenID`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.enum/dynamicopenid.md).
- Set [`authorizationURLKeypath`](asauthorizationproviderextensionloginconfiguration/authorizationurlkeypath.md) to the key for the authorization in the pre-authentication response. Leave [`authorizationURL`](asauthorizationproviderextensionloginconfiguration/authorizationurl.md) unset.

If you include an `authorizationRequest` dictionary in the federation pre-authentication response, Platform SSO creates a JWT OpenID request object from it and signs it with the device signing key. Platform SSO also updates the scope value to include the current scope for the request.

#### Perform the Authentication

Web-based authentication assumes that the identity provider is a nonpublic client for OAuth and uses the following flow:

![Diagram of the seven-step Platform SSO web-based authentication flow between the user, Platform SSO, and the identity provider (including its authorization endpoint).](/images/com.apple.authenticationservices/psso-web-based-auth@2x.png)

**Step 1**: The user starts the web-based authentication login flow.

**Step 2**: Platform SSO either contacts the static `authorizationURL` directly, or performs a pre-authentication HTTP GET request to [`federationUserPreauthenticationURL`](asauthorizationproviderextensionloginconfiguration/federationuserpreauthenticationurl.md) and extracts the `authorizationURL` from the key specified by the [`authorizationURLKeypath`](asauthorizationproviderextensionloginconfiguration/authorizationurlkeypath.md). If the URL fails to load, Platform SSO assumes the device is offline and uses a fallback credential.

The following is an example pre-authentication request:

```http
GET /discovery?oidcrequest&user=user@example.com HTTP/1.1
Host: auth.example.com
Connection: keep-alive
client-request-id: D546DD02-ACBD-4BA6-A48D-2BEA7CDABCDC
Accept: application/json
User-Agent: AppSSOAgent/1 CFNetwork/3887.100.1 Darwin/27.0.0
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Cache-Control: no-cache
```

The following is an example pre-authentication response:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 430
Connection: keep-alive

{
    "account_type": "Federated",
    "federation_protocol": "OIDC",
    "authorizationURL": "https://auth.example.com/authorize?state=ABCD1234&nonce=1EE6E70D-395D-4AE9-A075-F134E2F80420",
    "authorizationRequest": {
        "client_id": "52ADF3E3-DCCA-4507-BB0E-94EE5AFA643C",
        "nonce": "1EE6E70D-395D-4AE9-A075-F134E2F80420",
        "redirect_uri": "com.apple.platformsso://callback",
        "response_type": "code",
        "scope": "openid profile email",
        "state": "ABCD1234"
    }
}
```

**Step 3**: Platform SSO loads the webpage located at the `authorizationURL`. This request includes an updated scope for the current request in the web view. For more information on the available scope value, see [`Interpret Platform SSO authorization scopes`](implementing-web-based-authentication#Interpret-Platform-SSO-authorization-scopes.md).

**Step 4**: The user interacts with the web view, which can involve multiple steps that the authorization endpoint defines. Platform SSO loads only the URLs that the `WebLoginURLAllowList` key in the device management configuration permits. If authentication is successful, the authorization endpoint returns the callback URI `com.apple.platformsso://callback`, which includes an authorization code and a redirect to engage the Platform SSO extension.

When Platform SSO receives the callback URI, the web view closes.

The following is an example authorization request:

```http
POST /authorize?state=ABCD1234&nonce=1EE6E70D-395D-4AE9-A075-F134E2F80420&login_hint=user@example.com&redirect_uri=com.apple.platformsso://callback&scope=openid%20offline_access%20urn:apple:platformsso%20urn:apple:platformsso:auth:auth-prompt HTTP/1.1
Host: auth.example.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Content-Type: application/x-www-form-urlencoded
Origin: null
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)
Content-Length: 1434
Sec-Fetch-Dest: document
Accept-Language: en-US,en;q=0.9
Priority: u=0, i
Accept-Encoding: gzip, deflate, br, zstd
Connection: keep-alive

request=ewogICJraWQiJCCPb0y...5o1Slk1yxQFsmYwtg
```

The request value is:

- A signed JWT OpenID request object (base64url-encoded).
- Signed with the device signing key so the authorization endpoint can strongly identify the requesting Mac.

The following is an example JWT request object:

```json
{ 
    "kid": "fXvsEh1WFSFiXGNAUkqE38RjQwjFfEFscsWrk4YaM28=", 
    "x5c": [ "MIIBgjCCASmgA...JmggW3EQOU" ], 
    "typ": "platformsso-authorization-request+jwt", 
    "alg": "ES256" 
}.{ 
    "client_id": "52ADF3E3-DCCA-4507-BB0E-94EE5AFA643C", 
    "nonce": "1EE6E70D-395D-4AE9-A075-F134E2F80420", 
    "redirect_uri": "com.apple.platformsso://callback", 
    "scope": "openid profile email offline_access urn:apple:platformsso urn:apple:platformsso:auth:auth-prompt", 
    "state": "ABCD1234", 
    "response_type": "code" 
}.[Signature]
```

The following is an example response:

```http
HTTP/1.1 302 Found
Content-Length: 197
Location: com.apple.platformsso://callback?code=gAJZwNpLDPardp8NKwvyyJLYefxLqMQH&state=ABCD1234
Content-Type: text/html; charset=utf-8
Connection: keep-alive
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="refresh" content="0;url=com.apple.platformsso://callback?code=gAJZwNpLDPardp8NKwvyyJLYefxLqMQH&state=ABCD1234">
    </head>
    <body>
    Redirecting...
    </body>
</html>
```

When Platform SSO receives the response, it verifies that:

- The state query parameter is present, non-empty, and equal to the state value Platform SSO sent in the original request.
- The code query parameter is present and non-empty.

**Step 5**: Platform SSO uses the provided authorization code to authenticate with the identity provider. To begin the login, Platform SSO first retrieves an anti-replay value.

The following is an example anti-replay value request:

```http
POST /auth/token HTTP/1.1
Host: auth.example.com
Content-Type: application/x-www-form-urlencoded
User-Agent: AppSSOAgent/1 CFNetwork/3887.100.1 Darwin/27.0.0
client-request-id: F7263024-A625-400C-A75D-A0C011E4AAC0
Connection: keep-alive
Accept: application/json
Accept-Language: en-US,en;q=0.9
Content-Length: 24
Accept-Encoding: gzip, deflate, br
Cache-Control: no-cache

grant_type=srv_challenge
```

The following is an example anti-replay value response:

```http
HTTP/1.1 200 OK
Cache-Control: no-store, no-cache
Content-Type: application/json
Content-Length: 122
Connection: keep-alive

{"Nonce":"AwABAAAAAAADAOz_B...3AQwVsWCxHYQgAA"}
```

Using the received anti-replay value, the device sends a login request to the identity provider.

The following is an example HTTP login request:

```http
POST /auth/token HTTP/1.1
Host: auth.example.com
Content-Type: application/x-www-form-urlencoded
User-Agent: AppSSOAgent/1 CFNetwork/3887.100.1 Darwin/27.0.0
client-request-id: F7263024-A625-400C-A75D-A0C011E4AAC0
Connection: keep-alive
Accept: application/platformsso-login-response+jwt
Accept-Language: en-US,en;q=0.9
Content-Length: 2660
Accept-Encoding: gzip, deflate, br
Cache-Control: no-cache

platform_sso_version=1.0&grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=ewogICJraWQiI...Iewy1GSQOJw
```

The assertion value is a JWT login request (base64url-encoded).

Platform SSO includes the validated authorization response from step 4 as the value of the `subject_token` in the login request. The login request is a normal Platform SSO login request with three differences:

- `grant_type` is set to `urn:ietf:params:oauth:grant-type:token-exchange`.
- `subject_token` is the full absolute URL from the authorization response including the scheme and host.
- `subject_token_type` is set to `urn:apple:platformsso:authorization-code-response`.

The following is an example JWT login request:

```json
{
    "kid": "fXvsEh1WFSFiXGNAUkqE38RjQwjFfEFscsWrk4YaM28=",
    "x5c": [
        "MIIBgjCCASmgAwIBAgIBATAKBggqhkjOPQQDAjA3MRQwEgYDVQQDEwtkZXZpY2UgdGVzdDELMAkGA1UEBhMCVVMxEjAQBgNVBAoTCUFwcGxlIEluYzAeFw0yNjA2MTAxOTU5NDBaFw0yNzA2MTAxOTU5NDBaMDcxFDASBgNVBAMTC2RldmljZSB0ZXN0MQswCQYDVQQGEwJVUzESMBAGA1UEChMJQXBwbGUgSW5jMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEoPsP+ZfhDo10Ubr4qfn8e/k0U5H8dBq+YtPjohnq2qKO4n5xdvbj3Vsh+oXffe5trPqiXVAxuk5jJKBwbUO25qMmMCQwEgYDVR0TAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCB4AwCgYIKoZIzj0EAwIDRwAwRAIgdsT98cEVhh42mKc6mYYgpneTmhf4mc6EZTkXDHeOYjgCICeSlZIsg5blvS+zTSCBiekjiShL/09yanJmggW3EQOU"
    ],
    "typ": "platformsso-login-request+jwt",
    "alg": "ES256"
}.{
    "jwe_crypto": {
        "alg": "HPKE-P256-SHA256-A256GCM",
        "enc": "dir",
        "kid": "/3VgT0CYtZjhpGqeL/a1GkfrxsmgK93kPx1LkSupcaQ="
    },
    "exp": 1781124050,
    "nonce": "D9B2DD84-2C4A-4EFD-B88A-A203E0B8BA5F",
    "request_nonce": "AwABAAAAAAADAOz_B...3AQwVsWCxHYQgAA",
    "scope": "openid offline_access urn:apple:platformsso urn:apple:platformsso:auth:auth-prompt",
    "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
    "subject_token": "com.apple.platformsso://callback?code=gAJZwNpLDPardp8NKwvyyJLYefxLqMQH&state=ABCD1234",
    "iss": "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "sub": "user@example.com",
    "claims": {
        "id_token": {
            "groups": {
                "values": [
                    "com.apple.fooadmins",
                    "com.apple.baradmins",
                    "com.apple.foodatetime",
                    "com.apple.foosudo"
                ]
            }
        }
    },
    "aud": "https://auth.example.com/auth/token",
    "subject_token_type": "urn:apple:platformsso:authorization-code-response",
    "username": "user@example.com",
    "client_id": "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "iat": 1781123750
}.[Signature]
```

**Step 6**: The identity provider communicates with the authorization endpoint, which determines whether the provided authorization code is valid and whether login succeeds. In this flow, the identity provider is a nonpublic OAuth client and communication with the authorization endpoint happens out-of-band. The identity provider and its authorization endpoint define how to perform authentication.

**Step 7**: If all checks pass, the identity provider sends the Platform SSO login response back to the device, including the access token, ID token, and refresh token.

Platform SSO processes and validates the login response the same way as other login requests. It then uses the Platform SSO 2.0 key service to unlock the user’s keybag and complete the login or unlock flow. Platform SSO always uses the key service during web-based authentication.

#### Interpret Platform Sso Authorization Scopes

When Platform SSO requests OpenID tokens from your identity provider, it includes one of the scopes below in the authorization request. The scope tells your identity provider why the user is authenticating, so you can apply the correct policy (for example, require multifactor authentication at login but not at screen unlock).

All scope values use the prefix `urn:apple:platformsso:auth:`:

| Scope | Usage |
| --- | --- |
| `elevation` | Platform SSO prompts the user to re-authenticate to elevate privileges (administrator authorization prompt). |
| `refresh` | A silent token refresh with no user interaction. If refresh fails and falls back to a real login, the scope reverts to the originating caller’s scope (for example, `auth-prompt`). |
| `auth-prompt` | An in-session authentication prompt; for example, background re-authentication at session start, after a network change, or on a token-refresh timer. |
| `create-user` | Platform SSO creates a new local account at the login window using credentials from the identity provider. |
| `fallback` | Fallback uses OpenID because the primary credential (for example, Touch ID) isn’t usable. Platform SSO sends this scope on both the authorization request and the corresponding token verification. |
| `login` | The user logs in at the login window or unlocks FileVault. Also the default scope when no other context applies. |
| `password-change` | The user is in the password-change flow. |
| `setup-assistant` | Setup Assistant drives this authentication during initial device setup, including embedded system-session authentication that isn’t an elevation prompt. |
| `temporary-session` | Authentication for an Authenticated Guest Mode session. |
| `unlock` | The user unlocks their Mac from the screen-locked state (already logged in). |

> **Note**: Platform SSO adds exactly one of these scopes to your authorization URL per request. The scopes are mutually exclusive with respect to the originating user action.

For most session-driven flows, Platform SSO selects the scope purely from the session type:

| Session type | Resulting scope |
| --- | --- |
| Elevation prompt | `elevation` |
| In-session prompt | `auth-prompt` |
| Login window, or FileVault unlock | `login` |
| Password change | `password-change` |
| Setup Assistant | `setup-assistant` |
| Screen unlock | `unlock` |

A few scopes fall outside the session-type mapping:

- Platform SSO applies the special-purpose scopes (`create-user`, `temporary-session`, `fallback`, `refresh`) based on the specific feature path instead of the session type.
- When no specific context is available, `login` doubles as the default. Treat it as the safe baseline and reserve stricter policy for the more specific scopes.
- For fallback, Platform SSO sends the same scope on both legs of the OpenID handshake (the initial authorization request and the subsequent token verification), so your identity provider can apply policy decisions consistently across both.

#### Sync the Password

Optionally, you can sync the password the user enters during web-based authentication to the local user account. Use this option when the device management configuration sets the `AllowWebLoginPasswordSync` key to `true`. This requires the identity provider to embed a JavaScript snippet (like the following conceptual example) in the authorization endpoint login page:

```javascript
<script>
    function syncPasswordWithPlatformSSO() {
        // 1. Check for the Platform SSO API.
        if (!window.apple?.platformSSO) {
            // Platform SSO not available; no action required
            // because password sync is a supplementary feature.
            return;
        }
        // 2. Get the password from your sign-in form.
        const password = document.getElementById('password').value;
        // 3. Send the password to Platform SSO for local account sync.
        if (window.apple.platformSSO.syncPassword) {
            window.apple.platformSSO.syncPassword(password);
        }
    }
    // Call from your form's submit handler.
    document.getElementById('signinForm').addEventListener('submit', function() {
        syncPasswordWithPlatformSSO();
        // Form submission continues normally.
    });
</script>
```

#### Support Qr Code Authentication

QR code scanning is a supplementary feature that the authorization endpoint’s webpage initiates during web-based authentication. The sign-in page calls a JavaScript API injected into the web view, which opens an attached camera for QR code scanning. The JavaScript caller receives the scanned data and stores it for inclusion in the OAuth credential submission.

To add QR code scanning to your login page, use a JavaScript snippet like the following conceptual example:

```javascript
<script>
    async function authenticateWithQR() {
        // 1. Check for the Platform SSO API.
        if (!window.apple?.platformSSO) {
            // Fallback: Show a manual entry field.
            showManualCodeEntry();
            return;
        }

        try {
            // 2. Call the built-in QR scanner.
            const scannedData = await window.apple.platformSSO.scanQR();

            // 3. Use scanned data in your authentication flow
            // for example, submit as a one-time code, 
            // TOTP seed, or device binding token.
            await submitQRCodeToServer(scannedData);

        } catch (error) {
            // 4. Handle any cancellation or failure.
            if (error.message === "cancelled") {
                // User canceled the scan.
            } else {
                // Scanner error (camera unavailable, 
                // timeout, and so on).
            }
        }
    }
</script>
```

The `scanQR()` function resolves with:

- The QR code payload as a UTF-8 encoded string.
- The QR code content determines the format of the string (for example, a URL or token).

The `scanQR()` function rejects with an Error where `error.message` is one of:

- `cancelled`: The user dismissed the scanner.
- `error`: An internal error prevents the scan (for example, a camera session or scanner configuration failure).
- `invalid`: The scan didn’t return a valid QR code. Retry the scan.
- `timeout`: The scan exceeded the system time limit.
- `unavailable`: No camera is available.

## See Also

- [Authentication process](authentication-process.md)
  Use a system-supported method to authenticate with an identity provider.
- [Using access keys with Platform Single Sign-on](using-access-keys-with-platform-single-sign-on.md)
  Authenticate users with access keys stored in Apple Wallet.
- [class ASAuthorizationProviderExtensionKerberosMapping](asauthorizationproviderextensionkerberosmapping.md)
  A set of Kerberos mappings that the system login process uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/implementing-web-based-authentication)*