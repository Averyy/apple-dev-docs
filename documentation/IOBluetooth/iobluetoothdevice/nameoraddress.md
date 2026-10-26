# nameOrAddress

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Get the human readable name of the remote device. If the name is not present, it will return a string containing the device’s address.

**Availability**:
- macOS

## Declaration

```swift
var nameOrAddress: String! { get }
```

```objc
@property (readonly) NSString * nameOrAddress;
```

#### Discussion

If a remote name request has been successfully completed, the device name will be returned. If not, a string containg the device address in the format of “XX-XX-XX-XX-XX-XX” will be returned.

## See Also

### Related Documentation
- [- getNameOrAddress](./getnameoraddress.md)
  Get the human readable name of the remote device. If the name is not present, it will return a string containing the device’s address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/nameoraddress)*