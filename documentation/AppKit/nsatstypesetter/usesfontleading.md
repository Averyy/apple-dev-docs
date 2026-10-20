# usesFontLeading

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value controlling whether the typesetter uses the leading (or line gap) value specified in the font metric information.

**Availability**:
- macOS

## Declaration

```swift
var usesFontLeading: Bool { get set }
```

```objc
@property BOOL usesFontLeading;
```

## See Also

### Accessing the layout manager
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  The layout manager for the text being typeset.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./typesetterbehavior.md)
  The current typesetter behavior value.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  The threshold controlling when hyphenation is attempted.
- [var bidiProcessingEnabled: Bool](./bidiprocessingenabled.md)
  A Boolean value controlling whether the typesetter performs bidirectional text processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/usesfontleading)*