# setBorderColor(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the color of all borders of the text block.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setBorderColor(_ color: NSColor?)
```

```objc
- (void) setBorderColor:(NSColor *) color;
```

#### Discussion

This setting has no visible effect unless the border width is larger than the default, which is 0.

## Parameters

- `color`: The new color.

## See Also

### Related Documentation
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](./setwidth%28_,type,for%29.md)
  Sets the width of all edges of a specified layer of the text block.
### Working with color
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The background color of the text block.
- [func setBorderColor(NSColor?, rectEdge: CGRectEdge)](./setbordercolor%28_,rectedge%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setbordercolor(_:))*