# dictionaryRepresentation(forAuxiliaryDataType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSDictionary *) dictionaryRepresentationForAuxiliaryDataType:(NSString **) outAuxDataType;
```

#### Discussion

When using `CGImageDestination` functions to write depth data (along with image data) to a HEIF, JPEG, or DNG file, you can use this method to obtain a dictionary of primitive depth map information, then use the [`CGImageDestinationAddAuxiliaryDataInfo(_:_:_:)`](../../ImageIO/cgimagedestinationaddauxiliarydatainfo%28_,_,_%29.md) function to embed that data into the output file.

## Parameters

- `outAuxDataType`: On output, either [`kCGImageAuxiliaryDataTypeDisparity`](../../ImageIO/kcgimageauxiliarydatatypedisparity.md) or [`kCGImageAuxiliaryDataTypeDepth`](../../ImageIO/kcgimageauxiliarydatatypedepth.md), depending on the depth data’s type.

## See Also

### Creating depth data
- [convenience init(fromDictionaryRepresentation: [AnyHashable : Any]) throws](./init%28fromdictionaryrepresentation%29.md)
  Creates a depth data object from depth information such as that found in an image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/dictionaryrepresentation(forauxiliarydatatype:))*