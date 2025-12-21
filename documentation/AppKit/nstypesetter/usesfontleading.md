# usesFontLeading

**Framework**: AppKit  
**Kind**: property

Returns whether the typesetter uses the leading (or line gap) value specified in the font metric information of the current font.

**Availability**:
- macOS ?+

## Declaration

```swift
var usesFontLeading: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if it uses the information in the font metrics, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [var layoutManager: NSLayoutManager?](nstypesetter/layoutmanager.md)
  Returns the layout manager for the text being typeset.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](nstypesetter/typesetterbehavior.md)
  Returns the current typesetter behavior.
- [var hyphenationFactor: Float](nstypesetter/hyphenationfactor.md)
  Returns the current hyphenation factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/usesfontleading)*