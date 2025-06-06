# delegate

**Framework**: AVKit  
**Kind**: property

The capture view’s delegate object.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
weak var delegate: (any AVCaptureViewDelegate)? { get set }
```

#### Discussion

The capture view disables the start recording button if you don’t provide a delegate object.

## See Also

- [protocol AVCaptureViewDelegate](avcaptureviewdelegate.md)
  The protocol that defines the methods you can implement to respond to capture view events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview/delegate)*