# displayName

**Framework**: DeviceDiscoveryExtension  
**Kind**: property  
**Role**: Instance Property

A name for the device to display to the user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
var displayName: String { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSString * displayName;
```

## See Also

### Identifying the device
- [var identifier: String](./identifier.md)
  A unique identifier for the device.
- [var category: DDDevice.Category](./category-swift.property.md)
  An option that determies the icon that the picker UI displays for the device.
- [DDDevice.Category](./category-swift.enum.md)
  An option that determines the icon for the device in the picker UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/displayname)*