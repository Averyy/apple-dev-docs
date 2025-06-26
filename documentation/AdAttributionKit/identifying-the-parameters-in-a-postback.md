# Identifying the parameters in a postback

**Framework**: AdAttributionKit

Interpret postback properties to understand the attribution report.

#### Overview

The lists in this article describe all the possible parameters you can get in a postback. To verify that Apple signed the postback, see [`Verifying a postback`](verifying-a-postback.md).

#### Understand the Json Stanza the Framework Sends

The JSON stanza your servers receive resembles the following:

```json
{
  "jws-string": "eyJraWQiOiJhcHBsZS1kZXZlbG9wbWVudC1pZGVudGlmaWVyXC8xIiwiYWxnIjoiRVMyNTYifQ.eyJwb3N0YmFjay1pZGVudGlmaWVyIjoiODU1NDZFQjctRkQzOS00NEJDLTg5OTAtQzk4QTRBQzM2QTQ5IiwicHVibGlzaGVyLWl0ZW0taWRlbnRpZmllciI6MCwibWFya2V0cGxhY2UtaWRlbnRpZmllciI6ImNvbS5hcHBsZS5BcHBTdG9yZSIsImltcHJlc3Npb24tdHlwZSI6ImFwcC1pbXByZXNzaW9uIiwiYWQtbmV0d29yay1pZGVudGlmaWVyIjoiZGV2ZWxvcG1lbnQuYWRhdHRyaWJ1dGlvbmtpdCIsImRpZC13aW4iOnRydWUsInBvc3RiYWNrLXNlcXVlbmNlLWluZGV4IjowLCJjb252ZXJzaW9uLXR5cGUiOiJyZS1lbmdhZ2VtZW50Iiwic291cmNlLWlkZW50aWZpZXIiOiIxMjM0IiwiYWR2ZXJ0aXNlZC1pdGVtLWlkZW50aWZpZXIiOjEwNzM4MDI3NzU2fQ.bAdNwKd6OfHK9tofvjjua4X_JPcFTxXPQSspD9gZkinw97pY7R1aI-LSjl-oxZZF3_K2H5JK5TSEBee4_1U4oQ",
  "conversion-value": 24,
  "ad-interaction-type": "click",
  "country-code": "US"
}
```

The keys in this stanza may include:

#### Examine the Jws Header for the Encryption Algorithm and Key Identifier

The JWS header of the postback consists of two parameters and resembles the following structure:

```json
{
  "kid": "apple-development-identifier/1",
  "alg": "ES256"
}
```

The keys for this structure are:

#### Examine the Jws Payload of the Postback

The JWS decoded payload of the postback resembles the following structure:

```json
{
  "postback-identifier": "85546EB7-FD39-44BC-8990-C98A4AC36A49",
  "publisher-item-identifier": 0,
  "marketplace-identifier": "com.apple.AppStore",
  "impression-type": "app-impression",
  "ad-network-identifier": "development.adattributionkit",
  "did-win": true,
  "postback-sequence-index": 0,
  "conversion-type": "re-engagement",
  "source-identifier": "1234",
  "advertised-item-identifier": 10738027756
}
```

The keys the framework delivers in this structure may include the following:

#### Examine the Postbacks Jws Signature

The signature is a combination of the JSON Web Signature (JWS) header and payload components that Apple signs using its private key.

For more information about verifying the postback’s signature, see [`Verifying a postback`](verifying-a-postback.md). For more information about receiving postbacks, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

#### Understand the Crowd Anonymity Controlled Properties

To help ensure crowd anonymity, Apple assigns a postback data tier to app downloads. The postback data tier determines whether certain parameters appear in the postback, as well as the number of digits in the hierarchical source identifier. The following postback parameters are subject to the postback data tier:

- `coarse-conversion-value`
- `conversion-value`
- `source-identifier` (affects the number of digits the postback returns)
- `publisher-item-identifier`
- `marketplace-identifier`
- `country-code`

## See Also

- [Verifying a postback](verifying-a-postback.md)
  Ensure the validity of a postback you receive after an ad conversion by verifying its cryptographic signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/identifying-the-parameters-in-a-postback)*