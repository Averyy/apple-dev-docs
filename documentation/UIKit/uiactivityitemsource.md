# UIActivityItemSource

**Framework**: UIKit  
**Kind**: protocol

A set of methods that an activity view controller uses to retrieve the data items to act on.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol UIActivityItemSource : NSObjectProtocol
```

#### Overview

You can use this protocol in situations where you want to provide the data from one of your app’s existing objects instead of creating a separate [`UIActivityItemProvider`](uiactivityitemprovider.md) object. When implementing this protocol, your object becomes the data provider, providing the view controller with access to the items.

Because the methods of this protocol are executed on your app’s main thread, you should avoid using this protocol in cases where the data objects might take a significant amount of time to create. When creating large data objects, consider using a [`UIActivityItemProvider`](uiactivityitemprovider.md) object instead.

## Topics

### Getting the data items
- [func activityViewControllerPlaceholderItem(UIActivityViewController) -> Any](uiactivityitemsource/activityviewcontrollerplaceholderitem(_:).md)
  Returns the placeholder object for the data.
- [func activityViewController(UIActivityViewController, itemForActivityType: UIActivity.ActivityType?) -> Any?](uiactivityitemsource/activityviewcontroller(_:itemforactivitytype:).md)
  Returns the data object to be acted upon.
### Providing information about the data items
- [func activityViewController(UIActivityViewController, subjectForActivityType: UIActivity.ActivityType?) -> String](uiactivityitemsource/activityviewcontroller(_:subjectforactivitytype:).md)
  For activities that support a subject field, returns the subject for the item.
- [func activityViewController(UIActivityViewController, dataTypeIdentifierForActivityType: UIActivity.ActivityType?) -> String](uiactivityitemsource/activityviewcontroller(_:datatypeidentifierforactivitytype:).md)
  For items that are provided as data, returns the UTI for the item.
- [func activityViewController(UIActivityViewController, thumbnailImageForActivityType: UIActivity.ActivityType?, suggestedSize: CGSize) -> UIImage?](uiactivityitemsource/activityviewcontroller(_:thumbnailimageforactivitytype:suggestedsize:).md)
  For activities that support a preview image, returns a thumbnail preview image for the item.
### Providing metadata for accelerated previews
- [func activityViewControllerLinkMetadata(UIActivityViewController) -> LPLinkMetadata?](uiactivityitemsource/activityviewcontrollerlinkmetadata(_:).md)
  Returns metadata to display in the preview header of the share sheet.
### Instance Methods
- [func activityViewControllerShareRecipients(UIActivityViewController) -> [INPerson]](uiactivityitemsource/activityviewcontrollersharerecipients(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIActivityItemProvider](uiactivityitemprovider.md)

## See Also

- [class UIActivity](uiactivity.md)
  An abstract class that you subclass to implement app-specific services.
- [class UIActivityViewController](uiactivityviewcontroller.md)
  A view controller that you use to offer standard services from your app.
- [class UIActivityItemProvider](uiactivityitemprovider.md)
  A proxy for data that passes to an activity view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsource)*