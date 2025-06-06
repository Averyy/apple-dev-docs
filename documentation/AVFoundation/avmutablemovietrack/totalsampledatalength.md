# totalSampleDataLength

**Framework**: AVFoundation  
**Kind**: property

The total number of bytes of sample data the track requires.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var totalSampleDataLength: Int64 { get }
```

#### Discussion

The value may be `0` if the framework can’t determine the total sample data length.

## See Also

- [var isPlayable: Bool](avmutablemovietrack/isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isDecodable: Bool](avmutablemovietrack/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isEnabled: Bool](avmutablemovietrack/isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [var isSelfContained: Bool](avmutablemovietrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var hasProtectedContent: Bool](avmutablemovietrack/hasprotectedcontent.md)
  A Boolean value that indicates whether a track contains protected content.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avmutablemovietrack/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/totalsampledatalength)*