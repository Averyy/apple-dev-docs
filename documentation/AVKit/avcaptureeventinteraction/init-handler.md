# init(handler:)

**Framework**: AVKit  
**Kind**: init

Creates a capture event interaction with a handler that responds to presses of hardware buttons.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
@MainActor
init(handler: @escaping (AVCaptureEvent) -> Void)
```

## Parameters

- `handler`: An event handler the system calls when a person performs a primary or secondary capture event.

## See Also

- [init(primary: (AVCaptureEvent) -> Void, secondary: (AVCaptureEvent) -> Void)](avcaptureeventinteraction/init(primary:secondary:).md)
  Creates a capture event interaction with handlers that respond independently to presses of hardware buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/init(handler:))*