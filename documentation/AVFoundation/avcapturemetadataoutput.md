# AVCaptureMetadataOutput

**Framework**: AVFoundation  
**Kind**: class

A capture output for processing timed metadata produced by a capture session.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureMetadataOutput
```

#### Overview

An `AVCaptureMetadataOutput` object intercepts metadata objects emitted by its associated capture connection and forwards them to a delegate object for processing. You can use instances of this class to process specific types of metadata included with the input data. You use this class the way you do other output objects, typically by adding it as an output to an [`AVCaptureSession`](avcapturesession.md) object.

## Topics

### Configuring Metadata Capture
- [var availableMetadataObjectTypes: [AVMetadataObject.ObjectType]](avcapturemetadataoutput/availablemetadataobjecttypes.md)
  An array of strings identifying the types of metadata objects that can be captured.
- [var metadataObjectTypes: [AVMetadataObject.ObjectType]!](avcapturemetadataoutput/metadataobjecttypes.md)
  An array of strings identifying the types of metadata objects  to process.
- [var rectOfInterest: CGRect](avcapturemetadataoutput/rectofinterest.md)
  A rectangle of interest for limiting the search area for visual metadata.
### Receiving Captured Metadata Objects
- [func setMetadataObjectsDelegate((any AVCaptureMetadataOutputObjectsDelegate)?, queue: dispatch_queue_t?)](avcapturemetadataoutput/setmetadataobjectsdelegate(_:queue:).md)
  Sets the delegate and dispatch queue to use handle callbacks.
- [var metadataObjectsDelegate: (any AVCaptureMetadataOutputObjectsDelegate)?](avcapturemetadataoutput/metadataobjectsdelegate.md)
  The delegate of the capture metadata output object.
- [var metadataObjectsCallbackQueue: dispatch_queue_t?](avcapturemetadataoutput/metadataobjectscallbackqueue.md)
  The dispatch queue on which to execute the delegate’s methods.
- [protocol AVCaptureMetadataOutputObjectsDelegate](avcapturemetadataoutputobjectsdelegate.md)
  Methods for receiving metadata produced by a metadata capture output.
### Creating Metadata Output
- [init()](avcapturemetadataoutput/init.md)
  Creates a new capture metadata output.

## Relationships

### Inherits From
- [AVCaptureOutput](avcaptureoutput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCaptureMetadataInput](avcapturemetadatainput.md)
  A capture input for providing timed metadata to a capture session.
- [class AVMetadataObject](avmetadataobject.md)
  The abstract superclass for objects provided by a metadata capture output.
- [Metadata Types](metadata-types.md)
  Inspect the supported metadata object types that the framework supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput)*