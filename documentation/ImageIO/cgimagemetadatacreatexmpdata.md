# CGImageMetadataCreateXMPData(_:_:)

**Framework**: Image I/O  
**Kind**: func

Returns a data object that contains the metadata object’s contents serialized into the XMP format.

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
func CGImageMetadataCreateXMPData(_ metadata: CGImageMetadata, _ options: CFDictionary?) -> CFData?
```

#### Return Value

A [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object with an XMP representation of the metadata, or `NULL` if an error occurs.

#### Discussion

Use this function to create sidecar files with metadata for image formats that don’t support embedded XMP, or that you cannot edit due to other format restrictions. For example, use this function to create the data for proprietary RAW camera formats.

## Parameters

- `metadata`: The metadata object to serialize. The function converts all tags in this object to XMP data.
- `options`: Additional options for the serialization process. Options aren’t currently supported, so specify  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatacreatexmpdata(_:_:))*