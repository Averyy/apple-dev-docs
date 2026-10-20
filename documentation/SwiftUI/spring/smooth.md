# smooth

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A smooth spring with a predefined duration and no bounce.

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
@export(implementation)
static var smooth: Spring { get }
```

## See Also

### Getting built-in springs
- [static var bouncy: Spring](./bouncy.md)
  A spring with a predefined duration and higher amount of bounce.
- [static func bouncy(duration: TimeInterval, extraBounce: Double) -> Spring](./bouncy%28duration,extrabounce%29.md)
  A spring with a predefined duration and higher amount of bounce that can be tuned.
- [static func smooth(duration: TimeInterval, extraBounce: Double) -> Spring](./smooth%28duration,extrabounce%29.md)
  A smooth spring with a predefined duration and no bounce that can be tuned.
- [static var snappy: Spring](./snappy.md)
  A spring with a predefined duration and small amount of bounce that feels more snappy.
- [static func snappy(duration: TimeInterval, extraBounce: Double) -> Spring](./snappy%28duration,extrabounce%29.md)
  A spring with a predefined duration and small amount of bounce that feels more snappy and can be tuned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/smooth)*