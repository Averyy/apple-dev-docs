# activityViewController(_:itemForActivityType:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the data object to be acted upon.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func activityViewController(_ activityViewController: UIActivityViewController, itemForActivityType activityType: UIActivity.ActivityType?) -> Any?
```

#### Return Value

The final data object to be acted on. May be `nil` if multiple items were registered for a single activity type, so long as one of the items returns an actual value.

#### Discussion

This method returns the actual data object to be acted on by an activity object. Your implementation of this method should create or generate the data object and return it as quickly as possible.

## Parameters

- `activityViewController`: The activity view controller object requesting the data item.
- `activityType`: The type of activity to be performed with the data object. You can use this string to decide how best to prepare the data object.

## See Also

- [func activityViewControllerPlaceholderItem(UIActivityViewController) -> Any](uiactivityitemsource/activityviewcontrollerplaceholderitem(_:).md)
  Returns the placeholder object for the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:itemforactivitytype:))*