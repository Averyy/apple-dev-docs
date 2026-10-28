# usesFontLeading

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns whether the typesetter uses the leading (or line gap) value specified in the font metric information of the current font.

**Availability**:
- macOS

## Declaration

```swift
var usesFontLeading: Bool { get set }
```

```objc
@property BOOL usesFontLeading;
```

## Return Value

[`true`](../../Swift/true.md) if it uses the information in the font metrics, [`false`](../../Swift/false.md) otherwise.

## See Also

### Accessing the layout manager
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  Returns the layout manager for the text being typeset.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./typesetterbehavior.md)
  Returns the current typesetter behavior.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  Returns the current hyphenation factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/usesfontleading)*