# drawsBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver draws its background.

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

[`true`](../../Swift/true.md) to cause the receiver to fill its background with the background color,  [`false`](../../Swift/false.md) otherwise.

## See Also

### Setting graphics attributes
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The receiver’s background color.
- [var allowsDocumentBackgroundColorChange: Bool](./allowsdocumentbackgroundcolorchange.md)
  A Boolean value that indicates whether the receiver allows its background color to change.
- [func changeDocumentBackgroundColor(Any?)](./changedocumentbackgroundcolor%28_%29.md)
  An action method used to set the background color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/drawsbackground)*