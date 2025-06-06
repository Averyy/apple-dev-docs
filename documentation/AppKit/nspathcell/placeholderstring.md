# placeholderString

**Framework**: AppKit  
**Kind**: property

Returns the placeholder string.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var placeholderString: String? { get set }
```

#### Return Value

The placeholder string.

#### Discussion

If the `NSPathCell` object contains no `NSPathComponentCell` objects, the placeholder attributed string is drawn in their place, if it is not `nil`. If the placeholder attributed string is `nil`, the (non-attributed) placeholder string is drawn with default attributes, if it is not `nil`.

## See Also

- [var placeholderAttributedString: NSAttributedString?](nspathcell/placeholderattributedstring.md)
  Sets the value of the placeholder attributed string.
- [var backgroundColor: NSColor?](nspathcell/backgroundcolor.md)
  Returns the current background color of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/placeholderstring)*