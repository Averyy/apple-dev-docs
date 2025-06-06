# NSStringDrawingContext

**Framework**: AppKit  
**Kind**: class

An object that manages metrics for drawing attributed strings.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class NSStringDrawingContext
```

#### Overview

Prior to drawing, you can create an instance of this class and use it to specify the minimum scale factor and tracking adjustments for a string. After drawing, you can retrieve the actual values that were used during drawing.

To use this class, allocate and initialize a new instance, set the minimum values, and pass your object to one of the corresponding [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) methods that take the context object as a parameter. Upon completion of drawing, you can use the actual drawing values to make adjustments or record where the string was actually drawn.

## Topics

### Accessing the scale factors
- [var minimumScaleFactor: CGFloat](nsstringdrawingcontext/minimumscalefactor.md)
  The scale factor that determines the smallest font size to use during drawing.
- [var actualScaleFactor: CGFloat](nsstringdrawingcontext/actualscalefactor.md)
  The actual scale factor that the system applied to the font during drawing.
### Getting the drawing bounds
- [var totalBounds: CGRect](nsstringdrawingcontext/totalbounds.md)
  The most recent bounding rectangle that the system used to draw the string.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct NSStringDrawingOptions](../UIKit/NSStringDrawingOptions.md)
  Constants that specify the rendering options for drawing a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext)*