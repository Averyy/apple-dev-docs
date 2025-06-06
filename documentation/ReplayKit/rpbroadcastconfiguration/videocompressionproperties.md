# videoCompressionProperties

**Framework**: ReplayKit  
**Kind**: property

The compression properties for encoding movie clips that are to be overwritten.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var videoCompressionProperties: [String : any NSSecureCoding & NSObjectProtocol]? { get set }
```

#### Discussion

See [`AVVideoCompressionPropertiesKey`](https://developer.apple.com/documentation/AVFoundation/AVVideoCompressionPropertiesKey) for a list of available properties.

## See Also

- [var clipDuration: TimeInterval](rpbroadcastconfiguration/clipduration.md)
  The duration of movie clips sent the to the movie clip handler extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration/videocompressionproperties)*