# refinementDataLocation

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The starting file offset and size in bytes of the data necessary to provide an accurate sample location.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var refinementDataLocation: AVSampleCursorStorageRange { get }
```

```objc
@property (nonatomic, readonly) AVSampleCursorStorageRange refinementDataLocation;
```

## Discussion

Pass this refinement data to the [`refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)`](../mesamplecursor/refinesamplelocation%28_,refinementdata,refinementdatalength,refinedlocation%29.md) to determine the exact sample location.

## See Also

### Inspecting an estimated sample location
- [var byteSource: MEByteSource](./bytesource.md)
  The byte source to use to read the data for the sample.
- [var estimatedSampleLocation: AVSampleCursorStorageRange](./estimatedsamplelocation.md)
  The estimated starting file offset and size in bytes of the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meestimatedsamplelocation/refinementdatalocation)*