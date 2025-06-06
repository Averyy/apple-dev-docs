# hyphenationFactor

**Framework**: AppKit  
**Kind**: property

Returns the current hyphenation factor.

**Availability**:
- macOS ?+

## Declaration

```swift
var hyphenationFactor: Float { get set }
```

#### Return Value

The hyphenation factor, a value ranging from 0.0 to 1.0 that controls when hyphenation is attempted. By default, the value is 0.0, meaning hyphenation is off. A factor of 1.0 causes hyphenation to be attempted always.

## See Also

- [var layoutManager: NSLayoutManager?](nstypesetter/layoutmanager.md)
  Returns the layout manager for the text being typeset.
- [var usesFontLeading: Bool](nstypesetter/usesfontleading.md)
  Returns whether the typesetter uses the leading (or line gap) value specified in the font metric information of the current font.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](nstypesetter/typesetterbehavior.md)
  Returns the current typesetter behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/hyphenationfactor)*