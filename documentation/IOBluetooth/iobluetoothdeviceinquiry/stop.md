# stop()

**Framework**: IOBluetooth  
**Kind**: method

Halts the inquiry object. Could either stop the search for new devices, or the updating of found device names.

**Availability**:
- macOS ?+

## Declaration

```swift
func stop() -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the inquiry is successfully stopped. Returns kIOReturnNotPermitted if the inquiry object is already stopped. May return other IOReturn values, as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/stop())*