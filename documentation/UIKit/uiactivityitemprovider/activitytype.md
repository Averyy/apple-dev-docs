# activityType

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) UIActivityType activityType;
```

#### Discussion

The value of this property is `nil` until the user selects an activity. At that time, the value is set and the provider object is submitted to a queue for execution. Thus, you should access this value only after your object’s [`item`](./item.md) method is called.

## See Also

### Accessing the provider attributes
- [var item: Any](./item.md)
  Generates and returns the actual data-bearing object.
- [var placeholderItem: Any?](./placeholderitem.md)
  The placeholder object you specified at initialization time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/activitytype)*