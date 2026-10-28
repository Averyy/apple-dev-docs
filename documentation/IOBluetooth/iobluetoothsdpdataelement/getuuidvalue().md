# getUUIDValue()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

If the data element is a UUID (type 3), it returns the value as an IOBluetoothSDPUUID.

**Availability**:
- macOS

## Declaration

```swift
func getUUIDValue() -> IOBluetoothSDPUUID!
```

```objc
- (IOBluetoothSDPUUID *) getUUIDValue;
```

## Return Value

Returns an IOBluetoothSDPUUID representation of the data element if it is a UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/getuuidvalue())*