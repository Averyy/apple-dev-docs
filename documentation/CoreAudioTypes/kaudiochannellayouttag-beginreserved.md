# kAudioChannelLayoutTag_BeginReserved

**Framework**: Core Audio Types  
**Kind**: var

The beginning value for a reserved range of layout tags.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var kAudioChannelLayoutTag_BeginReserved: AudioChannelLayoutTag { get }
```

#### Discussion

The values in the range between `kAudioChannelLayoutTag_BeginReserved` and [`kAudioChannelLayoutTag_EndReserved`](kaudiochannellayouttag_endreserved.md) are for future Apple use. Do not create layout tags that fall in the range created by these values.

## See Also

- [var kAudioChannelLayoutTag_EndReserved: AudioChannelLayoutTag](kaudiochannellayouttag_endreserved.md)
  The ending value for a reserved range of layout tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_beginreserved)*