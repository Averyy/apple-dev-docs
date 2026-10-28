# SFrameReadingError.unsupportedType(_:)

**Framework**: TabularData  
**Kind**: case  
**Role**: Case

An error that indicates the scalable data frame contains an unknown or unsupported data type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case unsupportedType(Int)
```

## Discussion

The associated value contains the unknown data type identifier.

## See Also

### Getting Error Information
- [SFrameReadingError.badArchive(_:)](./badarchive%28_%29.md)
  An error that indicates the scalable data frame directory’s archive file is corrupt.
- [SFrameReadingError.badEncoding(_:)](./badencoding%28_%29.md)
  An error that indicates the scalable data frame contains bad data encoding.
- [SFrameReadingError.missingArchive](./missingarchive.md)
  An error that indicates the scalable data frame directory is missing an archive file.
- [SFrameReadingError.missingColumn(_:)](./missingcolumn%28_%29.md)
  An error that indicates the scalable data frame is missing one of the requested columns.
- [SFrameReadingError.unsupportedArchive(_:)](./unsupportedarchive%28_%29.md)
  An error that indicates the scalable data frame contains an archive version or layout the framework doesn’t support.
- [SFrameReadingError.unsupportedLayout(_:)](./unsupportedlayout%28_%29.md)
  An error that indicates the scalable data frame contains an unsupported data layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/sframereadingerror/unsupportedtype(_:))*