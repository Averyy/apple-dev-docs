# init(primary:secondary:)

**Framework**: AVKit  
**Kind**: init  
**Role**: Initializer

Creates a capture event interaction with handlers that respond independently to presses of hardware buttons.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
init(primary primaryHandler: @escaping (AVCaptureEvent) -> Void, secondary secondaryHandler: @escaping (AVCaptureEvent) -> Void)
```

```objc
- (instancetype) initWithPrimaryEventHandler:(void (^)(AVCaptureEvent *event)) primaryHandler secondaryEventHandler:(void (^)(AVCaptureEvent *event)) secondaryHandler;
```

## Parameters

- `primaryHandler`: An event handler the system calls when a person performs a primary capture event.
- `secondaryHandler`: An event handler the system calls when a person performs a secondary capture event.

## See Also

### Creating an interaction
- [init(handler: (AVCaptureEvent) -> Void)](./init%28handler%29.md)
  Creates a capture event interaction with a handler that responds to presses of hardware buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/init(primary:secondary:))*