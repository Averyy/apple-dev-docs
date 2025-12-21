# animatesDrop

**Framework**: MapKit  
**Kind**: property

A Boolean value indicating whether the annotation view is animated onto the screen.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var animatesDrop: Bool { get set }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/Swift/true), the map view animates the appearance of pin annotation views by making them appear to drop onto the map at the target point. This animation occurs whenever the view transitions from offscreen to onscreen.

## See Also

- [var pinTintColor: UIColor!](mkpinannotationview/pintintcolor.md)
  The color of the pin head.
- [var pinColor: MKPinAnnotationColor](mkpinannotationview/pincolor.md)
  The color of the pin head.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpinannotationview/animatesdrop)*