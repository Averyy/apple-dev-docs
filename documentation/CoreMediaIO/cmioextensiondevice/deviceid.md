# deviceID

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A universally unique device identifier value.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var deviceID: UUID { get }
```

```objc
@property (atomic, copy, readonly) NSUUID * deviceID;
```

## See Also

### Identifying a Device
- [var localizedName: String](./localizedname.md)
  A localized name for a device.
- [var legacyDeviceID: String](./legacydeviceid.md)
  A legacy device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/deviceid)*