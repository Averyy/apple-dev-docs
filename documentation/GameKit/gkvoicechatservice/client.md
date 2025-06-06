# client

**Framework**: GameKit  
**Kind**: property

An object that the voice chat service uses to communicate with remote participants.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
unowned(unsafe) var client: (any GKVoiceChatClient)! { get set }
```

#### Discussion

The client’s chief responsibility is to provide a network connection that the voice chat service can use to connect to another participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/client)*