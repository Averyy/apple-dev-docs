# timecodeFrameDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The frame duration that the generator will use to generate timecodes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var timecodeFrameDuration: CMTime { get set }
```

```objc
@property (nonatomic) CMTime timecodeFrameDuration;
```

## See Also

### Configuring the generator
- [var synchronizationTimeout: TimeInterval](./synchronizationtimeout.md)
  The maximum time interval allowed for source synchronization attempts before timing out.
- [var timecodeAlignmentOffset: TimeInterval](./timecodealignmentoffset.md)
  The time offset, in seconds, applied to the generated timecode.
- [func setDelegate((any AVCaptureTimecodeGeneratorDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/timecodeframeduration)*