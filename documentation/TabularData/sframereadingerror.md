# SFrameReadingError

**Framework**: TabularData  
**Kind**: enum

An error when reading a Turi Create scalable data frame.

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
enum SFrameReadingError
```

## Topics

### Getting Error Information
- [SFrameReadingError.badArchive(_:)](sframereadingerror/badarchive(_:).md)
  An error that indicates the scalable data frame directory’s archive file is corrupt.
- [SFrameReadingError.badEncoding(_:)](sframereadingerror/badencoding(_:).md)
  An error that indicates the scalable data frame contains bad data encoding.
- [SFrameReadingError.missingArchive](sframereadingerror/missingarchive.md)
  An error that indicates the scalable data frame directory is missing an archive file.
- [SFrameReadingError.missingColumn(_:)](sframereadingerror/missingcolumn(_:).md)
  An error that indicates the scalable data frame is missing one of the requested columns.
- [SFrameReadingError.unsupportedArchive(_:)](sframereadingerror/unsupportedarchive(_:).md)
  An error that indicates the scalable data frame contains an archive version or layout the framework doesn’t support.
- [SFrameReadingError.unsupportedLayout(_:)](sframereadingerror/unsupportedlayout(_:).md)
  An error that indicates the scalable data frame contains an unsupported data layout.
- [SFrameReadingError.unsupportedType(_:)](sframereadingerror/unsupportedtype(_:).md)
  An error that indicates the scalable data frame contains an unknown or unsupported data type.
### Default Implementations
- [CustomStringConvertible Implementations](sframereadingerror/customstringconvertible-implementations.md)
- [LocalizedError Implementations](sframereadingerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum JSONReadingError](jsonreadingerror.md)
  A JSON reading error.
- [enum CSVReadingError](csvreadingerror.md)
  A CSV reading error.
- [enum CSVWritingError](csvwritingerror.md)
  A CSV writing error.
- [struct ColumnDecodingError](columndecodingerror.md)
  A column decoding error.
- [struct ColumnEncodingError](columnencodingerror.md)
  A column encoding error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/sframereadingerror)*