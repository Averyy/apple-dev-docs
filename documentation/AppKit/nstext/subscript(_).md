# subscript(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This action method applies a subscript attribute to selected text (or all text if the receiver is a plain text object), lowering its baseline offset by a predefined amount.

**Availability**:
- macOS

## Declaration

```swift
func `subscript`(_ sender: Any?)
```

```objc
- (void) subscript:(id) sender;
```

## See Also

### Related Documentation
- [func lowerBaseline(Any?)](../nstextview/lowerbaseline%28_%29.md)
  Lowers the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
### Setting superscripting and subscripting
- [func superscript(Any?)](./superscript%28_%29.md)
  This action method applies a superscript attribute to selected text (or all text if the receiver is a plain text object), raising its baseline offset by a predefined amount.
- [func unscript(Any?)](./unscript%28_%29.md)
  This action method removes any superscripting or subscripting from selected text (or all text if the receiver is a plain text object).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/subscript(_:))*