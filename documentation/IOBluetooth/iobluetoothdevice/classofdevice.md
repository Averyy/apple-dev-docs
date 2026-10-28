# classOfDevice

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Gets the full class of device value for the remote device.

**Availability**:
- macOS

## Declaration

```swift
var classOfDevice: BluetoothClassOfDevice { get }
```

```objc
@property (nonatomic, readonly) BluetoothClassOfDevice classOfDevice;
```

## Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.

## See Also

### Related Documentation
- [- getClassOfDevice](./getclassofdevice.md)
  Gets the full class of device value for the remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/classofdevice)*