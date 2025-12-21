# synchronizationTimeout

**Framework**: AVFoundation  
**Kind**: property

The maximum time interval allowed for source synchronization attempts before timing out.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var synchronizationTimeout: TimeInterval { get set }
```

#### Discussion

This property specifies the duration, in seconds, that the [`AVCaptureTimecodeGenerator`](avcapturetimecodegenerator.md) will attempt to synchronize with a timecode source before timing out if synchronization cannot be achieved. If this threshold is exceeded, the synchronization status updates to reflect a timeout, and your [`timecodeGenerator(_:transitionedTo:for:)`](avcapturetimecodegeneratordelegate/timecodegenerator(_:transitionedto:for:).md) delegate method fires, informing you of the event. The default value is 15 seconds.

## See Also

- [var timecodeAlignmentOffset: TimeInterval](avcapturetimecodegenerator/timecodealignmentoffset.md)
  The time offset, in seconds, applied to the generated timecode.
- [var timecodeFrameDuration: CMTime](avcapturetimecodegenerator/timecodeframeduration.md)
  The frame duration that the generator will use to generate timecodes.
- [func setDelegate((any AVCaptureTimecodeGeneratorDelegate)?, queue: dispatch_queue_t?)](avcapturetimecodegenerator/setdelegate(_:queue:).md)
  Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/synchronizationtimeout)*