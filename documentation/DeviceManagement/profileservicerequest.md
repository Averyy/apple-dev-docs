# ProfileServiceRequest

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The request for assigning a profile to a set of devices.

**Availability**:
- Device Assignment Services 5.0+

## Declaration

```
object ProfileServiceRequest
```

## Properties

- `devices` ([string]): Array of strings that contains device serial numbers.
- `profile_uuid` (string): The unique identifier for a profile.

## See Also

### Request and Response
- [object AssignProfileResponse](./assignprofileresponse.md)
- [object AssignProfileResponse.Devices](./assignprofileresponse/devices-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profileservicerequest)*