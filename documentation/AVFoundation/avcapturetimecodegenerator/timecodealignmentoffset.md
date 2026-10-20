# timecodeAlignmentOffset

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time offset, in seconds, applied to the generated timecode.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var timecodeAlignmentOffset: TimeInterval { get set }
```

```objc
@property (nonatomic) NSTimeInterval timecodeAlignmentOffset;
```

#### Discussion

This offset allows fine-tuning of time alignment for synchronization with external sources or to accommodate any intentional delay. The default value is 0 seconds.

## See Also

### Configuring the generator
- [var synchronizationTimeout: TimeInterval](./synchronizationtimeout.md)
  The maximum time interval allowed for source synchronization attempts before timing out.
- [var timecodeFrameDuration: CMTime](./timecodeframeduration.md)
  The frame duration that the generator will use to generate timecodes.
- [func setDelegate((any AVCaptureTimecodeGeneratorDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/timecodealignmentoffset)*