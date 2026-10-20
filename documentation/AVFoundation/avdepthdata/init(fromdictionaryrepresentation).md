# init(fromDictionaryRepresentation:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) depthDataFromDictionaryRepresentation:(NSDictionary *) imageSourceAuxDataInfoDictionary error:(NSError **) outError;
```

## Mentions

- [Creating auxiliary depth data manually](../creating-auxiliary-depth-data-manually.md)

#### Discussion

When using `CGImageSource` functions to read from a HEIF, JPEG, or DNG file containing depth data (as well as image data), you can use the  [`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](../../ImageIO/cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md) function to load primitive depth map information, then use this initializer to create an [`AVDepthData`](../avdepthdata.md) object, as shown below.

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

- `imageSourceAuxDataInfoDictionary`: A dictionary of primitive depth-related information, in the format provided by the  [`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](../../ImageIO/cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md) function.

## See Also

### Creating depth data
- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](./dictionaryrepresentation%28forauxiliarydatatype%29.md)
  Returns a dictionary representation of the depth data suitable for writing into an image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/init(fromdictionaryrepresentation:))*