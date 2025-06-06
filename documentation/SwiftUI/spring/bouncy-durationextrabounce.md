# bouncy(duration:extraBounce:)

**Framework**: SwiftUI  
**Kind**: method

A spring with a predefined duration and higher amount of bounce that can be tuned.

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
static func bouncy(duration: TimeInterval = 0.5, extraBounce: Double = 0.0) -> Spring
```

## Parameters

- `duration`: The perceptual duration, which defines the pace of the   spring. This is approximately equal to the settling duration, but   for very bouncy springs, will be the duration of the period of   oscillation for the spring.
- `extraBounce`: How much additional bounce should be added to the base   bounce of 0.3.

## See Also

- [static var bouncy: Spring](spring/bouncy.md)
  A spring with a predefined duration and higher amount of bounce.
- [static var smooth: Spring](spring/smooth.md)
  A smooth spring with a predefined duration and no bounce.
- [static func smooth(duration: TimeInterval, extraBounce: Double) -> Spring](spring/smooth(duration:extrabounce:).md)
  A smooth spring with a predefined duration and no bounce that can be tuned.
- [static var snappy: Spring](spring/snappy.md)
  A spring with a predefined duration and small amount of bounce that feels more snappy.
- [static func snappy(duration: TimeInterval, extraBounce: Double) -> Spring](spring/snappy(duration:extrabounce:).md)
  A spring with a predefined duration and small amount of bounce that feels more snappy and can be tuned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/bouncy(duration:extrabounce:))*