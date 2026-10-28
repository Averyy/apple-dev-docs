# canPerform(withActivityItems:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) canPerformWithActivityItems:(NSArray *) activityItems;
```

## Return Value

[`true`](../../Swift/true.md) if your service can act on the specified data items or [`false`](../../Swift/false.md) if it cannot.

## Discussion

The default implementation of this method returns [`false`](../../Swift/false.md). Subclasses must override it and return [`true`](../../Swift/true.md) if the data in the `activityItems` parameter can be operated on by your service. Your implementation should check the types of the objects in the array and use that information to determine if your service can act on the corresponding data.

The [`UIActivityViewController`](../uiactivityviewcontroller.md) object calls this method when determining which services to show to the user.

## Parameters

- `activityItems`: An array of objects of varying types. These are the data objects on which the service would act.

## See Also

### Performing the activity
- [func prepare(withActivityItems: [Any])](./prepare%28withactivityitems%29.md)
  Prepares your service to act on the specified data.
- [var activityViewController: UIViewController?](./activityviewcontroller.md)
  The view controller to present to the user.
- [func perform()](./perform%28%29.md)
  Performs the service when no custom view controller is provided.
- [func activityDidFinish(Bool)](./activitydidfinish%28_%29.md)
  Notifies the system that your activity object has completed its work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/canperform(withactivityitems:))*