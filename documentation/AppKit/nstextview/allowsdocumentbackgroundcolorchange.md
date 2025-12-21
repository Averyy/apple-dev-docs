# allowsDocumentBackgroundColorChange

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver allows its background color to change.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsDocumentBackgroundColorChange: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver allows the background color to change, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var backgroundColor: NSColor](nstextview/backgroundcolor.md)
  The receiver’s background color.
- [var drawsBackground: Bool](nstextview/drawsbackground.md)
  A Boolean value that indicates whether the receiver draws its background.
- [func changeDocumentBackgroundColor(Any?)](nstextview/changedocumentbackgroundcolor(_:).md)
  An action method used to set the background color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/allowsdocumentbackgroundcolorchange)*