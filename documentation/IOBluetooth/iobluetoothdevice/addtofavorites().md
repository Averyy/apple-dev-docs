# addToFavorites()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Adds the target device to the user’s favorite devices list.

**Availability**:
- macOS

## Declaration

```swift
func addToFavorites() -> IOReturn
```

```objc
- (IOReturn) addToFavorites;
```

#### Return Value

Returns kIOReturnSuccess if the device was successfully added to the user’s list of favorite devices.

#### Discussion

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/addtofavorites())*