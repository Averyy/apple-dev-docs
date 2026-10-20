# contentSizeThatFits(_:)

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The size of your messages view, given the provided maximum size.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func contentSizeThatFits(_ size: CGSize) -> CGSize
```

```objc
- (CGSize) contentSizeThatFits:(CGSize) size;
```

#### Discussion

The system calls this method only when the Messages app needs to update the view’s size and the view controller is presenting a live view in the transcript or input field (the view controller’s [`presentationStyle`](../msmessagesappviewcontroller/presentationstyle.md) property is set to the [`MSMessagesAppPresentationStyle.transcript`](../msmessagesapppresentationstyle/transcript.md) value). Typically, the view’s size needs updating when the live message is added to the transcript, when the transcript’s width changes, or when the locale or dynamic type size changes.

The [`MSMessagesAppViewController`](../msmessagesappviewcontroller.md) class’s default implementation of the [`contentSizeThatFits(_:)`](./contentsizethatfits%28_%29.md) method simply returns the `size` parameter. Override this method to return an appropriate size for your live message view that fits within the provided size. The returned value must be equal to or smaller than the `size` parameter.

## Parameters

- `size`: The maximum available size, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapptranscriptpresentation/contentsizethatfits(_:))*