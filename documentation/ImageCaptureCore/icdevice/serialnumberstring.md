# serialNumberString

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The device’s serial number.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var serialNumberString: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * serialNumberString;
```

#### Discussion

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
- [var persistentIDString: String?](./persistentidstring.md)
  A string representation of the device’s persistent ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/serialnumberstring)*