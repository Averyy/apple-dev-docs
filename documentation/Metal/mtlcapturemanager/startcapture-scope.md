# startCapture(scope:)

**Framework**: Metal  
**Kind**: method

Starts capturing any of your app’s Metal commands that are in the specified capture scope.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func startCapture(scope captureScope: any MTLCaptureScope)
```

## Parameters

- `captureScope`: The capture scope to use.

## See Also

- [func startCapture(with: MTLCaptureDescriptor) throws](mtlcapturemanager/startcapture(with:).md)
  Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.
- [func startCapture(device: any MTLDevice)](mtlcapturemanager/startcapture(device:).md)
  Starts capturing any of your app’s Metal commands that are executed by the device object.
- [func startCapture(commandQueue: any MTLCommandQueue)](mtlcapturemanager/startcapture(commandqueue:).md)
  Starts capturing any of your app’s Metal commands that are executed by the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/startcapture(scope:))*