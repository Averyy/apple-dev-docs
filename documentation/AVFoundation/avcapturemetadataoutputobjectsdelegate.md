# AVCaptureMetadataOutputObjectsDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Methods for receiving metadata produced by a metadata capture output.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
protocol AVCaptureMetadataOutputObjectsDelegate : NSObjectProtocol
```

#### Overview

The `AVCaptureMetadataOutputObjectsDelegate` protocol must be adopted by the delegate of an [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md) object. The single method in this protocol is optional. The method allows a delegate to respond when a capture metadata output object receives relevant metadata objects through its connection.

The [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md) object calls the methods of the delegate object on the dispatch queue associated with its [`metadataObjectsCallbackQueue`](avcapturemetadataoutput/metadataobjectscallbackqueue.md) property.

## Topics

### Processing Emitted Metadata Objects
- [func metadataOutput(AVCaptureMetadataOutput, didOutput: [AVMetadataObject], from: AVCaptureConnection)](avcapturemetadataoutputobjectsdelegate/metadataoutput(_:didoutput:from:).md)
  Informs the delegate that the capture output object emitted new metadata objects.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func setMetadataObjectsDelegate((any AVCaptureMetadataOutputObjectsDelegate)?, queue: dispatch_queue_t?)](avcapturemetadataoutput/setmetadataobjectsdelegate(_:queue:).md)
  Sets the delegate and dispatch queue to use handle callbacks.
- [var metadataObjectsDelegate: (any AVCaptureMetadataOutputObjectsDelegate)?](avcapturemetadataoutput/metadataobjectsdelegate.md)
  The delegate of the capture metadata output object.
- [var metadataObjectsCallbackQueue: dispatch_queue_t?](avcapturemetadataoutput/metadataobjectscallbackqueue.md)
  The dispatch queue on which to execute the delegate’s methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate)*