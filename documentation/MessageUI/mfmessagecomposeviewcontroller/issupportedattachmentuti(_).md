# isSupportedAttachmentUTI(_:)

**Framework**: Message UI  
**Kind**: method  
**Role**: Type Method

Indicates whether or not the message can accept a file, with the specified UTI, as an attachment.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func isSupportedAttachmentUTI(_ uti: String) -> Bool
```

```objc
+ (BOOL) isSupportedAttachmentUTI:(NSString *) uti;
```

#### Return Value

[`true`](../../Swift/true.md) if a file with the specified UTI can be attached to the message, or [`false`](../../Swift/false.md) otherwise.

## Parameters

- `uti`: The UTI (Uniform Type Identifier) in question. See [Uniform Type Identifiers Reference](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257)

## See Also

### Determining if message composition is available
- [class func canSendText() -> Bool](./cansendtext%28%29.md)
  Returns a Boolean value that indicates whether the current device is capable of sending text messages.
- [class func canSendAttachments() -> Bool](./cansendattachments%28%29.md)
  Indicates whether or not messages can include attachments.
- [class func canSendSubject() -> Bool](./cansendsubject%28%29.md)
  Indicates whether or not messages can include subject lines, according to the user’s configuration in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/issupportedattachmentuti(_:))*