# init(fromDictionaryRepresentation:)

**Framework**: AVFoundation  
**Kind**: init

Creates a depth data object from depth information such as that found in an image file.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(fromDictionaryRepresentation imageSourceAuxDataInfoDictionary: [AnyHashable : Any]) throws
```

## Mentions

- [Creating Auxiliary Depth Data Manually](creating-auxiliary-depth-data-manually.md)

#### Discussion

When using `CGImageSource` functions to read from a HEIF, JPEG, or DNG file containing depth data (as well as image data), you can use the  [`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](https://developer.apple.com/documentation/ImageIO/CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)) function to load primitive depth map information, then use this initializer to create an [`AVDepthData`](avdepthdata.md) object, as shown below.

```swift
- (nullable AVDepthData *)depthDataFromImageData:(nonnull NSData *)imageData {
	AVDepthData *depthData = nil;

    CGImageSourceRef imageSource = CGImageSourceCreateWithData((CFDataRef)imageData, NULL);
	if (imageSource) {
		NSDictionary *auxDataDictionary = (__bridge NSDictionary *)CGImageSourceCopyAuxiliaryDataInfoAtIndex(imageSource, 0, kCGImageAuxiliaryDataTypeDisparity);
		if (auxDataDictionary) {
			depthData = [AVDepthData depthDataFromDictionaryRepresentation:auxDataDictionary error:NULL];
		}

		CFRelease(imageSource);
	}

    return depthData;
}
```

## Parameters

- `imageSourceAuxDataInfoDictionary`: A dictionary of primitive depth-related information, in the format provided by the    function.

## See Also

- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](avdepthdata/dictionaryrepresentation(forauxiliarydatatype:).md)
  Returns a dictionary representation of the depth data suitable for writing into an image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/init(fromdictionaryrepresentation:))*