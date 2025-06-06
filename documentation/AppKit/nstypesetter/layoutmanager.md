# layoutManager

**Framework**: AppKit  
**Kind**: property

Returns the layout manager for the text being typeset.

**Availability**:
- macOS ?+

## Declaration

```swift
unowned(unsafe) var layoutManager: NSLayoutManager? { get }
```

#### Return Value

The layout manager for the text being typeset. This value is valid only while the typesetter is performing layout.

## See Also

- [var usesFontLeading: Bool](nstypesetter/usesfontleading.md)
  Returns whether the typesetter uses the leading (or line gap) value specified in the font metric information of the current font.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](nstypesetter/typesetterbehavior.md)
  Returns the current typesetter behavior.
- [var hyphenationFactor: Float](nstypesetter/hyphenationfactor.md)
  Returns the current hyphenation factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/layoutmanager)*