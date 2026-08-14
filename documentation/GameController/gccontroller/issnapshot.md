# isSnapshot

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the controller is a snapshot of a controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var isSnapshot: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the controller is a snapshot of a controller. A snapshot is a copy of a real or virtual controller at a moment in time with its current element values. If [`false`](https://developer.apple.com/documentation/swift/false), the controller is a real or virtual controller.

## See Also

- [class func withExtendedGamepad() -> GCController](gccontroller/withextendedgamepad.md)
  Returns a snapshot of a newly created controller with an extended gamepad profile.
- [class func withMicroGamepad() -> GCController](gccontroller/withmicrogamepad.md)
  Returns a snapshot of a newly created controller with a micro gamepad profile.
- [func capture() -> GCController](gccontroller/capture.md)
  Returns a snapshot of the controller with its current element values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/issnapshot)*