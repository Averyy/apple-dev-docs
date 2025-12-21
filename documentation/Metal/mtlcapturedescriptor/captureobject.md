# captureObject

**Framework**: Metal  
**Kind**: property

The instance whose contents should be captured.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var captureObject: Any? { get set }
```

#### Discussion

The default value is `nil`, but you need to set an instance before using this descriptor to start a capture session.

The behavior of the capture session depends on the kind of instance being captured:

- Specify an [`MTLDevice`](mtldevice.md) instance to capture commands in command buffers created on any command queues created by the device instance.
- Specify an [`MTLCommandQueue`](mtlcommandqueue.md) instance to capture commands in command buffers created by a specific command queue.
- Specify an [`MTLCaptureScope`](mtlcapturescope.md) instance to indirectly define which commands are captured.

## See Also

- [var destination: MTLCaptureDestination](mtlcapturedescriptor/destination.md)
  The destination for any captured command data.
- [var outputURL: URL?](mtlcapturedescriptor/outputurl.md)
  A URL for a file to write the capture data into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturedescriptor/captureobject)*