# CGImageMetadataCreateMutable()

**Framework**: Image I/O  
**Kind**: func

Creates an empty, mutable image metdata opaque type.

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
func CGImageMetadataCreateMutable() -> CGMutableImageMetadata
```

#### Return Value

A [`CGMutableImageMetadata`](cgmutableimagemetadata.md) object that contains no metadata information, or `NULL` if an error occurs. You are responsible for releasing the returned object.

## See Also

- [func CGImageMetadataCreateMutableCopy(CGImageMetadata) -> CGMutableImageMetadata?](cgimagemetadatacreatemutablecopy(_:).md)
  Creates a deep, mutable copy of the specified metadata information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatacreatemutable())*