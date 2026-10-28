# textContainers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns an array containing the text containers belonging to the current layout manager.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var textContainers: NSArray? { get }
```

```objc
@property (assign, readonly, nullable) NSArray<NSTextContainer *> * textContainers;
```

## Return Value

An array containing the text containers belonging to the current layout manager. This value is valid only while the typesetter is performing layout.

## See Also

### Related Documentation
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  Returns the layout manager for the text being typeset.
### Managing text containers
- [var currentTextContainer: NSTextContainer?](./currenttextcontainer.md)
  Returns the text container for the text being typeset.
- [var lineFragmentPadding: CGFloat](./linefragmentpadding.md)
  Returns the current line fragment padding, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/textcontainers)*