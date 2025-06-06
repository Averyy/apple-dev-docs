# setStroke()

**Framework**: UIKit  
**Kind**: method

Sets the color of subsequent stroke operations to the color that the receiver represents.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setStroke()
```

#### Discussion

If you subclass `UIColor`, you must implement this method in your subclass. Your custom implementation should modify the stroke color in the current graphics context by setting it to the color represented by the receiver.

## See Also

- [Customizing drawings](customizing-drawings.md)
  Create custom colors and patterns for drawing in your app.
- [func set()](uicolor/set.md)
  Sets the color of subsequent stroke and fill operations to the color that the receiver represents.
- [func setFill()](uicolor/setfill.md)
  Sets the color of subsequent fill operations to the color that the receiver represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/setstroke())*