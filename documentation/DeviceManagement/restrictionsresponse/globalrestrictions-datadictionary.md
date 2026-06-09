# RestrictionsResponse.GlobalRestrictions

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains the global restrictions in effect.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object RestrictionsResponse.GlobalRestrictions
```

## Topics

### Objects
- [object RestrictionsResponse.GlobalRestrictions.Intersection](restrictionsresponse/globalrestrictions-data.dictionary/intersection-data.dictionary.md)
  A dictionary that contains intersected restrictions.
- [object RestrictionsResponse.GlobalRestrictions.RestrictedBool](restrictionsresponse/globalrestrictions-data.dictionary/restrictedbool-data.dictionary.md)
  A dictionary that contains Boolean restrictions.
- [object RestrictionsResponse.GlobalRestrictions.RestrictedValue](restrictionsresponse/globalrestrictions-data.dictionary/restrictedvalue-data.dictionary.md)
  A dictionary that contains numeric restrictions.
- [object RestrictionsResponse.GlobalRestrictions.Union](restrictionsresponse/globalrestrictions-data.dictionary/union-data.dictionary.md)
  A dictionary that contains unioned restrictions.

## Properties

- `intersection` (RestrictionsResponse.GlobalRestrictions.Intersection): A dictionary of intersected profile restrictions. Intersected restrictions indicate that new restrictions can only reduce the number of strings in the set.
- `restrictedBool` (RestrictionsResponse.GlobalRestrictions.RestrictedBool): A dictionary of Boolean profile restrictions.
- `restrictedValue` (RestrictionsResponse.GlobalRestrictions.RestrictedValue): A dictionary of numeric profile restrictions.
- `union` (RestrictionsResponse.GlobalRestrictions.Union): A dictionary of unioned profile restrictions. Unioned restrictions indicate that new restrictions can add to the set.

## See Also

- [object RestrictionsResponse.ErrorChainItem](restrictionsresponse/errorchainitem.md)
  A dictionary that describes an error chain item.
- [object RestrictionsResponse.ProfileRestrictions](restrictionsresponse/profilerestrictions-data.dictionary.md)
  A dictionary that contains restrictions from each profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictionsresponse/globalrestrictions-data.dictionary)*