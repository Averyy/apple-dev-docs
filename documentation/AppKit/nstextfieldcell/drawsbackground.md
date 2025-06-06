# drawsBackground

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the cell draws its background color.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var drawsBackground: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the cell draws its background color. In order to prevent inconsistent rendering, background color rendering is automatically disabled for rounded-bezel text fields.

## See Also

- [var drawsBackground: Bool](nstextfield/drawsbackground.md)
  A Boolean value that controls whether the text field’s cell draws a background color behind the text.
- [var backgroundColor: NSColor?](nstextfieldcell/backgroundcolor.md)
  The color of the cell’s background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/drawsbackground)*