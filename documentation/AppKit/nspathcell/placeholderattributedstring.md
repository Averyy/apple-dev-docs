# placeholderAttributedString

**Framework**: AppKit  
**Kind**: property

Sets the value of the placeholder attributed string.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
@MainActor var placeholderAttributedString: NSAttributedString? { get set }
```

#### Discussion

If the `NSPathCell` object contains no `NSPathComponentCell` objects, the placeholder attributed string is drawn in their place, if it is not `nil`. If the placeholder attributed string is `nil`, the (non-attributed) placeholder string is drawn with default attributes, if it is not `nil`.

## Parameters

- `string`: The string to set for the placeholder attributed string.

## See Also

- [var placeholderString: String?](nspathcell/placeholderstring.md)
  Returns the placeholder string.
- [var backgroundColor: NSColor?](nspathcell/backgroundcolor.md)
  Returns the current background color of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/placeholderattributedstring)*