# isDecodable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the track is decodable in the current environment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var isDecodable: Bool { get }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/Swift/true), the system can decode the track, even if decoding may be too slow for real-time playback.

## See Also

- [var isPlayable: Bool](avcompositiontrack/isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isEnabled: Bool](avcompositiontrack/isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [var isSelfContained: Bool](avcompositiontrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var totalSampleDataLength: Int64](avcompositiontrack/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avcompositiontrack/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/isdecodable)*