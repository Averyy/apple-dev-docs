# layoutManager

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the layout manager for the text being typeset.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var layoutManager: NSLayoutManager? { get }
```

```objc
@property (assign, readonly, nullable) NSLayoutManager * layoutManager;
```

## Return Value

The layout manager for the text being typeset. This value is valid only while the typesetter is performing layout.

## See Also

### Accessing the layout manager
- [var usesFontLeading: Bool](./usesfontleading.md)
  Returns whether the typesetter uses the leading (or line gap) value specified in the font metric information of the current font.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./typesetterbehavior.md)
  Returns the current typesetter behavior.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  Returns the current hyphenation factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/layoutmanager)*