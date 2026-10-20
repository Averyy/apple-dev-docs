# bidiProcessingEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value controlling whether the typesetter performs bidirectional text processing.

**Availability**:
- macOS

## Declaration

```swift
var bidiProcessingEnabled: Bool { get set }
```

```objc
@property BOOL bidiProcessingEnabled;
```

#### Discussion

You can use this method to disable the bidirectional layout stage if you know the paragraph does not need this stage; that is, if the characters in the backing store are in display order.

## See Also

### Accessing the layout manager
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  The layout manager for the text being typeset.
- [var usesFontLeading: Bool](./usesfontleading.md)
  A Boolean value controlling whether the typesetter uses the leading (or line gap) value specified in the font metric information.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./typesetterbehavior.md)
  The current typesetter behavior value.
- [var hyphenationFactor: Float](./hyphenationfactor.md)
  The threshold controlling when hyphenation is attempted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/bidiprocessingenabled)*