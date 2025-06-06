# convertRectToBacking(_:)

**Framework**: AppKit  
**Kind**: method

Converts the rectangle to the device pixel aligned coordinates system of a screen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func convertRectToBacking(_ rect: NSRect) -> NSRect
```

#### Return Value

The rectangle converted to the device pixel aligned coordinates system of the screen.

## Parameters

- `rect`: The rectangle.

## See Also

- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](nsscreen/backingalignedrect(_:options:).md)
  Converts a rectangle in global screen coordinates to a pixel aligned rectangle.
- [var backingScaleFactor: CGFloat](nsscreen/backingscalefactor.md)
  The backing store pixel scale factor for the screen.
- [func convertRectFromBacking(NSRect) -> NSRect](nsscreen/convertrectfrombacking(_:).md)
  Converts the rectangle from the device pixel aligned coordinates system of a screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/convertrecttobacking(_:))*