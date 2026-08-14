# isSupportedAttachmentUTI(_:)

**Framework**: Message UI  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a file with the specified UTI can be attached to the message, or [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `uti`: The UTI (Uniform Type Identifier) in question. See [`Uniform Type Identifiers Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257)

## See Also

- [class func canSendText() -> Bool](mfmessagecomposeviewcontroller/cansendtext.md)
  Returns a Boolean value that indicates whether the current device is capable of sending text messages.
- [class func canSendAttachments() -> Bool](mfmessagecomposeviewcontroller/cansendattachments.md)
  Indicates whether or not messages can include attachments.
- [class func canSendSubject() -> Bool](mfmessagecomposeviewcontroller/cansendsubject.md)
  Indicates whether or not messages can include subject lines, according to the user’s configuration in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/issupportedattachmentuti(_:))*