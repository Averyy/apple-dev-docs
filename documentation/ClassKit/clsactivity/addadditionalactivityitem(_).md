# addAdditionalActivityItem(_:)

**Framework**: ClassKit  
**Kind**: method  
**Role**: Instance Method

Adds an activity item to an activity.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func addAdditionalActivityItem(_ activityItem: CLSActivityItem)
```

```objc
- (void) addAdditionalActivityItem:(CLSActivityItem *) activityItem;
```

## Mentions

- [Recording additional metrics about a completed task](../recording-additional-metrics-about-a-completed-task.md)

## Parameters

- `activityItem`: The activity item to add to the activity.

## See Also

### Managing activity items
- [var primaryActivityItem: CLSActivityItem?](./primaryactivityitem.md)
  Adds an activity item to an activity and sets it as the primary activity item.
- [var additionalActivityItems: [CLSActivityItem]](./additionalactivityitems.md)
  The list of activity items associated with an activity.
- [func removeAllActivityItems()](./removeallactivityitems%28%29.md)
  Deletes all activity items associated with the current activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity/addadditionalactivityitem(_:))*