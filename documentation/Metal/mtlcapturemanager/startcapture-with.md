# startCapture(with:)

**Framework**: Metal  
**Kind**: method

Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func startCapture(with descriptor: MTLCaptureDescriptor) throws
```

## Parameters

- `descriptor`: A description of the capture session to create.

## See Also

- [func startCapture(device: any MTLDevice)](mtlcapturemanager/startcapture(device:).md)
  Starts capturing any of your app’s Metal commands that are executed by the device object.
- [func startCapture(commandQueue: any MTLCommandQueue)](mtlcapturemanager/startcapture(commandqueue:).md)
  Starts capturing any of your app’s Metal commands that are executed by the command queue.
- [func startCapture(scope: any MTLCaptureScope)](mtlcapturemanager/startcapture(scope:).md)
  Starts capturing any of your app’s Metal commands that are in the specified capture scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/startcapture(with:))*