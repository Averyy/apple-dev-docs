# NSTextContentStorageDelegate

**Framework**: AppKit  
**Kind**: protocol

The optional methods that delegates of content storage objects implement to handle content processing.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextContentStorageDelegate : NSTextContentManagerDelegate
```

## Topics

### Working with paragraphs
- [func textContentStorage(NSTextContentStorage, textParagraphWith: NSRange) -> NSTextParagraph?](nstextcontentstoragedelegate/textcontentstorage(_:textparagraphwith:).md)
  Returns a custom paragraph for a range that you provide from the object’s attributed string.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTextContentManagerDelegate](nstextcontentmanagerdelegate.md)

## See Also

- [var delegate: (any NSTextContentStorageDelegate)?](nstextcontentstorage/delegate.md)
  The delegate for the content storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstoragedelegate)*