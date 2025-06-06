# activityViewController

**Framework**: UIKit  
**Kind**: property

The view controller to present to the user.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var activityViewController: UIViewController? { get }
```

#### Discussion

Subclasses that provide additional UI using a view controller can override this method to return that view controller. If this method returns a valid object, the system presents the returned view controller modally instead of calling the [`perform()`](uiactivity/perform().md) method.

Your custom view controller should provide a view with your custom UI and should handle any user interactions inside those views. Upon completing the activity, don’t dismiss the view controller yourself. Instead, call the [`activityDidFinish(_:)`](uiactivity/activitydidfinish(_:).md) method and let the system dismiss it for you.

## See Also

- [func canPerform(withActivityItems: [Any]) -> Bool](uiactivity/canperform(withactivityitems:).md)
  Queries whether the service can act on the specified data items.
- [func prepare(withActivityItems: [Any])](uiactivity/prepare(withactivityitems:).md)
  Prepares your service to act on the specified data.
- [func perform()](uiactivity/perform.md)
  Performs the service when no custom view controller is provided.
- [func activityDidFinish(Bool)](uiactivity/activitydidfinish(_:).md)
  Notifies the system that your activity object has completed its work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activityviewcontroller)*