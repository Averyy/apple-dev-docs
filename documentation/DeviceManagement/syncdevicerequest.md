# SyncDeviceRequest

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The request to sync the list of devices.

**Availability**:
- Device Assignment Services 5.0+

## Declaration

```
object SyncDeviceRequest
```

## Properties

- `cursor` (string): A hex string that represents the starting position for a request. Use this to retrieve the list of devices that have been added or removed since a previous request. The string can be up to 1000 characters.
- `limit` (int32): The maximum number of entries to return. Optional.

  **Default**: `100`; **Maximum**: `1000`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/syncdevicerequest)*