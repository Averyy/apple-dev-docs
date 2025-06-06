# isDecodable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the track is decodable in the current environment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var isDecodable: AVAsyncProperty<Root, Bool> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

When this property is [`true`](https://developer.apple.com/documentation/swift/true), the system can decode the track, even if decoding may be too slow for real-time playback.

## See Also

- [static var formatDescriptions: AVAsyncProperty<Root, [CMFormatDescription]>](avpartialasyncproperty/formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [static var isPlayable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isplayable-6txa5.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [static var isEnabled: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isenabled.md)
  A Boolean value that indicates whether the track is in an enabled state.
- [static var isSelfContained: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isselfcontained.md)
  A Boolean value that indicates whether the track references sample data only within its container file.
- [static var totalSampleDataLength: AVAsyncProperty<Root, Int64>](avpartialasyncproperty/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [static var mediaCharacteristics: AVAsyncProperty<Root, [AVMediaCharacteristic]>](avpartialasyncproperty/mediacharacteristics.md)
  The media characteristics for the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/isdecodable)*