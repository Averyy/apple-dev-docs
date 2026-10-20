# loopCount

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The number of times the object played the media.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var loopCount: Int { get }
```

```objc
@property (readonly) NSInteger loopCount;
```

#### Discussion

This value starts at 0 and increments as the player continues to loop the replica player items.

This property is key-value observable.

## See Also

### Observing looping state
- [var status: AVPlayerLooper.Status](./status-swift.property.md)
  A status that indicates the object’s ability to loop playback.
- [AVPlayerLooper.Status](./status-swift.enum.md)
  Status constants that indicate whether a looper can successfully perform looping playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/loopcount)*