# activityDidFinish(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the system that your activity object has completed its work.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func activityDidFinish(_ completed: Bool)
```

```objc
- (void) activityDidFinish:(BOOL) completed;
```

#### Discussion

This method dismisses the sharing interface provided by the [`UIActivityViewController`](../uiactivityviewcontroller.md) object. If you provided a view controller using the [`activityViewController`](./activityviewcontroller.md) method, this method dismisses that view controller too.

You must call this method after completing the work associated with this object’s service. This is true regardless of whether you used the [`activityViewController`](./activityviewcontroller.md) or [`perform()`](./perform%28%29.md) method to initiate the service. When calling the method, use the Boolean value to indicate whether the service completed successfully.

This method must be called on the main thread.

## Parameters

- `completed`: Specify [`true`](../../Swift/true.md) if the service executed to completion or [`false`](../../Swift/false.md) if the service was canceled or didn’t finish because of an error.

## See Also

### Performing the activity
- [func canPerform(withActivityItems: [Any]) -> Bool](./canperform%28withactivityitems%29.md)
  Queries whether the service can act on the specified data items.
- [func prepare(withActivityItems: [Any])](./prepare%28withactivityitems%29.md)
  Prepares your service to act on the specified data.
- [var activityViewController: UIViewController?](./activityviewcontroller.md)
  The view controller to present to the user.
- [func perform()](./perform%28%29.md)
  Performs the service when no custom view controller is provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitydidfinish(_:))*