# RestrictionsResponse.ProfileRestrictions.ANY profile identifier

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains profile restrictions in effect.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RestrictionsResponse.ProfileRestrictions.ANY profile identifier
```

## Topics

### Objects
- [object RestrictionsResponse.ProfileRestrictions.ANY profile identifier.Intersection](restrictionsresponse/profilerestrictions-data.dictionary/any-profile-identifier-data.dictionary/intersection-data.dictionary.md)
  A dictionary that contains intersected restrictions.
- [object RestrictionsResponse.ProfileRestrictions.ANY profile identifier.RestrictedBool](restrictionsresponse/profilerestrictions-data.dictionary/any-profile-identifier-data.dictionary/restrictedbool-data.dictionary.md)
  A dictionary that contains Boolean restrictions.
- [object RestrictionsResponse.ProfileRestrictions.ANY profile identifier.RestrictedValue](restrictionsresponse/profilerestrictions-data.dictionary/any-profile-identifier-data.dictionary/restrictedvalue-data.dictionary.md)
  A dictionary that contains numeric restrictions.
- [object RestrictionsResponse.ProfileRestrictions.ANY profile identifier.Union](restrictionsresponse/profilerestrictions-data.dictionary/any-profile-identifier-data.dictionary/union-data.dictionary.md)
  A dictionary that contains unioned restrictions.

## Properties

- `intersection` (RestrictionsResponse.ProfileRestrictions.ANY profile identifier.Intersection): A dictionary of intersected profile restrictions. Intersected restrictions indicate that new restrictions can only reduce the number of strings in the set.
- `restrictedBool` (RestrictionsResponse.ProfileRestrictions.ANY profile identifier.RestrictedBool): A dictionary of Boolean profile restrictions.
- `restrictedValue` (RestrictionsResponse.ProfileRestrictions.ANY profile identifier.RestrictedValue): A dictionary of numeric profile restrictions.
- `union` (RestrictionsResponse.ProfileRestrictions.ANY profile identifier.Union): A dictionary of unioned profile restrictions. Unioned restrictions indicate that new restrictions can add to the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictionsresponse/profilerestrictions-data.dictionary/any-profile-identifier-data.dictionary)*