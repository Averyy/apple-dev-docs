# clipDuration

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

The duration of movie clips sent the to the movie clip handler extension.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
var clipDuration: TimeInterval { get set }
```

```objc
@property (nonatomic, assign) NSTimeInterval clipDuration;
```

## Discussion

The default value for a movie clip is 5 seconds.

## See Also

### Configuring Movie Clips
- [var videoCompressionProperties: [String : any NSSecureCoding & NSObjectProtocol]?](./videocompressionproperties.md)
  The compression properties for encoding movie clips that are to be overwritten.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration/clipduration)*