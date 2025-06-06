# init(byteSource:estimatedSampleLocation:refinementDataLocation:)

**Framework**: MediaExtension  
**Kind**: init

Creates an estimated sample location object with the byte source, sample location, and data location that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(byteSource: MEByteSource, estimatedSampleLocation: AVSampleCursorStorageRange, refinementDataLocation: AVSampleCursorStorageRange)
```

## Parameters

- `byteSource`: The byte source to use to read the data for the sample.
- `estimatedSampleLocation`: The estimated starting file offset and size in bytes of the sample.
- `refinementDataLocation`: The starting file offset and size in bytes of the data necessary to provide an accurate sample location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meestimatedsamplelocation/init(bytesource:estimatedsamplelocation:refinementdatalocation:))*