# additionalActivityItems

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

The list of activity items associated with an activity.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var additionalActivityItems: [CLSActivityItem] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<__kindof CLSActivityItem *> * additionalActivityItems;
```

## See Also

### Managing activity items
- [func addAdditionalActivityItem(CLSActivityItem)](./addadditionalactivityitem%28_%29.md)
  Adds an activity item to an activity.
- [var primaryActivityItem: CLSActivityItem?](./primaryactivityitem.md)
  Adds an activity item to an activity and sets it as the primary activity item.
- [func removeAllActivityItems()](./removeallactivityitems%28%29.md)
  Deletes all activity items associated with the current activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity/additionalactivityitems)*