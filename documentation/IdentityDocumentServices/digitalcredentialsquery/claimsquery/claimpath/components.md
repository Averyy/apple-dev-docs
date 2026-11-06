# components

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Instance Property

The steps that lead from the top level of a credential to the claim.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
var components: [DigitalCredentialsQuery.ClaimsQuery.PathComponent]
```

## Discussion

Each step is a [`DigitalCredentialsQuery.ClaimsQuery.PathComponent`](../pathcomponent.md) that selects one level of the credential’s data. The first component applies to the top level of the credential, and each later component applies to the data that the previous component selects. The order of the components matters, because the system follows them in sequence.

For example, a credential that contains the following data has a `city` claim inside an `address` object, and a `nationalities` array:

```json
{
  "address": { "city": "Cupertino" },
  "state": ["CA"]
}
```

To request the city, use a path with two steps that selects `address` and then `city`:

```swift
let cityPath = DigitalCredentialsQuery.ClaimsQuery.ClaimPath([
    .key("address"),
    .key("city")
])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/claimsquery/claimpath/components)*