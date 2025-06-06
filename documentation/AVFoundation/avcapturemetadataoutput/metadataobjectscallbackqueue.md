# metadataObjectsCallbackQueue

**Framework**: AVFoundation  
**Kind**: property

The dispatch queue on which to execute the delegate’s methods.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var metadataObjectsCallbackQueue: dispatch_queue_t? { get }
```

#### Discussion

To set the dispatch queue, you must use the [`setMetadataObjectsDelegate(_:queue:)`](avcapturemetadataoutput/setmetadataobjectsdelegate(_:queue:).md) method.

## See Also

- [func setMetadataObjectsDelegate((any AVCaptureMetadataOutputObjectsDelegate)?, queue: dispatch_queue_t?)](avcapturemetadataoutput/setmetadataobjectsdelegate(_:queue:).md)
  Sets the delegate and dispatch queue to use handle callbacks.
- [var metadataObjectsDelegate: (any AVCaptureMetadataOutputObjectsDelegate)?](avcapturemetadataoutput/metadataobjectsdelegate.md)
  The delegate of the capture metadata output object.
- [protocol AVCaptureMetadataOutputObjectsDelegate](avcapturemetadataoutputobjectsdelegate.md)
  Methods for receiving metadata produced by a metadata capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/metadataobjectscallbackqueue)*