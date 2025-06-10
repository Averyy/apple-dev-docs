# Generating developer tokens

**Framework**: Apple Music Feed

Create a JSON Web Token to authorize your requests to Apple Media Feed API.

#### Overview

The header of each Apple Media Feed API request requires authorization in the form of a developer token. A developer token is a signed token that authenticates you as a trusted developer and member of the Apple Developer Program.

Apple Media Feed API limits the number of requests you can make using a developer token within a specific period of time. If you exceed this limit, you temporarily receive `429 Too Many Requests` error responses for requests that use the token. This error resolves itself shortly after the request rate reduces.

#### Create Your Developer Token

[`Configuring a media identifier and authorization key`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-service-configurations/apple-music-feed) using your developer account allows you to obtain a key ID to use in your developer token.

Apple Media Feed API supports the JSON Web Token (JWT) specification, so you can pass statements and metadata called . For more information, see the [`JWT specification`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519) and the available libraries for generating signed JWTs.

Create a developer token as a JSON object with a header that includes the following:

> ❗ **Important**: Apple Media Feed API supports only developer tokens signed with the ES256 algorithm. Unsecured developer tokens or developer tokens signed with other algorithms reject with a `401` error code.

In the claims payload of the token, include the following:

> 💡 **Tip**: To locate your Team ID, sign in to your developer account, and click “Membership details” at the top of the page.

A decoded developer token has the following format:

```None
{
     "alg": "ES256",
     "kid": "ABC123DEFG"
}
{
     "iss": "DEF123GHIJ",
     "iat": 1437179036,
     "exp": 1493298100
}
```

After you create the token, sign it with your private key using the ES256 algorithm.

> **Note**: ES256 is the [`JSON Web Algorithms (JWA)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7518) name for the Elliptic Curve Digital Signature Algorithm (ECDSA) with the P-256 curve and the SHA-256 hash.

#### Authorize Requests

If you manage request authorization directly, in all requests, pass the `Authorization: Bearer` header set to the developer token.

```None
curl -v -H 'Authorization: Bearer [developer token]' "https://api.ent.apple.com/v1/test"
```

## See Also

- [Requesting a feed export](requesting-a-feed-export.md)
  Create requests for Apple Music Catalog metadata.
- [Interpreting responses](interpreting-responses.md)
  Learn about responses from Apple Media Feed API to your Apple Music Feed requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/generating-developer-tokens)*