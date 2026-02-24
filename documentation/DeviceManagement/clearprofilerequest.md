# ClearProfileRequest

**Framework**: Device Management  
**Kind**: dictionary

The request used to remove a profile from devices.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ClearProfileRequest
```

## Properties

- `devices` ([string]): An array of strings containing device serial numbers.
- `profile_uuid` (string): The unique identifier for a profile.

## See Also

- [object ClearProfileResponse](clearprofileresponse.md)
- [object ClearProfileResponse.Devices](clearprofileresponse/devices-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clearprofilerequest)*