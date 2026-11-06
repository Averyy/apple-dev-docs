# DigitalCredentialsQuery

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A request that describes the credentials and claims a relying party wants from a person’s digital ID.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct DigitalCredentialsQuery
```

## Discussion

A Digital Credentials Query Language (DCQL) query describes the credentials that a relying party requests from a person’s digital ID, and the specific pieces of information in them, called *claims*. A claim is one piece of information in a credential, such as a birth date or a family name. A *relying party* is the website, app, or service that asks to see that information and then relies on it to make a decision, such as confirming a person’s age or identity. The relying party builds the query and sends it in a request. The system passes the query to your app, which reads it to find matching credentials and show the person what the relying party requests.

The relying party sends the query in an [`OpenID4VPRequest`](./openid4vprequest.md) and the request exposes it through [`query`](./openid4vprequest/query.md).

A query contains one or more credential requests, each described by a [`DigitalCredentialsQuery.CredentialQuery`](./digitalcredentialsquery/credentialquery.md). Each credential request identifies the credential’s [`DigitalCredentialsQuery.CredentialFormat`](./digitalcredentialsquery/credentialformat.md), optional format-specific constraints in [`DigitalCredentialsQuery.Metadata`](./digitalcredentialsquery/metadata.md), and the claims the relying party wants, each described by a [`DigitalCredentialsQuery.ClaimsQuery`](./digitalcredentialsquery/claimsquery.md). A credential request can also list the issuer authorities and trust frameworks the relying party accepts, using [`DigitalCredentialsQuery.TrustedAuthoritiesQuery`](./digitalcredentialsquery/trustedauthoritiesquery.md).

A query can also include [`DigitalCredentialsQuery.CredentialSetQuery`](./digitalcredentialsquery/credentialsetquery.md) values, which group credential requests by their identifiers. Each credential set lists options, and any one option satisfies the set. A credential set is either required or optional.

## Topics

### Creating a query
- [init(credentials: [DigitalCredentialsQuery.CredentialQuery], credentialSets: [DigitalCredentialsQuery.CredentialSetQuery])](./digitalcredentialsquery/init%28credentials,credentialsets%29.md)
  Initializes a query.
### Inspecting a query
- [var credentials: [DigitalCredentialsQuery.CredentialQuery]](./digitalcredentialsquery/credentials.md)
  The credentials requested.
- [var credentialSets: [DigitalCredentialsQuery.CredentialSetQuery]](./digitalcredentialsquery/credentialsets.md)
  Groupings of credentials that satisfy the query.
### Describing credentials
- [DigitalCredentialsQuery.CredentialQuery](./digitalcredentialsquery/credentialquery.md)
  A request for a single credential.
- [DigitalCredentialsQuery.CredentialFormat](./digitalcredentialsquery/credentialformat.md)
  The format of a requested credential.
- [DigitalCredentialsQuery.Metadata](./digitalcredentialsquery/metadata.md)
  Format-specific constraints on a requested credential.
- [DigitalCredentialsQuery.CredentialSetQuery](./digitalcredentialsquery/credentialsetquery.md)
  A grouping of credentials that satisfies part of a query.
### Describing claims
- [DigitalCredentialsQuery.ClaimsQuery](./digitalcredentialsquery/claimsquery.md)
  A request for a single claim.
### Describing trusted issuers
- [DigitalCredentialsQuery.TrustedAuthoritiesQuery](./digitalcredentialsquery/trustedauthoritiesquery.md)
  An issuer authority or trust framework that a relying party accepts.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Requesting credentials with OpenID4VP
- [struct OpenID4VPRequest](./openid4vprequest.md)
  A type that represents an incoming OpenID for Verifiable Presentations request.
- [struct OpenID4VPResponse](./openid4vpresponse.md)
  A response to an OpenID4VP request.
- [enum OpenID4VPExchangeProtocolIdentifier](./openid4vpexchangeprotocolidentifier.md)
  A value that identifies which OpenID4VP exchange protocol a request or response uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery)*