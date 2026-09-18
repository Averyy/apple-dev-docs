# angle

**Framework**: UIKit  
**Kind**: property

The current angle of the hinge, in radians.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
var angle: CGFloat { get }
```

#### Discussion

The rate and granularity of angle updates are system policy and can change based on system state, so don’t depend on a particular update frequency or precision. If you only need to know whether the hinge is closed, partially open, or fully open, prefer `status` over the angle.

## See Also

- [var status: UIHinge.Status](uihinge/status-swift.property.md)
  The current status of the hinge
- [UIHinge.Status](uihinge/status-swift.enum.md)
  The status of an individual hinge


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihinge/angle)*