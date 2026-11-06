# DigitalCredentialsQuery.ClaimsQuery.ClaimPath

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A path that identifies one or more claims within a credential.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct ClaimPath
```

## Discussion

A credential stores its claims in a nested structure, so a name such as `city` isn’t enough to say which claim you mean. A claim path describes where the claim is by listing the steps to reach it, starting at the top level of the credential. Each step is a [`DigitalCredentialsQuery.ClaimsQuery.PathComponent`](./pathcomponent.md):

- [`DigitalCredentialsQuery.ClaimsQuery.PathComponent.key(_:)`](./pathcomponent/key%28_%29.md) selects a key of an object.
- [`DigitalCredentialsQuery.ClaimsQuery.PathComponent.arrayElement(index:)`](./pathcomponent/arrayelement%28index%29.md) selects the element at an index of an array.
- [`DigitalCredentialsQuery.ClaimsQuery.PathComponent.allArrayElements`](./pathcomponent/allarrayelements.md) selects every element of an array.

You pass a claim path to [`DigitalCredentialsQuery.ClaimsQuery`](../claimsquery.md) to say which claim a request asks for. For example, a credential that contains the following data has a `city` claim inside an `address` object, and a `driving_privileges` array that contains one object for each vehicle category the person can drive:

```json
{
  "address": { "city": "Cupertino" },
  "driving_privileges": [
    { "vehicle_category_code": "B", "expiry_date": "2030-05-01" },
    { "vehicle_category_code": "A", "expiry_date": "2028-09-15" }
  ]
}
```

To request the city, create a path that selects `address` and then `city`, and use it in a claims query:

```swift
let cityPath = DigitalCredentialsQuery.ClaimsQuery.ClaimPath([
    .key("address"),
    .key("city")
])

let cityClaim = DigitalCredentialsQuery.ClaimsQuery(path: cityPath)
```

To request the expiration date of only the first driving privilege, select the `driving_privileges` array, then the element at index `0`, and then the `expiry_date` key:

```swift
let firstExpiryPath = DigitalCredentialsQuery.ClaimsQuery.ClaimPath([
    .key("driving_privileges"),
    .arrayElement(index: 0),
    .key("expiry_date")
])
```

To request the vehicle category code of every driving privilege, replace the second step with `.allArrayElements`:

```swift
let allCategoriesPath = DigitalCredentialsQuery.ClaimsQuery.ClaimPath([
    .key("driving_privileges"),
    .allArrayElements,
    .key("vehicle_category_code")
])
```

Since a path can select more than one claim, a single claims query can request several values at once.

## Topics

### Initializers
- [init([DigitalCredentialsQuery.ClaimsQuery.PathComponent])](./claimpath/init%28_%29.md)
  Initializes a claim path.
### Instance Properties
- [var components: [DigitalCredentialsQuery.ClaimsQuery.PathComponent]](./claimpath/components.md)
  The steps that lead from the top level of a credential to the claim.

## Relationships

### Conforms To
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Describing a claim
- [DigitalCredentialsQuery.ClaimsQuery.PathComponent](./pathcomponent.md)
  A single step in a claims path.
- [DigitalCredentialsQuery.ClaimsQuery.AcceptedValue](./acceptedvalue.md)
  A value that a relying party accepts for a claim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/claimsquery/claimpath)*