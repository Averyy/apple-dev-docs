# DeviceHinge.Status

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The status of an individual hinge.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
struct Status
```

## Topics

### Getting hinge status
- [static var closed: DeviceHinge.Status](./status-swift.struct/closed.md)
  The hinge is closed.
- [static var fullyOpen: DeviceHinge.Status](./status-swift.struct/fullyopen.md)
  The hinge is open as far as the device allows.
- [static var partiallyOpen: DeviceHinge.Status](./status-swift.struct/partiallyopen.md)
  The hinge is partially open.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting hinge information
- [var angle: Angle](./angle.md)
  Current angle of the hinge.
- [var status: DeviceHinge.Status](./status-swift.property.md)
  Current status of the hinge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/devicehinge/status-swift.struct)*