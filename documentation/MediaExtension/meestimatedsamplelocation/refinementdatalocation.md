# refinementDataLocation

**Framework**: MediaExtension  
**Kind**: property

The starting file offset and size in bytes of the data necessary to provide an accurate sample location.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var refinementDataLocation: AVSampleCursorStorageRange { get }
```

#### Discussion

Pass this refinement data to the [`refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)`](mesamplecursor/refinesamplelocation(_:refinementdata:refinementdatalength:refinedlocation:).md) to determine the exact sample location.

## See Also

- [var byteSource: MEByteSource](meestimatedsamplelocation/bytesource.md)
  The byte source to use to read the data for the sample.
- [var estimatedSampleLocation: AVSampleCursorStorageRange](meestimatedsamplelocation/estimatedsamplelocation.md)
  The estimated starting file offset and size in bytes of the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meestimatedsamplelocation/refinementdatalocation)*