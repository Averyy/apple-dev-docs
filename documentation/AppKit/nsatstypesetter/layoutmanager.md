# layoutManager

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The layout manager for the text being typeset.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var layoutManager: NSLayoutManager? { get }
```

```objc
@property (assign, readonly, nullable) NSLayoutManager * layoutManager;
```

## See Also

### Accessing the layout manager
- [var usesFontLeading: Bool](./usesfontleading.md)
  A Boolean value controlling whether the typesetter uses the leading (or line gap) value specified in the font metric information.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./typesetterbehavior.md)
  The current typesetter behavior value.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  The threshold controlling when hyphenation is attempted.
- [var bidiProcessingEnabled: Bool](./bidiprocessingenabled.md)
  A Boolean value controlling whether the typesetter performs bidirectional text processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/layoutmanager)*