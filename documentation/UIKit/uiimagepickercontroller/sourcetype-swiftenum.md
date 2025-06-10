# UIImagePickerController.SourceType

**Framework**: UIKit  
**Kind**: enum

Constants that describe the source to use when picking an image or when determining available media types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum SourceType
```

#### Overview

A given source may not be available on a given device because the source is not physically present or because it cannot currently be accessed.

## Topics

### Constants
- [UIImagePickerController.SourceType.camera](uiimagepickercontroller/sourcetype-swift.enum/camera.md)
  Specifies the device’s built-in camera as the source for the image picker controller.
- [UIImagePickerController.SourceType.photoLibrary](uiimagepickercontroller/sourcetype-swift.enum/photolibrary.md)
  Specifies the device’s photo library as the source for the image picker controller.
- [UIImagePickerController.SourceType.savedPhotosAlbum](uiimagepickercontroller/sourcetype-swift.enum/savedphotosalbum.md)
  Specifies the device’s Camera Roll album as the source for the image picker controller.
### Initializers
- [init?(rawValue: Int)](uiimagepickercontroller/sourcetype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func availableMediaTypes(for: UIImagePickerController.SourceType) -> [String]?](uiimagepickercontroller/availablemediatypes(for:).md)
  Retrieves the available media types for the specified source type.
- [class func isSourceTypeAvailable(UIImagePickerController.SourceType) -> Bool](uiimagepickercontroller/issourcetypeavailable(_:).md)
  Queries whether the device supports picking media using the specified source type.
- [var sourceType: UIImagePickerController.SourceType](uiimagepickercontroller/sourcetype-swift.property.md)
  The type of picker interface to be displayed by the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum)*