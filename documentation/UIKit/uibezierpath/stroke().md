# stroke()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Draws a line along the path using the current drawing properties.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func stroke()
```

```objc
- (void) stroke;
```

## Discussion

The drawn line is centered on the path with its sides parallel to the path segment. This method applies the current drawing properties to the rendered path.

This method automatically saves the current graphics state prior to drawing and restores that state when it is done, so you do not have to save the graphics state yourself.

## See Also

### Drawing paths
- [func fill()](./fill%28%29.md)
  Uses the current drawing properties to paint the region that the path encloses.
- [func fill(with: CGBlendMode, alpha: CGFloat)](./fill%28with,alpha%29.md)
  Uses the specified blend mode and transparency values to paint the region that the path encloses.
- [func stroke(with: CGBlendMode, alpha: CGFloat)](./stroke%28with,alpha%29.md)
  Draws a line along the path using the specified blend mode and transparency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/stroke())*