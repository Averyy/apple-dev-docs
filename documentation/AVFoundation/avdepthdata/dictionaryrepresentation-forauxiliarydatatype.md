# dictionaryRepresentation(forAuxiliaryDataType:)

**Framework**: AVFoundation  
**Kind**: method

Returns a dictionary representation of the depth data suitable for writing into an image file.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func dictionaryRepresentation(forAuxiliaryDataType outAuxDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?
```

#### Discussion

When using `CGImageDestination` functions to write depth data (along with image data) to a HEIF, JPEG, or DNG file, you can use this method to obtain a dictionary of primitive depth map information, then use the [`CGImageDestinationAddAuxiliaryDataInfo(_:_:_:)`](https://developer.apple.com/documentation/ImageIO/CGImageDestinationAddAuxiliaryDataInfo(_:_:_:)) function to embed that data into the output file.

## Parameters

- `outAuxDataType`: On output, either   or  , depending on the depth data’s type.

## See Also

- [convenience init(fromDictionaryRepresentation: [AnyHashable : Any]) throws](avdepthdata/init(fromdictionaryrepresentation:).md)
  Creates a depth data object from depth information such as that found in an image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/dictionaryrepresentation(forauxiliarydatatype:))*