# UIHinge.Status

**Framework**: UIKit  
**Kind**: enum

The status of an individual hinge

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
enum Status
```

## Topics

### Getting the hinge status
- [UIHinge.Status.closed](uihinge/status-swift.enum/closed.md)
  The hinge is closed
- [UIHinge.Status.fullyOpen](uihinge/status-swift.enum/fullyopen.md)
  The hinge is open as far as the device allows
- [UIHinge.Status.partiallyOpen](uihinge/status-swift.enum/partiallyopen.md)
  The hinge is partially open
- [UIHinge.Status.unknown](uihinge/status-swift.enum/unknown.md)
  The status of the hinge is unknown
### Initializers
- [init?(rawValue: Int)](uihinge/status-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var angle: CGFloat](uihinge/angle.md)
  The current angle of the hinge, in radians.
- [var status: UIHinge.Status](uihinge/status-swift.property.md)
  The current status of the hinge


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihinge/status-swift.enum)*