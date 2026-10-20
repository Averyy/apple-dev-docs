# videoCompressionProperties

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

The compression properties for encoding movie clips that are to be overwritten.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
var videoCompressionProperties: [String : any NSSecureCoding & NSObjectProtocol]? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSDictionary<NSString *,NSObject<NSCoding,NSSecureCoding> *> * videoCompressionProperties;
```

#### Discussion

See [`AVVideoCompressionPropertiesKey`](../../AVFoundation/avvideocompressionpropertieskey.md) for a list of available properties.

## See Also

### Configuring Movie Clips
- [var clipDuration: TimeInterval](./clipduration.md)
  The duration of movie clips sent the to the movie clip handler extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration/videocompressionproperties)*