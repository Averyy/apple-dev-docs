# hasMediaCharacteristic(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a Boolean value that indicates whether the track references media with the specified media characteristic.

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
func hasMediaCharacteristic(_ mediaCharacteristic: AVMediaCharacteristic) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the track references media with the specified characteristic; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `mediaCharacteristic`: The media characteristic of interest.

## See Also

- [var isPlayable: Bool](avcompositiontrack/isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isDecodable: Bool](avcompositiontrack/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isEnabled: Bool](avcompositiontrack/isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [var isSelfContained: Bool](avcompositiontrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var totalSampleDataLength: Int64](avcompositiontrack/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/hasmediacharacteristic(_:))*