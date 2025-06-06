# setColor(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Adjusts the receiver to make the specified color the currently selected color.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setColor(_ newColor: NSColor)
```

#### Discussion

This method is invoked on the current color picker each time `NSColorPanel`‘s [`color`](nscolorpanel/color.md) method is invoked. If `color` is actually different from the color picker’s color (as it would be if, for example, the user dragged a color into `NSColorPanel`‘s color well), this method could be used to update the color picker’s color to reflect the change.

## Parameters

- `newColor`: The color to set as the currently selected color.

## See Also

- [Color Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html#//apple_ref/doc/uid/10000082i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingcustom/setcolor(_:))*