# unscript(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This action method removes any superscripting or subscripting from selected text (or all text if the receiver is a plain text object).

**Availability**:
- macOS

## Declaration

```swift
func unscript(_ sender: Any?)
```

```objc
- (void) unscript:(id) sender;
```

## See Also

### Related Documentation
- [func lowerBaseline(Any?)](../nstextview/lowerbaseline%28_%29.md)
  Lowers the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
- [func raiseBaseline(Any?)](../nstextview/raisebaseline%28_%29.md)
  Raises the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
### Setting superscripting and subscripting
- [func superscript(Any?)](./superscript%28_%29.md)
  This action method applies a superscript attribute to selected text (or all text if the receiver is a plain text object), raising its baseline offset by a predefined amount.
- [func `subscript`(Any?)](./subscript%28_%29.md)
  This action method applies a subscript attribute to selected text (or all text if the receiver is a plain text object), lowering its baseline offset by a predefined amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/unscript(_:))*