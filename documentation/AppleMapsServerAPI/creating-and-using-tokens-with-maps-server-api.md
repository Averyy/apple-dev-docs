# Creating and using tokens with Maps Server API

**Framework**: Apple Maps Server API

Sign JSON Web Tokens to use Maps Server API and debug common signing errors.

#### Overview

Maps Server API uses a Maps token to authenticate map initializations and other API requests, such as requests to retrieve directions or execute a search. To use a Maps token with Maps Server API you must have an Apple Developer account and obtain a Maps ID and a private key as described in [`Creating a Maps identifier and a private key`](creating-a-maps-identifier-and-a-private-key.md).

After getting or creating a token, confirm the success of the token authorization by using the token to access the API; check the status codes that the API responses return to verify the calls were successful.

#### Create a Token to Use Maps Server Api

Maps Server API requires a Maps token to initialize MapKit. A Maps token has two sections, a header and a payload. The header describes the token and the cryptographic operations applied to the payload. The payload contains a set of cryptographically signed claims.

Construct a token with these required fields in the header:

- **`alg`**: The algorithm you use to sign the token. Use the `ES256` algorithm to sign your token.
- **`kid`**: A 10-character key identifier that provides the ID of the private key that you obtain from your Apple Developer account.
- **`typ`**: A type parameter that you set to `"JWT"`.

In the payload section of the token, include the following claims:

- **`iss`**: The issuer of the token. This is a 10-character Team ID obtained from your Apple Developer account.
- **`iat`**: The “Issued At” registered claim key. The value of this claim indicates the token creation time, in terms of the number of seconds since UNIX Epoch, in UTC.
- **`exp`**: The “Expiration Time” registered claim key. The value of this claim indicates when the token expires, in terms of the number of seconds since the UNIX Epoch, in UTC.
- **`scope`**: A space-separated list of one or more Apple Maps frameworks you are authorizing the token to use. To use Maps Server API, set the value to `"server_api"`. See [`Available token scopes`](creating-and-using-tokens-with-maps-server-api#Available-token-scopes.md) for scope values of other Apple Maps frameworks.
- **`origin`**: Specifies the origins allowed when you make requests from a web browser. Use a domain pattern such as `*.example.com`, a specific domain such as `example.com`, or a comma-separated list of origins for multiple domains such as `example.com,*.subdomain.com`. The token requires an origin when the scope includes `mapkit_js`, `web_snapshots`, or `embed_api`.

To locate your Team ID, sign in to your [`Apple Developer account`](https://developer.apple.comhttps://developer.apple.com/account), and click Membership in the sidebar. Your Team ID appears in the Membership information section under the team name. Generate your token by signing it with your private key.

> **Note**: As a security best practice, consider creating separate tokens for each product scope. Using tokens with a single scope helps limit exposure when a token is compromised.

When decoded, a token for use with Maps Server API has the following format:

```other
{
    "alg": "ES256",
    "kid": "ABC123DEFG",
    "typ": "JWT"
}
{
    "iss": "DEF123GHIJ",
    "iat": 1437179036,
    "exp": 1493298100,
    "scope": "server_api",
    "origin": "*.example.com"
}
```

To learn more about Maps tokens, see the [`JSON Web Token (JWT) specification`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519). You can find a collection of libraries for generating signed tokens at [`JWT.io`](https://developer.apple.comhttps://jwt.io).

For next steps, go to [`Generate a Maps token`](-v1-token.md).

#### Available Token Scopes

The `scope` claim sets one or more Apple Maps frameworks you are authorizing the token to use. Available values are:

- **`embed_api`**: [`Maps Embed API`](https://developer.apple.comhttps://developer.apple.com/documentation/mapkitjs/displaying-place-information-using-the-maps-embed-api)
- **`mapkit_js`**: [`MapKit JS`](https://developer.apple.comhttps://developer.apple.com/documentation/mapkitjs/)
- **`server_api`**: Maps Server API
- **`web_snapshots`**: [`Maps Web Snapshots`](https://developer.apple.comhttps://developer.apple.com/documentation/snapshots/)

Instead of signing a token dynamically, you can use a static token when using any Apple Maps frameworks other than Maps Server API. See [`Creating a Maps token`](https://developer.apple.comhttps://developer.apple.com/documentation/MapKitJS/creating-a-maps-token).

## See Also

- [Creating a Maps identifier and a private key](creating-a-maps-identifier-and-a-private-key.md)
  Create a Maps identifier and a private key before generating tokens for MapKit JS.
- [Generate a Maps token](-v1-token.md)
  Returns a JWT maps access token that you use to call the service API.
- [Debugging an Invalid token](debugging-an-invalid-token.md)
  Inspect the JavaScript console logs, the token, and events to determine why a token is invalid.
- [Common objects](common-objects.md)
  Understand the common JSON objects that API responses contain.
- [Integrating the Apple Maps Server API into Java server applications](integrating-the-apple-maps-server-api-into-java-server-applications.md)
  Streamline your app’s API by moving georelated searches from inside your app to your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api)*