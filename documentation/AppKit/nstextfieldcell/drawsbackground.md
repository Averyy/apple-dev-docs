# drawsBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the cell draws its background color.

**Availability**:
- macOS

## Declaration

```swift
var drawsBackground: Bool { get set }
```

```objc
@property BOOL drawsBackground;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the cell draws its background color. In order to prevent inconsistent rendering, background color rendering is automatically disabled for rounded-bezel text fields.

## See Also

### Related Documentation
- [var drawsBackground: Bool](../nstextfield/drawsbackground.md)
  A Boolean value that controls whether the text field’s cell draws a background color behind the text.
### Controlling the Background
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The color of the cell’s background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/drawsbackground)*