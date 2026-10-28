# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setDelegate:(id<AVCaptureTimecodeGeneratorDelegate>) delegate queue:(dispatch_queue_t) callbackQueue;
```

## Discussion

Use this method to configure a delegate that handles timecode updates. The specified `queue` ensures thread-safe invocation of delegate methods.

## Parameters

- `delegate`: An object conforming to the [`AVCaptureTimecodeGeneratorDelegate`](../avcapturetimecodegeneratordelegate.md) protocol.
- `callbackQueue`: The dispatch queue on which the delegate methods are invoked. The `callbackQueue` parameter may not be `nil`, except when setting the [`AVCaptureTimecodeGeneratorDelegate`](../avcapturetimecodegeneratordelegate.md) to `nil`, otherwise [`setDelegate(_:queue:)`](./setdelegate%28_,queue%29.md) throws an `NSInvalidArgumentException`.

## See Also

### Configuring the generator
- [var synchronizationTimeout: TimeInterval](./synchronizationtimeout.md)
  The maximum time interval allowed for source synchronization attempts before timing out.
- [var timecodeAlignmentOffset: TimeInterval](./timecodealignmentoffset.md)
  The time offset, in seconds, applied to the generated timecode.
- [var timecodeFrameDuration: CMTime](./timecodeframeduration.md)
  The frame duration that the generator will use to generate timecodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/setdelegate(_:queue:))*