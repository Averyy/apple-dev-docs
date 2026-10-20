# availableRawPhotoFileTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The list of file types currently supported for RAW format capture and output.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var availableRawPhotoFileTypes: [AVFileType] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availableRawPhotoFileTypes;
```

#### Discussion

When you issue a photo capture request, you can separately specify the format for capturing or encoding image data and the container format for producing output files containing that data. However, each file type supports only a specific set of image data types.

After choosing an output file type, use the [`supportedRawPhotoPixelFormatTypesForFileType:`](./supportedrawphotopixelformattypesforfiletype_.md) method to choose an appropriate data format before creating a photo settings object.

## See Also

### Determining supported file types
- [var availablePhotoFileTypes: [AVFileType]](./availablephotofiletypes.md)
  The list of file types currently supported for photo capture and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablerawphotofiletypes)*