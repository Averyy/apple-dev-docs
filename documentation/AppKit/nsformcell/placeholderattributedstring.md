# placeholderAttributedString

**Framework**: AppKit  
**Kind**: property

The cell’s attributed placeholder string.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var placeholderAttributedString: NSAttributedString? { get set }
```

#### Discussion

If this property returns `nil`, you can also call `placeholderString` to see if the cell has a plain text placeholder string.

## See Also

- [var placeholderString: String?](nsformcell/placeholderstring.md)
  The cell’s plain text placeholder string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/placeholderattributedstring)*