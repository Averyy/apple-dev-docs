# isEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the track’s container enables it.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

For file-based media, you can change its [`isEnabled`](avplayeritemtrack/isenabled.md) presentation state using [`AVPlayerItemTrack`](avplayeritemtrack.md).

## See Also

- [var isPlayable: Bool](avmutablemovietrack/isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isDecodable: Bool](avmutablemovietrack/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isSelfContained: Bool](avmutablemovietrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var hasProtectedContent: Bool](avmutablemovietrack/hasprotectedcontent.md)
  A Boolean value that indicates whether a track contains protected content.
- [var totalSampleDataLength: Int64](avmutablemovietrack/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avmutablemovietrack/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/isenabled)*