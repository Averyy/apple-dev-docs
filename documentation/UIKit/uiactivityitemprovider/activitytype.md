# activityType

**Framework**: UIKit  
**Kind**: property

The type of the activity object that is expecting the data.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var activityType: UIActivity.ActivityType? { get }
```

#### Discussion

The value of this property is `nil` until the user selects an activity. At that time, the value is set and the provider object is submitted to a queue for execution. Thus, you should access this value only after your object’s [`item`](uiactivityitemprovider/item.md) method is called.

## See Also

- [var item: Any](uiactivityitemprovider/item.md)
  Generates and returns the actual data-bearing object.
- [var placeholderItem: Any?](uiactivityitemprovider/placeholderitem.md)
  The placeholder object you specified at initialization time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/activitytype)*