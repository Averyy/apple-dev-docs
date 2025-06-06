# init(_:duration:timingCurve:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new keyframe using the given value and timestamp.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(_ to: Value, duration: TimeInterval, timingCurve: UnitCurve = .linear)
```

## Parameters

- `to`: The value of the keyframe.
- `duration`: The duration of the segment defined by this keyframe.
- `timingCurve`: A unit curve that controls the speed of interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/linearkeyframe/init(_:duration:timingcurve:))*