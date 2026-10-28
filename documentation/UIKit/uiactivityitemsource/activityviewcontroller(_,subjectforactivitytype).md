# activityViewController(_:subjectForActivityType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

For activities that support a subject field, returns the subject for the item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func activityViewController(_ activityViewController: UIActivityViewController, subjectForActivityType activityType: UIActivity.ActivityType?) -> String
```

```objc
- (NSString *) activityViewController:(UIActivityViewController *) activityViewController subjectForActivityType:(UIActivityType) activityType;
```

## Return Value

A string to use as the contents of the subject field.

## Discussion

When posting an item the service may provide for a separate subject field and data field, such as an email message. Implement this method if you wish to provide a subject field for services that support one.

## Parameters

- `activityViewController`: The activity view controller object requesting information about the data item.
- `activityType`: The selected activity type; may be `nil`.

## See Also

### Providing information about the data items
- [func activityViewController(UIActivityViewController, dataTypeIdentifierForActivityType: UIActivity.ActivityType?) -> String](./activityviewcontroller%28_,datatypeidentifierforactivitytype%29.md)
  For items that are provided as data, returns the UTI for the item.
- [func activityViewController(UIActivityViewController, thumbnailImageForActivityType: UIActivity.ActivityType?, suggestedSize: CGSize) -> UIImage?](./activityviewcontroller%28_,thumbnailimageforactivitytype,suggestedsize%29.md)
  For activities that support a preview image, returns a thumbnail preview image for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:subjectforactivitytype:))*