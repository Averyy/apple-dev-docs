# client

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

An object that the voice chat service uses to communicate with remote participants.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: No longer supported.

## Declaration

```swift
unowned(unsafe) var client: (any GKVoiceChatClient)! { get set }
```

```objc
@property (assign) id<GKVoiceChatClient> client;
```

#### Discussion

The client’s chief responsibility is to provide a network connection that the voice chat service can use to connect to another participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/client)*