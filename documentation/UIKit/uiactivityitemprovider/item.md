# item

**Framework**: UIKit  
**Kind**: property

Generates and returns the actual data-bearing object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var item: Any { get }
```

#### Discussion

When the actual data-bearing object is required, this method is called by the provider object’s infrastructure. Subclasses must override this method and use it to perform whatever work is required to create the object and return it. You implement this method instead of the normal [`main()`](https://developer.apple.com/documentation/Foundation/Operation/main()) method you would implement for operation objects. This method is called on a secondary thread of your app.

The system provides no built-in progress indicator, so if generating the item may take a long time you should plan on providing feedback in your app yourself.

## See Also

- [var placeholderItem: Any?](uiactivityitemprovider/placeholderitem.md)
  The placeholder object you specified at initialization time.
- [var activityType: UIActivity.ActivityType?](uiactivityitemprovider/activitytype.md)
  The type of the activity object that is expecting the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/item)*