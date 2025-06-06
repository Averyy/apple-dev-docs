# makeCaptureScope(device:)

**Framework**: Metal  
**Kind**: method

Creates a capture scope for commands submitted to a specific device object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func makeCaptureScope(device: any MTLDevice) -> any MTLCaptureScope
```

#### Discussion

The capture scope captures commands in command buffers created on any command queues created by the device object.

## Parameters

- `device`: The device object whose commands you want to capture.

## See Also

- [func makeCaptureScope(commandQueue: any MTLCommandQueue) -> any MTLCaptureScope](mtlcapturemanager/makecapturescope(commandqueue:).md)
  Creates a capture scope for commands submitted to a specific command queue.
- [var defaultCaptureScope: (any MTLCaptureScope)?](mtlcapturemanager/defaultcapturescope.md)
  The capture scope to use when a capture is initiated in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/makecapturescope(device:))*