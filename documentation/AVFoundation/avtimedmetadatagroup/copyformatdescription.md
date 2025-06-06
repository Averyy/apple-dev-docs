# copyFormatDescription()

**Framework**: AVFoundation  
**Kind**: method

Creates a format description based on the receiver’s items.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func copyFormatDescription() -> CMMetadataFormatDescription?
```

#### Return Value

An instance of [`CMMetadataFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMMetadataFormatDescription) sufficient to describe the contents of all the items referenced by the object.

#### Discussion

The returned format description is suitable for use as the format hint parameter when creating an instance of [`AVAssetWriterInput`](avassetwriterinput.md).

Each item referenced by the receiver must carry a non-`nil` value for its `dataType` property.  An exception will be thrown if any item does not have a data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/copyformatdescription())*