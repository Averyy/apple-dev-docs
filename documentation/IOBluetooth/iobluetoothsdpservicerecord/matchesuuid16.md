# matchesUUID16(_:)

**Framework**: IOBluetooth  
**Kind**: method

Returns TRUE the UUID16 is found in the target service.

**Availability**:
- macOS ?+

## Declaration

```swift
func matchesUUID16(_ uuid16: BluetoothSDPUUID16) -> Bool
```

#### Return Value

Returns TRUE if the UUID16 is present in the service.

#### Discussion

NOTE: This method is only available in macOS 10.7 or later.

## Parameters

- `uuid16`: A BluetoothSDPUUID16 to search for in the target service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/matchesuuid16(_:))*