# delegateCallbackQueue

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

Provides the queue set in [`setDelegate(_:queue:)`](avcapturetimecodegenerator/setdelegate(_:queue:).md). If no delegate is assigned, this property is `nil`.

## See Also

- [var delegate: (any AVCaptureTimecodeGeneratorDelegate)?](avcapturetimecodegenerator/delegate.md)
  The delegate that receives timecode updates from the timecode generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/delegatecallbackqueue)*