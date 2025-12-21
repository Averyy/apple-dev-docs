# drawsBackground

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver draws its background.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var drawsBackground: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) to cause the receiver to fill its background with the background color,  [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [var backgroundColor: NSColor](nstextview/backgroundcolor.md)
  The receiver’s background color.
- [var allowsDocumentBackgroundColorChange: Bool](nstextview/allowsdocumentbackgroundcolorchange.md)
  A Boolean value that indicates whether the receiver allows its background color to change.
- [func changeDocumentBackgroundColor(Any?)](nstextview/changedocumentbackgroundcolor(_:).md)
  An action method used to set the background color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/drawsbackground)*