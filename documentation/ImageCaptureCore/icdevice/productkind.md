# productKind

**Framework**: ImageCaptureCore  
**Kind**: property

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

#### Discussion

Possible values are `"iPhone"`, `"iPod"`, and `"Camera"`.

## See Also

- [var name: String?](icdevice/name.md)
  The device’s name as reported by the device module, or if no device module is in control of this device, by the device transport.
- [var icon: CGImage?](icdevice/icon.md)
  The device’s icon image.
- [var uuidString: String?](icdevice/uuidstring.md)
  A string representation of the device’s universally unique identifier (UUID).
- [var persistentIDString: String?](icdevice/persistentidstring.md)
  A string representation of the device’s persistent ID.
- [var serialNumberString: String?](icdevice/serialnumberstring.md)
  The device’s serial number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/productkind)*