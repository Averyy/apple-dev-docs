# Generating JSON Web Tokens for API requests

**Framework**: App Store Server API

Create JSON Web Tokens signed with your private key to authorize requests for App Store Server API and External Purchase Server API.

#### Overview

JSON Web Token (JWT) is an open standard ([`RFC 7519`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519)) that defines a way to securely transmit information. The [`App Store Server API`](AppStoreServerAPI.md) and [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI) require a JWT to authorize each request you make to the API. You create the token, signing it with the private key you downloaded from App Store Connect. For more information about creating keys, see [`Creating API keys to authorize API requests`](creating-api-keys-to-authorize-api-requests.md).

To generate a signed JWT:

1. Create the JWT header.
2. Create the JWT payload.
3. Sign the JWT.

Include the signed JWT in the authorization header of each API request. Generate a new signed JWT for each new request.

> 💡 **Tip**:  The App Store Server Library provides an API client and creates JWTs for use with the [`App Store Server API`](AppStoreServerAPI.md). For more information, see [`Simplifying your implementation by using the App Store Server Library`](simplifying-your-implementation-by-using-the-app-store-server-library.md).

 The App Store Server Library provides an API client and creates JWTs for use with the [`App Store Server API`](AppStoreServerAPI.md). For more information, see [`Simplifying your implementation by using the App Store Server Library`](simplifying-your-implementation-by-using-the-app-store-server-library.md).

##### Create the Jwt Header

To create a JWT to communicate with the [`App Store Server API`](AppStoreServerAPI.md) or [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI), use the following fields and values in the header:

| Header Field | Value |
| --- | --- |
| `alg` - Encryption Algorithm | `ES256`  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) All JWTs must be signed with ES256 encryption |
| `kid` - Key ID | Your private key ID from App Store Connect (Ex: `2X9R4HXF34`) |
| `typ` - Token Type | `JWT` |

To get your key ID, copy it from App Store Connect by logging in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/), then:

1. Select Users and Access, then select the Keys tab.
2. The key IDs appear in a column under the Active heading. Hover the cursor next to a key ID to display the Copy Key ID link.
3. Click Copy Key ID.

If you have more than one API key, copy the key ID of the private key that you use to sign the JWT.

Here’s an example of a JWT header:

```javascript
{
  "alg": "ES256",
  "kid": "2X9R4HXF34",
  "typ": "JWT"
}
```

##### Create the Jwt Payload

The JWT payload contains information specific to the [`App Store Server API`](AppStoreServerAPI.md) and [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI), such as issuer ID and expiration time. Use the following fields — also known as JWT claims — to include these values in the JWT payload:

|  |  |
| --- | --- |
| `iss` - Issuer | Your issuer ID from the Keys page in App Store Connect (Ex: “`57246542-96fe-1a63-e053-0824d011072a"`) |
| `iat` - Issued At | The time at which you issue the token, in UNIX time, in seconds (Ex: `1623085200`) |
| `exp` - Expiration Time | The token’s expiration time, in UNIX time, in seconds. Tokens that expire more than 60 minutes after the time in `iat` are not valid (Ex: `1623086400`) |
| `aud` - Audience | `appstoreconnect-v1` |
| `bid` - Bundle ID | Your app’s bundle ID (Ex: `“com.example.testbundleid”)` |

To get your issuer ID, log in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/), then:

1. Select Users and Access, then select the Keys tab.
2. The issuer ID appears near the top of the page. To copy the issuer ID, click Copy next to the ID.

Here’s an example of a JWT payload:

```javascript
{
  "iss": "57246542-96fe-1a63e053-0824d011072a",
  "iat": 1623085200,
  "exp": 1623086400,
  "aud": "appstoreconnect-v1",
  "bid": "com.example.testbundleid"
}
```

Note that the JWT is valid for up to one hour after the time you indicate in the `iat` field, or it expires sooner if you set the `exp` field for an earlier time.

##### Sign the Jwt

Use the private key associated with the key ID you specified in the header to sign the token using ES256 encryption.

There are a variety of open source libraries available online for creating and signing JWT tokens. See [`JWT.io`](https://developer.apple.comhttps://jwt.io/) for more information.  For calls to the [`App Store Server API`](AppStoreServerAPI.md), consider using the App Store Server Library to create the JWTs instead. For more information, see [`Simplifying your implementation by using the App Store Server Library`](simplifying-your-implementation-by-using-the-app-store-server-library.md).

##### Include the Jwt in the Authorization Header of the Request

After you create and sign the JWT, provide it in the request’s authorization header as a bearer token.

The following example for the [`App Store Server API`](AppStoreServerAPI.md) shows a `curl` command using a bearer token. Replace the text `[signed token]` with the value of the signed JWT itself. Replace `{transactionId}` with a transaction identifier of your customer.

```other
curl -v -H 'Authorization: Bearer [signed token]' 
"https://api.storekit.itunes.apple.com/inApps/v1/subscriptions/{transactionId}"
```

## See Also

- [Simplifying your implementation by using the App Store Server Library](simplifying-your-implementation-by-using-the-app-store-server-library.md)
  Use Apple’s open source library to create JSON Web Tokens (JWT) to authorize your calls, verify transactions, extract transaction identifiers from receipts, and more.
- [Creating API keys to authorize API requests](creating-api-keys-to-authorize-api-requests.md)
  Create API keys you use to sign JSON Web Tokens and authorize API requests.
- [Identifying rate limits](identifying-rate-limits.md)
  Recognize the rate limits that apply to App Store Server API endpoints and handle them in your code.
- [App Store Server API changelog](app-store-server-api-changelog.md)
  Learn about new features and updates in the App Store Server API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/generating-json-web-tokens-for-api-requests)*