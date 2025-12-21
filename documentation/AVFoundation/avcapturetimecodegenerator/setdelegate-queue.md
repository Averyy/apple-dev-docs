# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func setDelegate(_ delegate: (any AVCaptureTimecodeGeneratorDelegate)?, queue callbackQueue: dispatch_queue_t?)
```

#### Discussion

Use this method to configure a delegate that handles timecode updates. The specified `queue` ensures thread-safe invocation of delegate methods.

## Parameters

- `delegate`: An object conforming to the   protocol.
- `callbackQueue`: The dispatch queue on which the delegate methods are invoked. The   parameter may not be  , except when setting the   to  , otherwise   throws an  .

## See Also

- [var synchronizationTimeout: TimeInterval](avcapturetimecodegenerator/synchronizationtimeout.md)
  The maximum time interval allowed for source synchronization attempts before timing out.
- [var timecodeAlignmentOffset: TimeInterval](avcapturetimecodegenerator/timecodealignmentoffset.md)
  The time offset, in seconds, applied to the generated timecode.
- [var timecodeFrameDuration: CMTime](avcapturetimecodegenerator/timecodeframeduration.md)
  The frame duration that the generator will use to generate timecodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/setdelegate(_:queue:))*