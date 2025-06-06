# superscript(_:)

**Framework**: AppKit  
**Kind**: method

This action method applies a superscript attribute to selected text (or all text if the receiver is a plain text object), raising its baseline offset by a predefined amount.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func superscript(_ sender: Any?)
```

## See Also

- [func raiseBaseline(Any?)](nstextview/raisebaseline(_:).md)
  Raises the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
- [func `subscript`(Any?)](nstext/subscript(_:).md)
  This action method applies a subscript attribute to selected text (or all text if the receiver is a plain text object), lowering its baseline offset by a predefined amount.
- [func unscript(Any?)](nstext/unscript(_:).md)
  This action method removes any superscripting or subscripting from selected text (or all text if the receiver is a plain text object).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/superscript(_:))*