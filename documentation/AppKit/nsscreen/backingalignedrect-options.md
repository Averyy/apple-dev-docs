# backingAlignedRect(_:options:)

**Framework**: AppKit  
**Kind**: method

Converts a rectangle in global screen coordinates to a pixel aligned rectangle.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func backingAlignedRect(_ rect: NSRect, options: AlignmentOptions = []) -> NSRect
```

#### Return Value

Returns a a pixel aligned rectangle on the target screen from the given input rectangle in global screen coordinates.

#### Discussion

This method uses [`NSIntegralRectWithOptions(_:_:)`](https://developer.apple.com/documentation/Foundation/NSIntegralRectWithOptions(_:_:)) to produce the pixel aligned rectangle.

## Parameters

- `rect`: The input rectangle in global screen coordinates.
- `options`: Specifies the alignment options. See   for possible values.

## See Also

- [var backingScaleFactor: CGFloat](nsscreen/backingscalefactor.md)
  The backing store pixel scale factor for the screen.
- [func convertRectFromBacking(NSRect) -> NSRect](nsscreen/convertrectfrombacking(_:).md)
  Converts the rectangle from the device pixel aligned coordinates system of a screen.
- [func convertRectToBacking(NSRect) -> NSRect](nsscreen/convertrecttobacking(_:).md)
  Converts the rectangle to the device pixel aligned coordinates system of a screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/backingalignedrect(_:options:))*