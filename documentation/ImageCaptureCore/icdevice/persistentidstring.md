# persistentIDString

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

A string representation of the device’s persistent ID.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var persistentIDString: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * persistentIDString;
```

## See Also

### Identifying a Device
- [var name: String?](./name.md)
  The device’s name as reported by the device module, or if no device module is in control of this device, by the device transport.
- [var productKind: String?](./productkind.md)
  The device’s type.
- [var icon: CGImage?](./icon.md)
  The device’s icon image.
- [var uuidString: String?](./uuidstring.md)
  A string representation of the device’s universally unique identifier (UUID).
- [var serialNumberString: String?](./serialnumberstring.md)
  The device’s serial number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/persistentidstring)*