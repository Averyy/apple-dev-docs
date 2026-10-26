# isSelfContained

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this track references sample data only within its container file.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`isSelfContained`](../avpartialasyncproperty/isselfcontained.md) asynchronously instead.

## Declaration

```swift
var isSelfContained: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSelfContained) BOOL selfContained;
```

## See Also

### Accessing track information
- [formatDescriptions](./formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [playable](./isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [decodable](./isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [enabled](./isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [totalSampleDataLength](./totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [- hasMediaCharacteristic:](./hasmediacharacteristic%28_%29.md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/isselfcontained)*