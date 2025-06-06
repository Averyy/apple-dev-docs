# metadataOutput(_:didOutput:from:)

**Framework**: AVFoundation  
**Kind**: method

Informs the delegate that the capture output object emitted new metadata objects.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
optional func metadataOutput(_ output: AVCaptureMetadataOutput, didOutput metadataObjects: [AVMetadataObject], from connection: AVCaptureConnection)
```

#### Discussion

The [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md) object emits only metadata objects whose types are included in its [`metadataObjectTypes`](avcapturemetadataoutput/metadataobjecttypes.md) property. The delegate implements this method to perform additional processing on metadata objects as they become available. If you plan to use metadata objects outside the scope of this method, you must store strong references to them and remove those references when the objects are no longer required.

This method is executed on the dispatch queue specified by the [`metadataObjectsCallbackQueue`](avcapturemetadataoutput/metadataobjectscallbackqueue.md) property of the capture metadata output object. Because this method may be called frequently, your implementation should be efficient to prevent capture performance problems, including dropped metadata objects.

## Parameters

- `output`: The   object that captured and emitted the metadata objects.
- `metadataObjects`: An array of   instances representing the newly emitted metadata. Because   is an abstract class, the objects in this array are always instances of a concrete subclass.
- `connection`: The capture connection through which the objects were emitted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate/metadataoutput(_:didoutput:from:))*