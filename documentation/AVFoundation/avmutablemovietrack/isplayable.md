# isPlayable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the track is playable in the current environment.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var isPlayable: Bool { get }
```

## See Also

- [var isDecodable: Bool](avmutablemovietrack/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isEnabled: Bool](avmutablemovietrack/isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [var isSelfContained: Bool](avmutablemovietrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var hasProtectedContent: Bool](avmutablemovietrack/hasprotectedcontent.md)
  A Boolean value that indicates whether a track contains protected content.
- [var totalSampleDataLength: Int64](avmutablemovietrack/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avmutablemovietrack/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/isplayable)*