# layoutManager

**Framework**: AppKit  
**Kind**: property

The layout manager for the text being typeset.

**Availability**:
- macOS ?+

## Declaration

```swift
unowned(unsafe) var layoutManager: NSLayoutManager? { get }
```

## See Also

- [var usesFontLeading: Bool](nsatstypesetter/usesfontleading.md)
  A Boolean value controlling whether the typesetter uses the leading (or line gap) value specified in the font metric information.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](nsatstypesetter/typesetterbehavior.md)
  The current typesetter behavior value.
- [var hyphenationFactor: Float](nsatstypesetter/hyphenationfactor.md)
  The threshold controlling when hyphenation is attempted.
- [var bidiProcessingEnabled: Bool](nsatstypesetter/bidiprocessingenabled.md)
  A Boolean value controlling whether the typesetter performs bidirectional text processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/layoutmanager)*