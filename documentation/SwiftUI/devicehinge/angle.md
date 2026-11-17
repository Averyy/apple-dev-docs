# angle

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

Current angle of the hinge.

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
var angle: Angle
```

## Discussion

The rate and granularity of angle updates are system policy and can change based on system state, so don’t depend on a particular update frequency or precision. If you only need to know whether the hinge is closed, partially open, or fully open, prefer [`status`](./status-swift.property.md) over the angle.

## See Also

### Getting hinge information
- [var status: DeviceHinge.Status](./status-swift.property.md)
  Current status of the hinge.
- [DeviceHinge.Status](./status-swift.struct.md)
  The status of an individual hinge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/devicehinge/angle)*