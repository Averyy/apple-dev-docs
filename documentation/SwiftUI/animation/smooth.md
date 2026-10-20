# smooth

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A smooth spring animation with a predefined duration and no bounce.

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
@export(implementation)
static var smooth: Animation { get }
```

## See Also

### Getting built-in spring animations
- [static var bouncy: Animation](./bouncy.md)
  A spring animation with a predefined duration and higher amount of bounce.
- [static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation](./bouncy%28duration,extrabounce%29.md)
  A spring animation with a predefined duration and higher amount of bounce that can be tuned.
- [static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation](./smooth%28duration,extrabounce%29.md)
  A smooth spring animation with a predefined duration and no bounce that can be tuned.
- [static var snappy: Animation](./snappy.md)
  A spring animation with a predefined duration and small amount of bounce that feels more snappy.
- [static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation](./snappy%28duration,extrabounce%29.md)
  A spring animation with a predefined duration and small amount of bounce that feels more snappy and can be tuned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/smooth)*