# AUMessageChannel

**Framework**: Audio Toolbox  
**Kind**: protocol  
**Role**: Protocol

A specification for a bidirectional communication message channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol AUMessageChannel
```

```objc
@protocol AUMessageChannel
```

## Overview

Audio units and their hosts have unique communication needs. For example, for better audio processing they can exchange musical context. An audio unit implements a class that conforms to [`AUMessageChannel`](./aumessagechannel.md) and returns an instance from [`messageChannel(for:)`](./auaudiounit/messagechannel%28for%29.md). A host queries the instance through the channel name.

This protocol offers a method to send messages to an audio unit and a block to send messages to the host.

## Topics

### Sending a Message to an Audio Unit
- [func callAudioUnit([AnyHashable : Any]) -> [AnyHashable : Any]](./aumessagechannel/callaudiounit%28_%29.md)
  Sends an audio unit a custom data message.
### Sending a Message to a Host
- [var callHostBlock: CallHostBlock?](./aumessagechannel/callhostblock.md)
  A callback for the audio unit to send a message to the host.

## See Also

### Messaging Channels
- [func messageChannel(for: String) -> any AUMessageChannel](./auaudiounit/messagechannel%28for%29.md)
  Returns an object for bidirectional communication between an audio unit and its host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aumessagechannel)*