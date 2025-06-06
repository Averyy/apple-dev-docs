# totalSampleDataLength

**Framework**: AVFoundation  
**Kind**: property

The total number of bytes of sample data the track requires.

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
var totalSampleDataLength: Int64 { get }
```

#### Discussion

The value may be `0` if the framework can’t determine the total sample data length.

## See Also

- [var isPlayable: Bool](avcompositiontrack/isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isDecodable: Bool](avcompositiontrack/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isEnabled: Bool](avcompositiontrack/isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [var isSelfContained: Bool](avcompositiontrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avcompositiontrack/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/totalsampledatalength)*