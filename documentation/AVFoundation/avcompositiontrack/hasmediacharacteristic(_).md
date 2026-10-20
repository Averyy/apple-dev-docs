# hasMediaCharacteristic(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the track references media with the specified media characteristic.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func hasMediaCharacteristic(_ mediaCharacteristic: AVMediaCharacteristic) -> Bool
```

```objc
- (BOOL) hasMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic;
```

#### Return Value

[`true`](../../Swift/true.md) if the track references media with the specified characteristic; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `mediaCharacteristic`: The media characteristic of interest.

## See Also

### Accessing track information
- [var isPlayable: Bool](./isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isDecodable: Bool](./isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [var isSelfContained: Bool](./isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var totalSampleDataLength: Int64](./totalsampledatalength.md)
  The total number of bytes of sample data the track requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/hasmediacharacteristic(_:))*