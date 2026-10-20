# uuidString

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

A string representation of the device’s universally unique identifier (UUID).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var uuidString: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * UUIDString;
```

## See Also

### Identifying a Device
- [var name: String?](./name.md)
  The device’s name as reported by the device module, or if no device module is in control of this device, by the device transport.
- [var productKind: String?](./productkind.md)
  The device’s type.
- [var icon: CGImage?](./icon.md)
  The device’s icon image.
- [var persistentIDString: String?](./persistentidstring.md)
  A string representation of the device’s persistent ID.
- [var serialNumberString: String?](./serialnumberstring.md)
  The device’s serial number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/uuidstring)*