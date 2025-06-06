# RestrictionsResponse.ProfileRestrictions

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains restrictions from each profile.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RestrictionsResponse.ProfileRestrictions
```

#### Discussion

This dictionary is only available if `ProfileRestrictions` is `true` in the command.

## Topics

### Commands
- [object RestrictionsResponse.ProfileRestrictions.ANY profile identifier](restrictionsresponse/profilerestrictions-data.dictionary/any-profile-identifier-data.dictionary.md)
  A dictionary that contains profile restrictions in effect.

## See Also

- [object RestrictionsResponse.GlobalRestrictions](restrictionsresponse/globalrestrictions-data.dictionary.md)
  A dictionary that contains the global restrictions in effect.
- [object RestrictionsResponse.ErrorChainItem](restrictionsresponse/errorchainitem.md)
  A dictionary that describes an error chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictionsresponse/profilerestrictions-data.dictionary)*