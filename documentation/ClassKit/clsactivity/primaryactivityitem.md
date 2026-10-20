# primaryActivityItem

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

Adds an activity item to an activity and sets it as the primary activity item.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var primaryActivityItem: CLSActivityItem? { get set }
```

```objc
@property (nonatomic, strong, nullable) CLSActivityItem * primaryActivityItem;
```

## Mentions

- [Recording additional metrics about a completed task](../recording-additional-metrics-about-a-completed-task.md)

## See Also

### Managing activity items
- [func addAdditionalActivityItem(CLSActivityItem)](./addadditionalactivityitem%28_%29.md)
  Adds an activity item to an activity.
- [var additionalActivityItems: [CLSActivityItem]](./additionalactivityitems.md)
  The list of activity items associated with an activity.
- [func removeAllActivityItems()](./removeallactivityitems%28%29.md)
  Deletes all activity items associated with the current activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity/primaryactivityitem)*