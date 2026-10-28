# delegateCallbackQueue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The dispatch queue on which delegate callbacks are invoked.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var delegateCallbackQueue: dispatch_queue_t? { get }
```

```objc
@property (nonatomic, readonly, nullable) dispatch_queue_t delegateCallbackQueue;
```

## Discussion

Provides the queue set in [`setDelegate(_:queue:)`](./setdelegate%28_,queue%29.md). If no delegate is assigned, this property is `nil`.

## See Also

### Handling delegate callbacks
- [var delegate: (any AVCaptureTimecodeGeneratorDelegate)?](./delegate.md)
  The delegate that receives timecode updates from the timecode generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/delegatecallbackqueue)*