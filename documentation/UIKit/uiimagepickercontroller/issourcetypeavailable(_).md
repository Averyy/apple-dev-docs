# isSourceTypeAvailable(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Queries whether the device supports picking media using the specified source type.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func isSourceTypeAvailable(_ sourceType: UIImagePickerController.SourceType) -> Bool
```

```objc
+ (BOOL) isSourceTypeAvailable:(UIImagePickerControllerSourceType) sourceType;
```

## Return Value

[`true`](../../Swift/true.md) if the device supports the specified source type; [`false`](../../Swift/false.md) if the specified source type is not available.

## Discussion

Because a media source may not be present or may be unavailable, devices may not always support all source types. For example, if you attempt to pick an image from the user’s library and the library is empty, this method returns [`false`](../../Swift/false.md). Similarly, if the camera is already in use, this method returns [`false`](../../Swift/false.md).

Before attempting to use an `UIImagePickerController` object to pick an image, you must call this method to ensure that the desired source type is available.

## Parameters

- `sourceType`: The source to use to pick an image or movie.

## See Also

### Setting the picker source
- [class func availableMediaTypes(for: UIImagePickerController.SourceType) -> [String]?](./availablemediatypes%28for%29.md)
  Retrieves the available media types for the specified source type.
- [var sourceType: UIImagePickerController.SourceType](./sourcetype-swift.property.md)
  The type of picker interface to be displayed by the controller.
- [UIImagePickerController.SourceType](./sourcetype-swift.enum.md)
  Constants that describe the source to use when picking an image or when determining available media types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/issourcetypeavailable(_:))*