# show(_:sender:)

**Framework**: UIKit  
**Kind**: method

Presents the specified view controller in the navigation interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func show(_ vc: UIViewController, sender: Any?)
```

#### Discussion

This method pushes `vc` onto the navigation stack in a similar way as the [`pushViewController(_:animated:)`](uinavigationcontroller/pushviewcontroller(_:animated:).md) method. You can call this method directly if you want but typically this method is called from elsewhere in the view controller hierarchy when a new view controller needs to be shown.

The Show segue uses this method to display a new view controller.

## Parameters

- `vc`: The view controller to display.
- `sender`: The object that made the request to show the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/show(_:sender:))*