# init(handler:)

**Framework**: AVKit  
**Kind**: init  
**Role**: Initializer

Creates a capture event interaction with a handler that responds to presses of hardware buttons.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
init(handler: @escaping (AVCaptureEvent) -> Void)
```

```objc
- (instancetype) initWithEventHandler:(void (^)(AVCaptureEvent *event)) handler;
```

## Parameters

- `handler`: An event handler the system calls when a person performs a primary or secondary capture event.

## See Also

### Creating an interaction
- [init(primary: (AVCaptureEvent) -> Void, secondary: (AVCaptureEvent) -> Void)](./init%28primary,secondary%29.md)
  Creates a capture event interaction with handlers that respond independently to presses of hardware buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/init(handler:))*