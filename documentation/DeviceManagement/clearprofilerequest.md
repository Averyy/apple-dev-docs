# ClearProfileRequest

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The request used to remove a profile from devices.

**Availability**:
- Device Assignment Services 5.0+

## Declaration

```
object ClearProfileRequest
```

## Properties

- `devices` ([string]): An array of strings containing device serial numbers.
- `profile_uuid` (string): The unique identifier for a profile.

## See Also

### Request and Response
- [object ClearProfileResponse](./clearprofileresponse.md)
- [object ClearProfileResponse.Devices](./clearprofileresponse/devices-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clearprofilerequest)*