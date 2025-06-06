# placeholderAttributedString

**Framework**: AppKit  
**Kind**: property

The placeholder text for the cell, specified as an attributed string.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var placeholderAttributedString: NSAttributedString? { get set }
```

#### Discussion

Assigning a new value to this property also clears out any value set for the [`placeholderString`](nstextfieldcell/placeholderstring.md) property.

## See Also

- [var placeholderString: String?](nstextfieldcell/placeholderstring.md)
  The placeholder text for the cell, specified as a plain text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/placeholderattributedstring)*