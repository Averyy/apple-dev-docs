# activityViewController(_:thumbnailImageForActivityType:suggestedSize:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

For activities that support a preview image, returns a thumbnail preview image for the item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func activityViewController(_ activityViewController: UIActivityViewController, thumbnailImageForActivityType activityType: UIActivity.ActivityType?, suggestedSize size: CGSize) -> UIImage?
```

```objc
- (UIImage *) activityViewController:(UIActivityViewController *) activityViewController thumbnailImageForActivityType:(UIActivityType) activityType suggestedSize:(CGSize) size;
```

#### Return Value

The image to use as a preview for the item.

## Parameters

- `activityViewController`: The activity view controller object requesting information about the data item.
- `activityType`: The selected activity type.
- `size`: The suggested size for the thumbnail image, in points. You should provide an image using the appropriate [`scale`](../uiscreen/scale.md) for the screen. Images provided at the suggested size will result in the best experience.

## See Also

### Providing information about the data items
- [func activityViewController(UIActivityViewController, subjectForActivityType: UIActivity.ActivityType?) -> String](./activityviewcontroller%28_,subjectforactivitytype%29.md)
  For activities that support a subject field, returns the subject for the item.
- [func activityViewController(UIActivityViewController, dataTypeIdentifierForActivityType: UIActivity.ActivityType?) -> String](./activityviewcontroller%28_,datatypeidentifierforactivitytype%29.md)
  For items that are provided as data, returns the UTI for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:thumbnailimageforactivitytype:suggestedsize:))*