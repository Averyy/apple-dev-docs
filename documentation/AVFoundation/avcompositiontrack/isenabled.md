# isEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the track’s container enables it.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var isEnabled: Bool { get }
```

#### Discussion

For file-based media, you can change its [`isEnabled`](avplayeritemtrack/isenabled.md) presentation state using [`AVPlayerItemTrack`](avplayeritemtrack.md).

## See Also

- [var isPlayable: Bool](avcompositiontrack/isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isDecodable: Bool](avcompositiontrack/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isSelfContained: Bool](avcompositiontrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var totalSampleDataLength: Int64](avcompositiontrack/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avcompositiontrack/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/isenabled)*