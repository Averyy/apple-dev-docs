# availableMediaTypes(for:)

**Framework**: UIKit  
**Kind**: method

Retrieves the available media types for the specified source type.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func availableMediaTypes(for sourceType: UIImagePickerController.SourceType) -> [String]?
```

#### Return Value

An array whose elements identify the available media types for the specified source type.

#### Discussion

Some iOS devices support video recording. Use this method, along with the [`isSourceTypeAvailable(_:)`](uiimagepickercontroller/issourcetypeavailable(_:).md) method, to determine if video recording is available on a device. The availability of video recording is indicated by the presence of the `kUTTypeMovie` media type for the [`UIImagePickerController.SourceType.camera`](uiimagepickercontroller/sourcetype-swift.enum/camera.md) source type.

## Parameters

- `sourceType`: The source to use to pick an image.

## See Also

- [class func isSourceTypeAvailable(UIImagePickerController.SourceType) -> Bool](uiimagepickercontroller/issourcetypeavailable(_:).md)
  Queries whether the device supports picking media using the specified source type.
- [var sourceType: UIImagePickerController.SourceType](uiimagepickercontroller/sourcetype-swift.property.md)
  The type of picker interface to be displayed by the controller.
- [UIImagePickerController.SourceType](uiimagepickercontroller/sourcetype-swift.enum.md)
  Constants that describe the source to use when picking an image or when determining available media types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/availablemediatypes(for:))*