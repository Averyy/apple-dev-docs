# typesetterBehavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the current typesetter behavior.

**Availability**:
- macOS

## Declaration

```swift
var typesetterBehavior: NSLayoutManager.TypesetterBehavior { get set }
```

```objc
@property NSTypesetterBehavior typesetterBehavior;
```

## Return Value

The current typesetter behavior.

## See Also

### Accessing the layout manager
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  Returns the layout manager for the text being typeset.
- [var usesFontLeading: Bool](./usesfontleading.md)
  Returns whether the typesetter uses the leading (or line gap) value specified in the font metric information of the current font.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  Returns the current hyphenation factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/typesetterbehavior)*