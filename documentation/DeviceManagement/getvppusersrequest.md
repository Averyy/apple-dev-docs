# GetVppUsersRequest

**Framework**: Devicemanagement  
**Kind**: dictionary

The request for the users’ details service.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object GetVppUsersRequest
```

#### Discussion

> **Note**:  The `batchToken` encodes the original value of `includeRetired`; therefore, if a `batchToken` is present on the request, the `includeRetired` field (if passed) is ignored.

## See Also

- [object GetVppUsersResponse](getvppusersresponse.md)
  The response from the users’ details service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceManagement/getvppusersrequest)*