# sourceType

**Framework**: UIKit  
**Kind**: property

The type of picker interface to be displayed by the controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sourceType: UIImagePickerController.SourceType { get set }
```

#### Discussion

Prior to running the picker interface, set this value to the desired source type. The source type you set must be available and an exception is thrown if it is not. If you change this property while the picker is visible, the picker interface changes to match the new value in this property.

The various source types are listed in the [`UIImagePickerController.SourceType`](uiimagepickercontroller/sourcetype-swift.enum.md) enumeration. The default value is [`UIImagePickerController.SourceType.photoLibrary`](uiimagepickercontroller/sourcetype-swift.enum/photolibrary.md).

## See Also

- [class func availableMediaTypes(for: UIImagePickerController.SourceType) -> [String]?](uiimagepickercontroller/availablemediatypes(for:).md)
  Retrieves the available media types for the specified source type.
- [class func isSourceTypeAvailable(UIImagePickerController.SourceType) -> Bool](uiimagepickercontroller/issourcetypeavailable(_:).md)
  Queries whether the device supports picking media using the specified source type.
- [UIImagePickerController.SourceType](uiimagepickercontroller/sourcetype-swift.enum.md)
  Constants that describe the source to use when picking an image or when determining available media types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype-swift.property)*