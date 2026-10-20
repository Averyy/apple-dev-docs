# CGImageMetadataTagGetType(_:)

**Framework**: Image I/O  
**Kind**: func

Returns the type of the metadata tag’s value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageMetadataTagGetType(_ tag: CGImageMetadataTag) -> CGImageMetadataType
```

#### Return Value

A constant that indicates the type of the value. For a list of possible return values, see [`CGImageMetadataType`](cgimagemetadatatype.md).

#### Discussion

To get the value itself, call [`CGImageMetadataTagCopyValue(_:)`](cgimagemetadatatagcopyvalue(_:).md). Metadata tags store string, number, and Boolean values using the [`CGImageMetadataType.string`](cgimagemetadatatype/string.md) type.

## Parameters

- `tag`: The metadata tag from which to fetch the namespace information.

## See Also

- [enum CGImageMetadataType](cgimagemetadatatype.md)
  Constants that indicate the XMP type for a metadata tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatataggettype(_:))*