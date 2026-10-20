# setSupervisionTimeout(_:)

**Framework**: IOBluetooth  
**Kind**: method

Sets the connection supervision timeout.

**Availability**:
- macOS ?+

## Declaration

```swift
func setSupervisionTimeout(_ timeout: UInt16) -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if it was possible to set the connection supervision timeout.

#### Discussion

NOTE: This method is only available in macOS 10.5 (Bluetooth v2.0) or later.

## Parameters

- `timeout`: A client-supplied link supervision timeout value to use to monitor the connection. The timeout value should be specified in slots, so you can use the BluetoothGetSlotsFromSeconds macro to get the proper value. e.g. BluetoothGetSlotsFromSeconds( 5.0 ) will give yield the proper number of slots (8000) for 5 seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/setsupervisiontimeout(_:))*