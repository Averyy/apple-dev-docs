# audioStreamPacketDescriptions

**Framework**: Core Media  
**Kind**: property

Get an array of AudioStreamPacketDescriptions describing audio samples in the buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var audioStreamPacketDescriptions: [AudioStreamPacketDescription]? { get }
```

#### Discussion

Returns a valid array for the variable bytes per packet or variable frames per packet audio data in the provided sample buffer. Nil is returned for all other format types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/audiostreampacketdescriptions)*