# metadataObjectsDelegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The delegate of the capture metadata output object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var metadataObjectsDelegate: (any AVCaptureMetadataOutputObjectsDelegate)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<AVCaptureMetadataOutputObjectsDelegate> metadataObjectsDelegate;
```

#### Discussion

The delegate object must conform to the [`AVCaptureMetadataOutputObjectsDelegate`](../avcapturemetadataoutputobjectsdelegate.md) protocol. The object in this property is used to process all metadata objects captured from the capture metadata output object’s connection.

To set the delegate object, you must use the [`setMetadataObjectsDelegate(_:queue:)`](./setmetadataobjectsdelegate%28_,queue%29.md) method.

## See Also

### Receiving captured metadata objects
- [func setMetadataObjectsDelegate((any AVCaptureMetadataOutputObjectsDelegate)?, queue: dispatch_queue_t?)](./setmetadataobjectsdelegate%28_,queue%29.md)
  Sets the delegate and dispatch queue to use handle callbacks.
- [var metadataObjectsCallbackQueue: dispatch_queue_t?](./metadataobjectscallbackqueue.md)
  The dispatch queue on which to execute the delegate’s methods.
- [protocol AVCaptureMetadataOutputObjectsDelegate](../avcapturemetadataoutputobjectsdelegate.md)
  Methods for receiving metadata produced by a metadata capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/metadataobjectsdelegate)*