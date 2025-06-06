# textContainers

**Framework**: AppKit  
**Kind**: property

Returns an array containing the text containers belonging to the current layout manager.

**Availability**:
- macOS ?+

## Declaration

```swift
unowned(unsafe) var textContainers: NSArray? { get }
```

#### Return Value

An array containing the text containers belonging to the current layout manager. This value is valid only while the typesetter is performing layout.

## See Also

- [var layoutManager: NSLayoutManager?](nstypesetter/layoutmanager.md)
  Returns the layout manager for the text being typeset.
- [var currentTextContainer: NSTextContainer?](nstypesetter/currenttextcontainer.md)
  Returns the text container for the text being typeset.
- [var lineFragmentPadding: CGFloat](nstypesetter/linefragmentpadding.md)
  Returns the current line fragment padding, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/textcontainers)*