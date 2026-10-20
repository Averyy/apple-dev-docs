# sampleLocation

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The starting file offset and size in bytes of the sample.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var sampleLocation: AVSampleCursorStorageRange { get }
```

```objc
@property (nonatomic, readonly) AVSampleCursorStorageRange sampleLocation;
```

## See Also

### Inspecting a sample location
- [var byteSource: MEByteSource](./bytesource.md)
  The byte source to use to read the data for the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplelocation/samplelocation)*