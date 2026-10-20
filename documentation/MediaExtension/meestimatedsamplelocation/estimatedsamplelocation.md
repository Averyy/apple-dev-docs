# estimatedSampleLocation

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The estimated starting file offset and size in bytes of the sample.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var estimatedSampleLocation: AVSampleCursorStorageRange { get }
```

```objc
@property (nonatomic, readonly) AVSampleCursorStorageRange estimatedSampleLocation;
```

## See Also

### Inspecting an estimated sample location
- [var byteSource: MEByteSource](./bytesource.md)
  The byte source to use to read the data for the sample.
- [var refinementDataLocation: AVSampleCursorStorageRange](./refinementdatalocation.md)
  The starting file offset and size in bytes of the data necessary to provide an accurate sample location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meestimatedsamplelocation/estimatedsamplelocation)*