# matchesSearch(_:)

**Framework**: IOBluetooth  
**Kind**: method

Returns TRUE any of the UUID arrays in the search array match the target service.

**Availability**:
- macOS ?+

## Declaration

```swift
func matchesSearch(_ searchArray: [Any]!) -> Bool
```

#### Return Value

Returns `TRUE` if any of the UUID arrays match.

#### Discussion

The given array should contain [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) objects. Each sub-[`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) should contain [`IOBluetoothSDPUUID`](iobluetoothsdpuuid.md) objects. In turn, each sub-NSArray gets passed to -matchesUUIDArray: If any of those returns `TRUE`, then the search stops and `TRUE` is returned. Essentially the primary NSArray contains the OR operations and each sub-array contains the AND operations.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## Parameters

- `searchArray`: An NSArray of NSArrays of IOBluetoothSDPUUID objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/matchessearch(_:))*