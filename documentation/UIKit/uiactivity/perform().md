# perform()

**Framework**: UIKit  
**Kind**: method

Performs the service when no custom view controller is provided.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func perform()
```

#### Discussion

The default implementation of this method does nothing. If your service doesn’t provide any custom UI using the [`activityViewController`](uiactivity/activityviewcontroller.md) method, override this method and use it to perform the activity. Your activity must operate on the data items received in the [`prepare(withActivityItems:)`](uiactivity/prepare(withactivityitems:).md) method.

This method is called on your app’s main thread. If your app can complete the activity quickly on the main thread, do so and call the [`activityDidFinish(_:)`](uiactivity/activitydidfinish(_:).md) method when it’s done. If performing the activity might take some time, use this method to start the work in the background and then exit without calling [`activityDidFinish(_:)`](uiactivity/activitydidfinish(_:).md) from this method. When your background work has completed, call [`activityDidFinish(_:)`](uiactivity/activitydidfinish(_:).md). You must call [`activityDidFinish(_:)`](uiactivity/activitydidfinish(_:).md) on the main thread.

## See Also

- [func canPerform(withActivityItems: [Any]) -> Bool](uiactivity/canperform(withactivityitems:).md)
  Queries whether the service can act on the specified data items.
- [func prepare(withActivityItems: [Any])](uiactivity/prepare(withactivityitems:).md)
  Prepares your service to act on the specified data.
- [var activityViewController: UIViewController?](uiactivity/activityviewcontroller.md)
  The view controller to present to the user.
- [func activityDidFinish(Bool)](uiactivity/activitydidfinish(_:).md)
  Notifies the system that your activity object has completed its work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/perform())*