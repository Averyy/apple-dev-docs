# allowsDocumentBackgroundColorChange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver allows its background color to change.

**Availability**:
- macOS

## Declaration

```swift
var allowsDocumentBackgroundColorChange: Bool { get set }
```

```objc
@property BOOL allowsDocumentBackgroundColorChange;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver allows the background color to change, otherwise [`false`](../../Swift/false.md).

## See Also

### Setting graphics attributes
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The receiver’s background color.
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean value that indicates whether the receiver draws its background.
- [func changeDocumentBackgroundColor(Any?)](./changedocumentbackgroundcolor%28_%29.md)
  An action method used to set the background color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/allowsdocumentbackgroundcolorchange)*