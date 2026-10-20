# voiceChat(withName:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Joins the local player to a voice channel.

**Availability**:
- iOS 4.1+ - Deprecated in 18.0
- iPadOS 4.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported

## Declaration

```swift
func voiceChat(withName name: String) -> GKVoiceChat?
```

```objc
- (GKVoiceChat *) voiceChatWithName:(NSString *) name;
```

#### Return Value

A voice chat object for the channel, or `nil` if an error occurs or parental controls restrict the player from joining a voice chat.

#### Discussion

This method adds the local player to the named voice chat channel and creates it if necessary. GameKit connects players who join a channel with the same name. A match can have multiple channels and a player can join multiple channels.

When the local player disconnects from a match, all voice channels associated with the match stop working. Therefore, before you disconnect a player, you need to stop the associated voice channels and set the voice chat objects to `nil`.

## Parameters

- `name`: The name of the channel to join.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/voicechat(withname:))*