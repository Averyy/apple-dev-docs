# startCapture(with:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) startCaptureWithDescriptor:(MTLCaptureDescriptor *) descriptor error:(NSError **) error;
```

## Parameters

- `descriptor`: A description of the capture session to create.

## See Also

### Starting capture
- [func startCapture(device: any MTLDevice)](./startcapture%28device%29.md)
  Starts capturing any of your app’s Metal commands that are executed by the device object.
- [func startCapture(commandQueue: any MTLCommandQueue)](./startcapture%28commandqueue%29.md)
  Starts capturing any of your app’s Metal commands that are executed by the command queue.
- [func startCapture(scope: any MTLCaptureScope)](./startcapture%28scope%29.md)
  Starts capturing any of your app’s Metal commands that are in the specified capture scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/startcapture(with:))*