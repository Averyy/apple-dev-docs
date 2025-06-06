# CGImageMetadataCreateMutableCopy(_:)

**Framework**: Image I/O  
**Kind**: func

Creates a deep, mutable copy of the specified metadata information.

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
func CGImageMetadataCreateMutableCopy(_ metadata: CGImageMetadata) -> CGMutableImageMetadata?
```

#### Return Value

A new [`CGMutableImageMetadata`](cgmutableimagemetadata.md) type that contains a deep copy of the tags in the metadata parameter.

#### Discussion

Typically, you call this function before modifying the metadata information for an image. Use it to create a copy of the image’s existing metadata information, and then add or modify that metadata before saving it with the image.

## Parameters

- `metadata`: The metadata information to copy. This function makes a deep copy of all   structures in this parameter, including the values for the tags.

## See Also

- [func CGImageMetadataCreateMutable() -> CGMutableImageMetadata](cgimagemetadatacreatemutable().md)
  Creates an empty, mutable image metdata opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatacreatemutablecopy(_:))*