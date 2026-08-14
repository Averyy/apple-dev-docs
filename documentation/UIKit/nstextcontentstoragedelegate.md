# NSTextContentStorageDelegate

**Framework**: UIKit  
**Kind**: protocol

The optional methods that delegates of content storage objects implement to handle content processing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTextContentManagerDelegate](nstextcontentmanagerdelegate.md)

## See Also

- [var delegate: (any NSTextContentStorageDelegate)?](nstextcontentstorage/delegate.md)
  The delegate for the content storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentstoragedelegate)*