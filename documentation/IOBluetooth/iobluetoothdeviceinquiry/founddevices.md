# foundDevices()

**Framework**: IOBluetooth  
**Kind**: method

Returns found IOBluetoothDevice objects as an array.

**Availability**:
- macOS ?+

## Declaration

```swift
func foundDevices() -> [Any]!
```

#### Return Value

Returns an NSArray of IOBluetoothDevice objects.

#### Discussion

Will not return nil. If there are no devices found, returns an array with length of 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/founddevices())*