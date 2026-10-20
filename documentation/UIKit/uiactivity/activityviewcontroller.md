# activityViewController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) UIViewController * activityViewController;
```

#### Discussion

Subclasses that provide additional UI using a view controller can override this method to return that view controller. If this method returns a valid object, the system presents the returned view controller modally instead of calling the [`perform()`](./perform%28%29.md) method.

Your custom view controller should provide a view with your custom UI and should handle any user interactions inside those views. Upon completing the activity, don’t dismiss the view controller yourself. Instead, call the [`activityDidFinish(_:)`](./activitydidfinish%28_%29.md) method and let the system dismiss it for you.

## See Also

### Performing the activity
- [func canPerform(withActivityItems: [Any]) -> Bool](./canperform%28withactivityitems%29.md)
  Queries whether the service can act on the specified data items.
- [func prepare(withActivityItems: [Any])](./prepare%28withactivityitems%29.md)
  Prepares your service to act on the specified data.
- [func perform()](./perform%28%29.md)
  Performs the service when no custom view controller is provided.
- [func activityDidFinish(Bool)](./activitydidfinish%28_%29.md)
  Notifies the system that your activity object has completed its work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activityviewcontroller)*