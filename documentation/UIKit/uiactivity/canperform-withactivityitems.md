# canPerform(withActivityItems:)

**Framework**: UIKit  
**Kind**: method

Queries whether the service can act on the specified data items.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func canPerform(withActivityItems activityItems: [Any]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if your service can act on the specified data items or [`false`](https://developer.apple.com/documentation/swift/false) if it cannot.

#### Discussion

The default implementation of this method returns [`false`](https://developer.apple.com/documentation/swift/false). Subclasses must override it and return [`true`](https://developer.apple.com/documentation/swift/true) if the data in the `activityItems` parameter can be operated on by your service. Your implementation should check the types of the objects in the array and use that information to determine if your service can act on the corresponding data.

The [`UIActivityViewController`](uiactivityviewcontroller.md) object calls this method when determining which services to show to the user.

## Parameters

- `activityItems`: An array of objects of varying types. These are the data objects on which the service would act.

## See Also

- [func prepare(withActivityItems: [Any])](uiactivity/prepare(withactivityitems:).md)
  Prepares your service to act on the specified data.
- [var activityViewController: UIViewController?](uiactivity/activityviewcontroller.md)
  The view controller to present to the user.
- [func perform()](uiactivity/perform.md)
  Performs the service when no custom view controller is provided.
- [func activityDidFinish(Bool)](uiactivity/activitydidfinish(_:).md)
  Notifies the system that your activity object has completed its work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/canperform(withactivityitems:))*