# outputURL

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A URL for a file to write the capture data into.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var outputURL: URL? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSURL * outputURL;
```

## Discussion

The default value is `nil`. If you set [`destination`](./destination.md) to [`MTLCaptureDestination.gpuTraceDocument`](../mtlcapturedestination/gputracedocument.md), you need to set this property to where you want the file to be written to.

## See Also

### Setting capture parameters
- [var captureObject: Any?](./captureobject.md)
  The instance whose contents should be captured.
- [var destination: MTLCaptureDestination](./destination.md)
  The destination for any captured command data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturedescriptor/outputurl)*