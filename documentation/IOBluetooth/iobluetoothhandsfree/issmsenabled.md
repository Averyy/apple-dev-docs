# isSMSEnabled

**Framework**: IOBluetooth  
**Kind**: property

Return YES if the device has SMS enabled.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isSMSEnabled: Bool { get }
```

#### Discussion

Returns YES if the device has SMS enabled (by responding to a CMGF command). NO if the device has not set an SMS mode or doesn’t support SMS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/issmsenabled)*