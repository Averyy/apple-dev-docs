# CGImageMetadataCreateFromXMPData(_:)

**Framework**: Image I/O  
**Kind**: func

Creates a collection of metadata tags from the specified XMP data.

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
func CGImageMetadataCreateFromXMPData(_ data: CFData) -> CGImageMetadata?
```

#### Return Value

A [`CGImageMetadata`](cgimagemetadata.md) object that contains the parsed metadata information, or `NULL` if an error occurs. You are responsible for releasing the returned object.

#### Discussion

Use this function to parse the raw XMP data from an image and build a parseable set of metadata tags. Use the returned object to enumerate the tags or search for individual tags within the collection.

## Parameters

- `data`: An object containin XMP data. The contents of this object must represent a complete XMP tree. The XMP data may include packet headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatacreatefromxmpdata(_:))*