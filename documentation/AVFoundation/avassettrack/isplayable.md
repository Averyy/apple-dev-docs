# isPlayable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the track is playable in the current environment.

**Availability**:
- iOS 5.0+ - Deprecated in 16.0
- iPadOS 5.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`isPlayable`](../avpartialasyncproperty/isplayable-6txa5.md) asynchronously instead.

## Declaration

```swift
var isPlayable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPlayable) BOOL playable;
```

## See Also

### Accessing track information
- [formatDescriptions](./formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [decodable](./isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [enabled](./isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [selfContained](./isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [totalSampleDataLength](./totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [- hasMediaCharacteristic:](./hasmediacharacteristic%28_%29.md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/isplayable)*