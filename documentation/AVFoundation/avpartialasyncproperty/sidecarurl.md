# sidecarURL

**Framework**: AVFoundation  
**Kind**: property

The sidecar URL used by the MediaExtension. The sidecar URL is returned only if the MediaExtension format reader supports sidecar files, and implements this property [MEFileInfo setSidecarFilename:]. Will return nil otherwise.

**Availability**:
- macOS 26.0+

## Declaration

```swift
static var sidecarURL: AVAsyncProperty<Root, URL?> { get }
```

## See Also

- [var description: String](avpartialasyncproperty/description.md)
  A description of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/sidecarurl)*