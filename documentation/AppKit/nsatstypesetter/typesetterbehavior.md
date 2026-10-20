# typesetterBehavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current typesetter behavior value.

**Availability**:
- macOS

## Declaration

```swift
var typesetterBehavior: NSLayoutManager.TypesetterBehavior { get set }
```

```objc
@property NSTypesetterBehavior typesetterBehavior;
```

## See Also

### Accessing the layout manager
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  The layout manager for the text being typeset.
- [var usesFontLeading: Bool](./usesfontleading.md)
  A Boolean value controlling whether the typesetter uses the leading (or line gap) value specified in the font metric information.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  The threshold controlling when hyphenation is attempted.
- [var bidiProcessingEnabled: Bool](./bidiprocessingenabled.md)
  A Boolean value controlling whether the typesetter performs bidirectional text processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/typesetterbehavior)*