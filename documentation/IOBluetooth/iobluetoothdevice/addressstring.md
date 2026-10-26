# addressString

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Get a string representation of the Bluetooth device address for the target device. The format of the string is the same as returned by IOBluetoothNSStringFromDeviceAddress().

**Availability**:
- macOS

## Declaration

```swift
var addressString: String! { get }
```

```objc
@property (readonly) NSString * addressString;
```

#### Discussion

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## See Also

### Related Documentation
- [- getAddressString](./getaddressstring.md)
  Get a string representation of the Bluetooth device address for the target device. The format of the string is the same as returned by IOBluetoothNSStringFromDeviceAddress().


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/addressstring)*