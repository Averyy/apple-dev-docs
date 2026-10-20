# byteSource

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The byte source to use to read the data for the sample.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var byteSource: MEByteSource { get }
```

```objc
@property (nonatomic, retain, readonly) MEByteSource * byteSource;
```

## See Also

### Inspecting an estimated sample location
- [var estimatedSampleLocation: AVSampleCursorStorageRange](./estimatedsamplelocation.md)
  The estimated starting file offset and size in bytes of the sample.
- [var refinementDataLocation: AVSampleCursorStorageRange](./refinementdatalocation.md)
  The starting file offset and size in bytes of the data necessary to provide an accurate sample location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meestimatedsamplelocation/bytesource)*