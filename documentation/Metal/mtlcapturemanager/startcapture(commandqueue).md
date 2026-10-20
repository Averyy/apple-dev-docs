# startCapture(commandQueue:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Starts capturing any of your app’s Metal commands that are executed by the command queue.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.13+ - Deprecated in 10.15
- tvOS 11.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`startCapture(with:)`](./startcapture%28with%29.md) instead.

## Declaration

```swift
func startCapture(commandQueue: any MTLCommandQueue)
```

```objc
- (void) startCaptureWithCommandQueue:(id<MTLCommandQueue>) commandQueue;
```

## Parameters

- `commandQueue`: The command queue whose commands you want to capture.

## See Also

### Starting capture
- [func startCapture(with: MTLCaptureDescriptor) throws](./startcapture%28with%29.md)
  Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.
- [func startCapture(device: any MTLDevice)](./startcapture%28device%29.md)
  Starts capturing any of your app’s Metal commands that are executed by the device object.
- [func startCapture(scope: any MTLCaptureScope)](./startcapture%28scope%29.md)
  Starts capturing any of your app’s Metal commands that are in the specified capture scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/startcapture(commandqueue:))*