# MSMessagesAppTranscriptPresentation

**Framework**: Messages  
**Kind**: protocol

A protocol that provides support for displaying live messages in the transcript of the Messages app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol MSMessagesAppTranscriptPresentation
```

#### Overview

These methods are called when a view controller is presented using a [`MSMessagesAppPresentationStyle.transcript`](msmessagesapppresentationstyle/transcript.md) presentation style.

## Topics

### Providing the Content’s Size
- [func contentSizeThatFits(CGSize) -> CGSize](msmessagesapptranscriptpresentation/contentsizethatfits(_:).md)
  The size of your messages view, given the provided maximum size.

## Relationships

### Conforming Types
- [MSMessagesAppViewController](msmessagesappviewcontroller.md)

## See Also

- [IceCreamBuilder: Building an iMessage Extension](icecreambuilder-building-an-imessage-extension.md)
  Allow users to collaborate on the design of ice cream sundae stickers.
- [Creating a Sticker App with a Custom Layout](creating-a-sticker-app-with-a-custom-layout.md)
  Expand on the Messages sticker app template to create an app with a customized user interface.
- [class MSMessagesAppViewController](msmessagesappviewcontroller.md)
  The principal view controller for iMessage apps.
- [enum MSMessagesAppPresentationStyle](msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapptranscriptpresentation)*