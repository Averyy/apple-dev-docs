# outputURL

**Framework**: Metal  
**Kind**: property

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

#### Discussion

The default value is `nil`. If you set [`destination`](mtlcapturedescriptor/destination.md) to [`MTLCaptureDestination.gpuTraceDocument`](mtlcapturedestination/gputracedocument.md), you must set this property to where you want the file to be written to.

## See Also

- [var captureObject: Any?](mtlcapturedescriptor/captureobject.md)
  The object whose contents should be captured.
- [var destination: MTLCaptureDestination](mtlcapturedescriptor/destination.md)
  The destination for any captured command data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturedescriptor/outputurl)*