# currentTextContainer

**Framework**: AppKit  
**Kind**: property

Returns the text container for the text being typeset.

**Availability**:
- macOS ?+

## Declaration

```swift
unowned(unsafe) var currentTextContainer: NSTextContainer? { get }
```

#### Return Value

The text container for the text being typeset. This value is valid only while the typesetter is performing layout.

## See Also

- [var textContainers: NSArray?](nstypesetter/textcontainers.md)
  Returns an array containing the text containers belonging to the current layout manager.
- [var lineFragmentPadding: CGFloat](nstypesetter/linefragmentpadding.md)
  Returns the current line fragment padding, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/currenttextcontainer)*