# makeCaptureScope(commandQueue:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a capture scope for commands submitted to a specific command queue.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func makeCaptureScope(commandQueue: any MTLCommandQueue) -> any MTLCaptureScope
```

```objc
- (id<MTLCaptureScope>) newCaptureScopeWithCommandQueue:(id<MTLCommandQueue>) commandQueue;
```

## Parameters

- `commandQueue`: The command queue whose commands you want to capture.

## See Also

### Creating a capture scope
- [func makeCaptureScope(device: any MTLDevice) -> any MTLCaptureScope](./makecapturescope%28device%29.md)
  Creates a capture scope for commands submitted to a specific device object.
- [var defaultCaptureScope: (any MTLCaptureScope)?](./defaultcapturescope.md)
  The capture scope to use when a capture is initiated in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/makecapturescope(commandqueue:)-1rozd)*