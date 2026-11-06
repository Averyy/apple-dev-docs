# DigitalCredentialsQuery.ClaimsQuery.PathComponent

**Framework**: IdentityDocumentServices  
**Kind**: enum  
**Role**: Enumeration

A single step in a claims path.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
enum PathComponent
```

## Topics

### Enumeration Cases
- [DigitalCredentialsQuery.ClaimsQuery.PathComponent.allArrayElements](./pathcomponent/allarrayelements.md)
  Selects every element of an array.
- [DigitalCredentialsQuery.ClaimsQuery.PathComponent.arrayElement(index:)](./pathcomponent/arrayelement%28index%29.md)
  Selects the index of an array.
- [DigitalCredentialsQuery.ClaimsQuery.PathComponent.key(_:)](./pathcomponent/key%28_%29.md)
  Selects the key of an object.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Describing a claim
- [DigitalCredentialsQuery.ClaimsQuery.ClaimPath](./claimpath.md)
  A path that identifies one or more claims within a credential.
- [DigitalCredentialsQuery.ClaimsQuery.AcceptedValue](./acceptedvalue.md)
  A value that a relying party accepts for a claim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/claimsquery/pathcomponent)*