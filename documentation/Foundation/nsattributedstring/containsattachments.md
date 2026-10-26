# containsAttachments

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the attribute string contains any attachment attributes.

**Availability**:
- macOS 10.0+

> **Deprecated**: Use [`containsAttachments(in:)`](./containsattachments%28in%29.md) instead.

## Declaration

```swift
var containsAttachments: Bool { get }
```

```objc
@property (readonly) BOOL containsAttachments;
```

#### Return Value

YES if the attributed string contains any attachment attributes, otherwise NO.

#### Discussion

This method checks only for attachment attributes, not for `NSAttachmentCharacter`.

## See Also

### Deprecated Properties
- [+ textFileTypes](./textfiletypes.md)
  Returns an array of strings that represent file types that can be loaded as text.
- [+ textUnfilteredFileTypes](./textunfilteredfiletypes.md)
  Returns an array of strings that represent file types that can be loaded as a text.
- [+ textPasteboardTypes](./textpasteboardtypes.md)
  Returns an array of pasteboard types that can be loaded as text.
- [+ textUnfilteredPasteboardTypes](./textunfilteredpasteboardtypes.md)
  Returns an array of pasteboard types that can be loaded as text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/containsattachments)*