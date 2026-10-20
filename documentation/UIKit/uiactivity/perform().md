# perform()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) performActivity;
```

#### Discussion

The default implementation of this method does nothing. If your service doesn’t provide any custom UI using the [`activityViewController`](./activityviewcontroller.md) method, override this method and use it to perform the activity. Your activity must operate on the data items received in the [`prepare(withActivityItems:)`](./prepare%28withactivityitems%29.md) method.

This method is called on your app’s main thread. If your app can complete the activity quickly on the main thread, do so and call the [`activityDidFinish(_:)`](./activitydidfinish%28_%29.md) method when it’s done. If performing the activity might take some time, use this method to start the work in the background and then exit without calling [`activityDidFinish(_:)`](./activitydidfinish%28_%29.md) from this method. When your background work has completed, call [`activityDidFinish(_:)`](./activitydidfinish%28_%29.md). You must call [`activityDidFinish(_:)`](./activitydidfinish%28_%29.md) on the main thread.

## See Also

### Performing the activity
- [func canPerform(withActivityItems: [Any]) -> Bool](./canperform%28withactivityitems%29.md)
  Queries whether the service can act on the specified data items.
- [func prepare(withActivityItems: [Any])](./prepare%28withactivityitems%29.md)
  Prepares your service to act on the specified data.
- [var activityViewController: UIViewController?](./activityviewcontroller.md)
  The view controller to present to the user.
- [func activityDidFinish(Bool)](./activitydidfinish%28_%29.md)
  Notifies the system that your activity object has completed its work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/perform())*