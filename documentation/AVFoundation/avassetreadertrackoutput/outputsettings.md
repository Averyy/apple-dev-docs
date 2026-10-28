# outputSettings

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The output settings for this track output.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var outputSettings: [String : Any]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * outputSettings;
```

## Discussion

The value is a dictionary that contains values for audio and video settings keys. A value of `nil` indicates that the track output vends samples in their original format as stored in the target track. In that case, the track output skips decoding and returns the samples in decode order. A non-`nil` value causes the track output to decode the samples and return them in presentation order.

## See Also

### Inspecting an output
- [var track: AVAssetTrack](./track.md)
  The track from which the output reads sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/outputsettings)*