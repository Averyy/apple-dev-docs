# credentialIdentities(forService:credentialIdentityTypes:)

**Framework**: Authentication Services  
**Kind**: method

Retrieves an array of all previously saved credential identities in the store for your extension.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- visionOS 1.1+

## Declaration

```swift
func credentialIdentities(forService serviceIdentifier: ASCredentialServiceIdentifier? = nil, credentialIdentityTypes: ASCredentialIdentityStore.IdentityTypes = []) async -> [any ASCredentialIdentity]
```

#### Return Value

An array of previously saved credential identities that match the identifier and identity type criteria.

## Parameters

- `serviceIdentifier`: An   that limits results to only that service. Pass   to get credential identities for all services. Defaults to  .
- `credentialIdentityTypes`: An array of   that limits results to only those types. Pass   to get credential identities for all types. Defaults to  .

## See Also

- [class ASCredentialServiceIdentifier](ascredentialserviceidentifier.md)
  An identifier representing a particular service for which the user needs a credential, like a web site.
- [ASCredentialIdentityStore.IdentityTypes](ascredentialidentitystore/identitytypes.md)
  The defined identity types for use in retrieving credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/credentialidentities(forservice:credentialidentitytypes:))*