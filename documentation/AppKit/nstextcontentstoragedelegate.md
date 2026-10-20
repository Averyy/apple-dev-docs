# NSTextContentStorageDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

The optional methods that delegates of content storage objects implement to handle content processing.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextContentStorageDelegate : NSTextContentManagerDelegate
```

```objc
@protocol NSTextContentStorageDelegate <NSTextContentManagerDelegate>
```

#### Overview

The optional methods that delegates of content storage objects implement to handle content processing.

## Topics

### Working with paragraphs
- [func textContentStorage(NSTextContentStorage, textParagraphWith: NSRange) -> NSTextParagraph?](./nstextcontentstoragedelegate/textcontentstorage%28_,textparagraphwith%29.md)
  Returns a custom `NSTextParagraph` for the specified range in the content storage’s attributed string.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTextContentManagerDelegate](./nstextcontentmanagerdelegate.md)

## See Also

### Accessing paragraphs
- [var delegate: (any NSTextContentStorageDelegate)?](./nstextcontentstorage/delegate.md)
  The delegate for the content storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstoragedelegate)*