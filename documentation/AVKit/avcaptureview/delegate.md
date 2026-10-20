# delegate

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The capture view’s delegate object.

**Availability**:
- macOS 10.10+

## Declaration

```swift
weak var delegate: (any AVCaptureViewDelegate)? { get set }
```

```objc
@property (weak, nullable) id<AVCaptureViewDelegate> delegate;
```

#### Discussion

The capture view disables the start recording button if you don’t provide a delegate object.

## See Also

### Configuring the delegate
- [protocol AVCaptureViewDelegate](../avcaptureviewdelegate.md)
  The protocol that defines the methods you can implement to respond to capture view events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview/delegate)*