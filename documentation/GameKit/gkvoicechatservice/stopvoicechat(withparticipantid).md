# stopVoiceChat(withParticipantID:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Ends a previously established voice chat.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
func stopVoiceChat(withParticipantID participantID: String!)
```

```objc
- (void) stopVoiceChatWithParticipantID:(NSString *) participantID;
```

## Discussion

When this method is called, the client’s [`voiceChatService(_:didStopWithParticipantID:error:)`](../gkvoicechatclient/voicechatservice%28_,didstopwithparticipantid,error%29.md) method is called.

## Parameters

- `participantID`: A string that uniquely identifies the participant in the chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/stopvoicechat(withparticipantid:))*