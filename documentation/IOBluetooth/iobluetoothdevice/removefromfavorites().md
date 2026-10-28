# removeFromFavorites()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Removes the target device from the user’s favorite devices list.

**Availability**:
- macOS

## Declaration

```swift
func removeFromFavorites() -> IOReturn
```

```objc
- (IOReturn) removeFromFavorites;
```

## Return Value

Returns kIOReturnSuccess if the device was successfully removed from the user’s list of favorite devices.

## Discussion

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/removefromfavorites())*