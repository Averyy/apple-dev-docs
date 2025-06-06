# placeholderString

**Framework**: AppKit  
**Kind**: property

The cell’s plain text placeholder string.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var placeholderString: String? { get set }
```

#### Discussion

If this property returns `nil`, you can also call `placeholderAttributedString` to see if the cell has an attributed placeholder string. Note that invoking this method clears out any attributed string set by the [`placeholderAttributedString`](nsformcell/placeholderattributedstring.md) property.

## See Also

- [var placeholderAttributedString: NSAttributedString?](nsformcell/placeholderattributedstring.md)
  The cell’s attributed placeholder string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/placeholderstring)*