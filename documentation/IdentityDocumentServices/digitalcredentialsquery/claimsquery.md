# DigitalCredentialsQuery.ClaimsQuery

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A request for a single claim.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct ClaimsQuery
```

## Topics

### Creating a claims query
- [init(id: String?, path: DigitalCredentialsQuery.ClaimsQuery.ClaimPath, values: [DigitalCredentialsQuery.ClaimsQuery.AcceptedValue], intentToRetain: Bool?)](./claimsquery/init%28id,path,values,intenttoretain%29.md)
  Initializes a claims query.
### Inspecting a claims query
- [var id: String?](./claimsquery/id.md)
  Identifies a claim within the credential query.
- [var path: DigitalCredentialsQuery.ClaimsQuery.ClaimPath](./claimsquery/path.md)
  The path to the claim within the credential.
- [var values: [DigitalCredentialsQuery.ClaimsQuery.AcceptedValue]](./claimsquery/values.md)
  The values the relying party accepts for the claim.
- [var intentToRetain: Bool?](./claimsquery/intenttoretain.md)
  A Boolean value that indicates whether the relying party intends to retain the claim.
### Describing a claim
- [DigitalCredentialsQuery.ClaimsQuery.ClaimPath](./claimsquery/claimpath.md)
  A path that identifies one or more claims within a credential.
- [DigitalCredentialsQuery.ClaimsQuery.PathComponent](./claimsquery/pathcomponent.md)
  A single step in a claims path.
- [DigitalCredentialsQuery.ClaimsQuery.AcceptedValue](./claimsquery/acceptedvalue.md)
  A value that a relying party accepts for a claim.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/claimsquery)*