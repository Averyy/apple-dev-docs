# metadataObjectsCallbackQueue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) dispatch_queue_t metadataObjectsCallbackQueue;
```

#### Discussion

To set the dispatch queue, you must use the [`setMetadataObjectsDelegate(_:queue:)`](./setmetadataobjectsdelegate%28_,queue%29.md) method.

## See Also

### Receiving captured metadata objects
- [func setMetadataObjectsDelegate((any AVCaptureMetadataOutputObjectsDelegate)?, queue: dispatch_queue_t?)](./setmetadataobjectsdelegate%28_,queue%29.md)
  Sets the delegate and dispatch queue to use handle callbacks.
- [var metadataObjectsDelegate: (any AVCaptureMetadataOutputObjectsDelegate)?](./metadataobjectsdelegate.md)
  The delegate of the capture metadata output object.
- [protocol AVCaptureMetadataOutputObjectsDelegate](../avcapturemetadataoutputobjectsdelegate.md)
  Methods for receiving metadata produced by a metadata capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/metadataobjectscallbackqueue)*