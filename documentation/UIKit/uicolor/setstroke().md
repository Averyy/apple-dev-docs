# setStroke()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the color of subsequent stroke operations to the color that the receiver represents.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setStroke()
```

```objc
- (void) setStroke;
```

## Discussion

If you subclass `UIColor`, you must implement this method in your subclass. Your custom implementation should modify the stroke color in the current graphics context by setting it to the color represented by the receiver.

## See Also

### Applying the color to the drawing environment
- [Customizing drawings](../customizing-drawings.md)
  Create custom colors and patterns for drawing in your app.
- [func set()](./set%28%29.md)
  Sets the color of subsequent stroke and fill operations to the color that the receiver represents.
- [func setFill()](./setfill%28%29.md)
  Sets the color of subsequent fill operations to the color that the receiver represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/setstroke())*