# kAudioChannelLayoutTag_DiscreteInOrder

**Framework**: Core Audio Types  
**Kind**: var

A tag used to map input channels to output channels without changing the channel order.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var kAudioChannelLayoutTag_DiscreteInOrder: AudioChannelLayoutTag { get }
```

#### Discussion

This tag needs to be `OR`ed with the actual number of channels.

## See Also

- [var kAudioChannelLayoutTag_Unknown: AudioChannelLayoutTag](kaudiochannellayouttag_unknown.md)
  The channel layout is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_discreteinorder)*