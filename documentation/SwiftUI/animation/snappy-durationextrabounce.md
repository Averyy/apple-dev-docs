# snappy(duration:extraBounce:)

**Framework**: SwiftUI  
**Kind**: method

A spring animation with a predefined duration and small amount of bounce that feels more snappy and can be tuned.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func snappy(duration: TimeInterval = 0.5, extraBounce: Double = 0.0) -> Animation
```

## Parameters

- `duration`: The perceptual duration, which defines the pace of the   spring. This is approximately equal to the settling duration, but   for very bouncy springs, will be the duration of the period of   oscillation for the spring.
- `extraBounce`: How much additional bounce should be added to the base   bounce of 0.15.

## See Also

- [static var bouncy: Animation](animation/bouncy.md)
  A spring animation with a predefined duration and higher amount of bounce.
- [static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation](animation/bouncy(duration:extrabounce:).md)
  A spring animation with a predefined duration and higher amount of bounce that can be tuned.
- [static var smooth: Animation](animation/smooth.md)
  A smooth spring animation with a predefined duration and no bounce.
- [static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation](animation/smooth(duration:extrabounce:).md)
  A smooth spring animation with a predefined duration and no bounce that can be tuned.
- [static var snappy: Animation](animation/snappy.md)
  A spring animation with a predefined duration and small amount of bounce that feels more snappy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/snappy(duration:extrabounce:))*