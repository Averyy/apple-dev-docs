# isDecodable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the track is decodable in the current environment.

**Availability**:
- iOS 11.0+ - Deprecated in 16.0
- iPadOS 11.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.13+ - Deprecated in 13.0
- tvOS 11.0+ - Deprecated in 16.0
- watchOS 4.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`isDecodable`](../avpartialasyncproperty/isdecodable.md) asynchronously instead.

## Declaration

```swift
var isDecodable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isDecodable) BOOL decodable;
```

#### Discussion

When this property is [`true`](../../Swift/true.md), the system can decode the track, even if decoding may be too slow for real-time playback.

## See Also

### Accessing track information
- [formatDescriptions](./formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [playable](./isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [enabled](./isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [selfContained](./isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [totalSampleDataLength](./totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [- hasMediaCharacteristic:](./hasmediacharacteristic%28_%29.md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/isdecodable)*