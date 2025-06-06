# prepare(withActivityItems:)

**Framework**: UIKit  
**Kind**: method

Prepares your service to act on the specified data.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func prepare(withActivityItems activityItems: [Any])
```

#### Discussion

The default implementation of this method does nothing. This method is called after the user has selected your service but before your service is asked to perform its action. Subclasses should override this method and use it to store a reference to the data items in the `activityItems` parameter. In addition, if the implementation of your service requires displaying additional UI to the user, you can use this method to prepare your view controller object and make it available from the [`activityViewController`](uiactivity/activityviewcontroller.md) method.

## Parameters

- `activityItems`: An array of objects of varying types. These are the data objects on which to act.

## See Also

- [func canPerform(withActivityItems: [Any]) -> Bool](uiactivity/canperform(withactivityitems:).md)
  Queries whether the service can act on the specified data items.
- [var activityViewController: UIViewController?](uiactivity/activityviewcontroller.md)
  The view controller to present to the user.
- [func perform()](uiactivity/perform.md)
  Performs the service when no custom view controller is provided.
- [func activityDidFinish(Bool)](uiactivity/activitydidfinish(_:).md)
  Notifies the system that your activity object has completed its work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/prepare(withactivityitems:))*