# Gradient.Stop

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [init(color: Color, location: CGFloat)](./stop/init%28color,location%29.md)
  Creates a color stop with a color and location.
### Configuring a gradient stop
- [var color: Color](./stop/color.md)
  The color for the stop.
- [var location: CGFloat](./stop/location.md)
  The parametric location of the stop.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a gradient from stops
- [init(stops: [Gradient.Stop])](./init%28stops%29.md)
  Creates a gradient from an array of color stops.
- [var stops: [Gradient.Stop]](./stops.md)
  The array of color stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gradient/stop)*