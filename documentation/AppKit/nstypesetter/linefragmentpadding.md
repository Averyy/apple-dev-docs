# lineFragmentPadding

**Framework**: AppKit  
**Kind**: property

Returns the current line fragment padding, in points.

**Availability**:
- macOS ?+

## Declaration

```swift
var lineFragmentPadding: CGFloat { get set }
```

#### Return Value

The current line fragment padding, in points; that is, the portion on each end of the line fragment rectangle left blank.

#### Discussion

Text is inset within the line fragment rectangle by this amount.

## See Also

- [var currentTextContainer: NSTextContainer?](nstypesetter/currenttextcontainer.md)
  Returns the text container for the text being typeset.
- [var textContainers: NSArray?](nstypesetter/textcontainers.md)
  Returns an array containing the text containers belonging to the current layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/linefragmentpadding)*