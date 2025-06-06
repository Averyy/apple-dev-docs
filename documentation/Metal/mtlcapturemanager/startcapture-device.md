# startCapture(device:)

**Framework**: Metal  
**Kind**: method

Starts capturing any of your app’s Metal commands that are executed by the device object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func startCapture(device: any MTLDevice)
```

## Parameters

- `device`: The device object whose commands you want to capture.

## See Also

- [func startCapture(with: MTLCaptureDescriptor) throws](mtlcapturemanager/startcapture(with:).md)
  Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.
- [func startCapture(commandQueue: any MTLCommandQueue)](mtlcapturemanager/startcapture(commandqueue:).md)
  Starts capturing any of your app’s Metal commands that are executed by the command queue.
- [func startCapture(scope: any MTLCaptureScope)](mtlcapturemanager/startcapture(scope:).md)
  Starts capturing any of your app’s Metal commands that are in the specified capture scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/startcapture(device:))*