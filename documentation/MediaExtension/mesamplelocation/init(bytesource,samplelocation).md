# init(byteSource:sampleLocation:)

**Framework**: MediaExtension  
**Kind**: init  
**Role**: Initializer

Creates a sample location object with the byte source and sample location that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(byteSource: MEByteSource, sampleLocation: AVSampleCursorStorageRange)
```

```objc
- (instancetype) initWithByteSource:(MEByteSource *) byteSource sampleLocation:(AVSampleCursorStorageRange) sampleLocation;
```

## Parameters

- `byteSource`: The byte source to use to read the data for the sample.
- `sampleLocation`: The starting file offset and size in bytes of the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplelocation/init(bytesource:samplelocation:))*