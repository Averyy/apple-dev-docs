# UIImagePickerController.SourceType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the source to use when picking an image or when determining available media types.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
enum SourceType
```

```c
enum UIImagePickerControllerSourceType : NSInteger;
```

#### Overview

A given source may not be available on a given device because the source is not physically present or because it cannot currently be accessed.

## Topics

### Constants
- [UIImagePickerController.SourceType.camera](./sourcetype-swift.enum/camera.md)
  Specifies the device’s built-in camera as the source for the image picker controller.
- [UIImagePickerController.SourceType.photoLibrary](./sourcetype-swift.enum/photolibrary.md)
  Specifies the device’s photo library as the source for the image picker controller.
- [UIImagePickerController.SourceType.savedPhotosAlbum](./sourcetype-swift.enum/savedphotosalbum.md)
  Specifies the device’s Camera Roll album as the source for the image picker controller.
### Initializers
- [init?(rawValue: Int)](./sourcetype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting the picker source
- [class func availableMediaTypes(for: UIImagePickerController.SourceType) -> [String]?](./availablemediatypes%28for%29.md)
  Retrieves the available media types for the specified source type.
- [class func isSourceTypeAvailable(UIImagePickerController.SourceType) -> Bool](./issourcetypeavailable%28_%29.md)
  Queries whether the device supports picking media using the specified source type.
- [var sourceType: UIImagePickerController.SourceType](./sourcetype-swift.property.md)
  The type of picker interface to be displayed by the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum)*