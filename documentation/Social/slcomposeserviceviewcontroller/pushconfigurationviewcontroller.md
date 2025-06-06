# pushConfigurationViewController(_:)

**Framework**: Social  
**Kind**: method

Presents a configuration view controller that lets the user configure the post.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func pushConfigurationViewController(_ viewController: UIViewController!)
```

#### Discussion

Typically, this method is called in the tap handler for a configuration item. A user selects a configuration item from the list displayed in the compose view and the associated configuration view controller is displayed. Only one configuration view controller can be visible at a time.

Note that your custom configuration view controller should set its [`preferredContentSize`](https://developer.apple.com/documentation/UIKit/UIViewController/preferredContentSize) property to an appropriate value. `SLComposeServiceViewController` observes changes to the [`preferredContentSize`](https://developer.apple.com/documentation/UIKit/UIViewController/preferredContentSize) property and animates view size changes if necessary.

## Parameters

- `viewController`: The view controller that manages the type of configuration the user selected.

## See Also

- [func popConfigurationViewController()](slcomposeserviceviewcontroller/popconfigurationviewcontroller.md)
  Dismisses the current configuration view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/pushconfigurationviewcontroller(_:))*