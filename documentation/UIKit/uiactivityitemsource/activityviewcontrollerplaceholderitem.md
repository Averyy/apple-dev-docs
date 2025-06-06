# activityViewControllerPlaceholderItem(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the placeholder object for the data.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func activityViewControllerPlaceholderItem(_ activityViewController: UIActivityViewController) -> Any
```

#### Return Value

An object to use as a placeholder for the actual data.

#### Discussion

This method returns an object that can be used as a placeholder for the real data. Placeholder objects don’t have to contain any real data but should be configured as closely as possible to the actual data object you intend to provide. In general the actual value should match in type but it’s possible to return a different type of data for [`activityViewController(_:itemForActivityType:)`](uiactivityitemsource/activityviewcontroller(_:itemforactivitytype:).md). It should be one that the activity can handle otherwise you may get an activity with empty content. For example, the placeholder could be a [`UIImage`](uiimage.md) object but the actual value could be an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object with PDF information.

## Parameters

- `activityViewController`: The activity view controller object requesting the placeholder item.

## See Also

- [func activityViewController(UIActivityViewController, itemForActivityType: UIActivity.ActivityType?) -> Any?](uiactivityitemsource/activityviewcontroller(_:itemforactivitytype:).md)
  Returns the data object to be acted upon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontrollerplaceholderitem(_:))*