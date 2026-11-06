# VerifiableCredentialRegistration

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A type used for registering SD-JWT verifiable credentials.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
struct VerifiableCredentialRegistration
```

## Overview

SD-JWT verifiable credentials are a credential format defined in IETF SD-JWT VC.

## Topics

### Creating a registration
- [init(verifiableCredentialTypes: [String], supportedIssuerKeyIdentifiers: [Data], supportedAuthorityKeyIdentifiers: [Data], documentIdentifier: String, invalidationDate: Date?)](./verifiablecredentialregistration/init%28verifiablecredentialtypes,supportedissuerkeyidentifiers,supportedauthoritykeyidentifiers,documentidentifier,invalidationdate%29.md)
  Initializes a verifiable credential registration.
### Inspecting a registration
- [var verifiableCredentialTypes: [String]](./verifiablecredentialregistration/verifiablecredentialtypes.md)
  The verifiable credential types that the registered credential can satisfy.
- [var supportedIssuerKeyIdentifiers: [Data]](./verifiablecredentialregistration/supportedissuerkeyidentifiers.md)
  A list of X.509 authority key identifiers that correspond to the issuer certificate chain for the verifiable credential.
- [var supportedAuthorityKeyIdentifiers: [Data]](./verifiablecredentialregistration/supportedauthoritykeyidentifiers.md)
  A list of authority key identifiers that correspond to relying party authorizers that your app trusts.
- [var invalidationDate: Date?](./verifiablecredentialregistration/invalidationdate.md)
  A date that indicates when the registration should be invalidated.

## Relationships

### Conforms To
- [IdentityDocumentRegistration](./identitydocumentregistration.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Registering as an identity document provider
- [actor IdentityDocumentProviderRegistrationStore](./identitydocumentproviderregistrationstore.md)
  A store that notifies the system which documents an app has available for presentment.
- [protocol IdentityDocumentRegistration](./identitydocumentregistration.md)
  A protocol that defines an identity document registration.
- [struct MobileDocumentRegistration](./mobiledocumentregistration.md)
  A type you use to register mobile documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/verifiablecredentialregistration)*