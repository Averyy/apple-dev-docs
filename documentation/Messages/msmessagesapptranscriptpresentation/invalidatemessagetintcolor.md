# invalidateMessageTintColor()

**Framework**: Messages  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func invalidateMessageTintColor()
```

#### Discussion

Call this when `messageTintColor` changes, e.g. due to change in app state or trait collection.

The message will be updated to reflect the new color. This method will only work if the `presentationStyle` is `MSMessagesAppPresentationStyleTranscript`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapptranscriptpresentation/invalidatemessagetintcolor())*