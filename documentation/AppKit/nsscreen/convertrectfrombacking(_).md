# convertRectFromBacking(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Converts the rectangle from the device pixel aligned coordinates system of a screen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func convertRectFromBacking(_ rect: NSRect) -> NSRect
```

```objc
- (NSRect) convertRectFromBacking:(NSRect) rect;
```

#### Return Value

The rectangle converted from the device pixel aligned coordinates system of the screen.

## Parameters

- `rect`: The rectangle.

## See Also

### Converting Between Screen and Backing Coordinates
- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](./backingalignedrect%28_,options%29.md)
  Converts a rectangle in global screen coordinates to a pixel aligned rectangle.
- [var backingScaleFactor: CGFloat](./backingscalefactor.md)
  The backing store pixel scale factor for the screen.
- [func convertRectToBacking(NSRect) -> NSRect](./convertrecttobacking%28_%29.md)
  Converts the rectangle to the device pixel aligned coordinates system of a screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/convertrectfrombacking(_:))*