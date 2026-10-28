# color

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The currently selected color for the color well.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var color: NSColor { get set }
```

```objc
@property (copy) NSColor * color;
```

## Discussion

Use this property to get the currently selected color, or to set the current color programmatically.

## See Also

### Related Documentation
- [var color: NSColor](../nscolorpanel/color.md)
  The color of the receiver.
### Managing the selected color
- [func takeColorFrom(Any?)](./takecolorfrom%28_%29.md)
  Changes the currently selected color to the color of the specified object.
- [var supportsAlpha: Bool](./supportsalpha.md)
  A Boolean value that determines whether the color picker supports alpha values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/color)*