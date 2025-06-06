# setClassOfDevice(_:forTimeInterval:)

**Framework**: IOBluetooth  
**Kind**: method

Sets the current class of device value, for the specified amount of time. Note that the time interval  be set and valid. The range of acceptable values is 30-120 seconds. Anything above or below will be rounded up, or down, as appropriate.

**Availability**:
- macOS ?+

## Declaration

```swift
func setClassOfDevice(_ classOfDevice: BluetoothClassOfDevice, forTimeInterval seconds: TimeInterval) -> IOReturn
```

#### Return Value

Returns the whether setting the class of device value was successful. 0 if success, error code otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/setclassofdevice(_:fortimeinterval:))*