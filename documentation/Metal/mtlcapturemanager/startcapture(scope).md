# startCapture(scope:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Starts capturing any of your app’s Metal commands that are in the specified capture scope.

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
func startCapture(scope captureScope: any MTLCaptureScope)
```

```objc
- (void) startCaptureWithScope:(id<MTLCaptureScope>) captureScope;
```

## Parameters

- `captureScope`: The capture scope to use.

## See Also

### Starting capture
- [func startCapture(with: MTLCaptureDescriptor) throws](./startcapture%28with%29.md)
  Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.
- [func startCapture(device: any MTLDevice)](./startcapture%28device%29.md)
  Starts capturing any of your app’s Metal commands that are executed by the device object.
- [func startCapture(commandQueue: any MTLCommandQueue)](./startcapture%28commandqueue%29.md)
  Starts capturing any of your app’s Metal commands that are executed by the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/startcapture(scope:))*