# productKind

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The device’s type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var productKind: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * productKind;
```

## Discussion

Possible values are `"iPhone"`, `"iPod"`, and `"Camera"`.

## See Also

### Identifying a Device
- [var name: String?](./name.md)
  The device’s name as reported by the device module, or if no device module is in control of this device, by the device transport.
- [var icon: CGImage?](./icon.md)
  The device’s icon image.
- [var uuidString: String?](./uuidstring.md)
  A string representation of the device’s universally unique identifier (UUID).
- [var persistentIDString: String?](./persistentidstring.md)
  A string representation of the device’s persistent ID.
- [var serialNumberString: String?](./serialnumberstring.md)
  The device’s serial number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/productkind)*