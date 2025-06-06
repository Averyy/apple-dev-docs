# RestrictionsResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get a list of restrictions.

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
object RestrictionsResponse
```

## Topics

### Commands
- [object RestrictionsResponse.GlobalRestrictions](restrictionsresponse/globalrestrictions-data.dictionary.md)
  A dictionary that contains the global restrictions in effect.
- [object RestrictionsResponse.ProfileRestrictions](restrictionsresponse/profilerestrictions-data.dictionary.md)
  A dictionary that contains restrictions from each profile.
- [object RestrictionsResponse.ErrorChainItem](restrictionsresponse/errorchainitem.md)
  A dictionary that describes an error chain.

## See Also

- [object RestrictionsCommand](restrictionscommand.md)
  The command to get a list of restrictions on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictionsresponse)*