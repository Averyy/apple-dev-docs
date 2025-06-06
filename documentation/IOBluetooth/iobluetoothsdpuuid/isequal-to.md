# isEqual(to:)

**Framework**: IOBluetooth  
**Kind**: method

Compares the target IOBluetoothSDPUUID object with the given otherUUID object.

**Availability**:
- macOS ?+

## Declaration

```swift
func isEqual(to otherUUID: IOBluetoothSDPUUID!) -> Bool
```

#### Return Value

Returns true if the UUID values of each object are equal. This includes the case where the sizes are different but the data itself is the same when the Bluetooth UUID base is applied.

#### Discussion

This method will compare the two UUID values independent of their length.

## Parameters

- `otherUUID`: The UUID object to be compared with the target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/isequal(to:))*