# UIHinge.Status

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The status of an individual hinge

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
enum Status
```

```c
enum UIHingeStatus : NSInteger;
```

## Topics

### Getting the hinge status
- [UIHinge.Status.closed](./status-swift.enum/closed.md)
  The hinge is closed
- [UIHinge.Status.fullyOpen](./status-swift.enum/fullyopen.md)
  The hinge is open as far as the device allows
- [UIHinge.Status.partiallyOpen](./status-swift.enum/partiallyopen.md)
  The hinge is partially open
- [UIHinge.Status.unknown](./status-swift.enum/unknown.md)
  The status of the hinge is unknown
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the hinge state
- [var angle: CGFloat](./angle.md)
  The current angle of the hinge, in radians.
- [var status: UIHinge.Status](./status-swift.property.md)
  The current status of the hinge


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihinge/status-swift.enum)*