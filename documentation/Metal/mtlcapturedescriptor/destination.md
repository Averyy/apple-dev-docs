# destination

**Framework**: Metal  
**Kind**: property

The destination for any captured command data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var destination: MTLCaptureDestination { get set }
```

#### Discussion

The default value is [`MTLCaptureDestination.developerTools`](mtlcapturedestination/developertools.md).

## See Also

- [var captureObject: Any?](mtlcapturedescriptor/captureobject.md)
  The object whose contents should be captured.
- [var outputURL: URL?](mtlcapturedescriptor/outputurl.md)
  A URL for a file to write the capture data into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturedescriptor/destination)*