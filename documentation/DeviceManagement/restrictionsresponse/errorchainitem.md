# RestrictionsResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object RestrictionsResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object RestrictionsResponse.GlobalRestrictions](restrictionsresponse/globalrestrictions-data.dictionary.md)
  A dictionary that contains the global restrictions in effect.
- [object RestrictionsResponse.ProfileRestrictions](restrictionsresponse/profilerestrictions-data.dictionary.md)
  A dictionary that contains restrictions from each profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictionsresponse/errorchainitem)*