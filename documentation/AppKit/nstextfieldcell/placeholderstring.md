# placeholderString

**Framework**: AppKit  
**Kind**: property

The placeholder text for the cell, specified as a plain text string.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var placeholderString: String? { get set }
```

#### Discussion

Assigning a new value to this property also clears out any value set for the [`placeholderAttributedString`](nstextfieldcell/placeholderattributedstring.md) property.

## See Also

- [var placeholderAttributedString: NSAttributedString?](nstextfieldcell/placeholderattributedstring.md)
  The placeholder text for the cell, specified as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/placeholderstring)*