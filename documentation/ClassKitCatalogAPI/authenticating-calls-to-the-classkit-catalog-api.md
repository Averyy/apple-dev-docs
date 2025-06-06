# Authenticating Calls to the ClassKit Catalog API

**Framework**: ClassKit Catalog API

Establish your identity to the ClassKit Catalog server by providing a cryptographically signed token for each call.

#### Overview

You authenticate the calls you make to the ClassKit Catalog API by including a cryptographically signed [`JSON Web Token (JWT)`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519). You sign the JWT using a private key that you provision in [`Apple Developer`](https://developer.apple.comhttps://developer.apple.com) website, and then include the signed token as part of the header of each call that you make.

##### Register a Private Key

Sign in to the Apple Developer web site, and navigate to the “Certificates, IDs, & Profiles” page. Choose Keys in the sidebar, and then click the plus (+) button to add a new key. Name the key, and enable it for use with ClassKit Catalog. Complete the registration and download the private key.

![Screenshot of the Apple Developer website showing the form for adding a new cryptographic key.](https://docs-assets.developer.apple.com/published/ff35702215033cc574b718cdd5d24a2d/media-3675465%402x.png)

You can download the private key only once. Apple doesn’t keep a copy of your key, so you can’t retrieve the key again. If you lose your key, you’ll need to revoke the key and create a new one. Similarly, if your private key is ever compromised, you’ll need to revoke the original key and create a new one.

##### Create and Sign a Token

Compose a JWT as a combination of a header, a claim set, and a signature, as described in the [`JSON Web Token (JWT)`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519) specification. Create the header as a JSON object with key-value pairs representing:

- The key identifier, given by the `kid` key. Provide the key identifier reported to you by the Apple Developer site after provisioning the key.
- The type of token, given by the `typ` key. Provide a value of `JWT` to indicated a JSON web token.
- The algorithm used to sign the token, given by the `alg` key. Set the value to `ES256` to indicate the Elliptic Curve Digital Signature Algorithm (ECDSA) algorithm with the P-256 curve and SHA-256 hash algorithm.

An example header looks like this:

```json
{
  "kid": "9QVIE72P19",
  "typ": "JWT",
  "alg": "ES256"
}
```

Create a claim set as another JSON object with key-value pairs representing:

- The issuer claim that identifies you as the issuer of the JWT, given by the `iss` key. Provide your Apple Developer account team identifier as the value.
- The issued-at claim that indicates when you created the JWT, given by the `iat` key. Indicate the number of seconds after the Unix epoch when you created the token.
- The expiration-time claim that indicates a time after which the JWT is no longer valid, given by the `exp` key. Indicate the number of seconds after the Unix epoch when the token should expire, which is typically 10 to 30 minutes after creation.

An example claim set looks like this:

```json
{
  "iss": "4J2MBDPZ6M",
  "iat": 1587058400,
  "exp": 1587060200
}
```

Base-64 encode and compute a signature over these two objects, as described in the JWT specification, using your private key with the P-256 ECDSA algorithm and a SHA-256 hash. The two encoded objects plus the computed signature, separated by periods, make up the JWT.

##### Authenticate Requests with the Signed Token

Include the JWT with every request you make to the ClassKit Catalog API by adding `Authorization: Bearer <JWT>` to the header, where you replace <`JWT>` with your actual token. Here is an example of making a request using the `curl` command line utility:

```shell
% curl -v -H "Authorization: Bearer <JWT>" "https://classkit-catalog.apple.com/v1/contexts?identifierPath=%5B%22com.apple.www.Quizzer%22%5D&environment=production&locale=en-us"
```

## See Also

- [Testing Your ClassKit Catalog Implementation](testing-your-classkit-catalog-implementation.md)
  Verify your server interaction before deployment by operating in a development environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/authenticating-calls-to-the-classkit-catalog-api)*