# removeAllActivityItems()

**Framework**: ClassKit  
**Kind**: method  
**Role**: Instance Method

Deletes all activity items associated with the current activity.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func removeAllActivityItems()
```

```objc
- (void) removeAllActivityItems;
```

## Discussion

Call the [`save(completion:)`](../clsdatastore/save%28completion%29.md) method on the data store after removing activity items, just as you would when adding items, to propagate the changes to the network:

```swift
activity.removeAllActivityItems()

CLSDataStore.shared.save { error in
    // Handle errors.
}
```

## See Also

### Managing activity items
- [func addAdditionalActivityItem(CLSActivityItem)](./addadditionalactivityitem%28_%29.md)
  Adds an activity item to an activity.
- [var primaryActivityItem: CLSActivityItem?](./primaryactivityitem.md)
  Adds an activity item to an activity and sets it as the primary activity item.
- [var additionalActivityItems: [CLSActivityItem]](./additionalactivityitems.md)
  The list of activity items associated with an activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity/removeallactivityitems())*