# Gradient.Stop

**Framework**: SwiftUI  
**Kind**: struct

One color stop in the gradient.

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
@frozen
struct Stop
```

## Topics

### Creating a gradient stop
- [init(color: Color, location: CGFloat)](gradient/stop/init(color:location:).md)
  Creates a color stop with a color and location.
### Configuring a gradient stop
- [var color: Color](gradient/stop/color.md)
  The color for the stop.
- [var location: CGFloat](gradient/stop/location.md)
  The parametric location of the stop.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(stops: [Gradient.Stop])](gradient/init(stops:).md)
  Creates a gradient from an array of color stops.
- [var stops: [Gradient.Stop]](gradient/stops.md)
  The array of color stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gradient/stop)*