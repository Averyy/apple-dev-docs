# presentationController(_:prepare:)

**Framework**: UIKit  
**Kind**: method

Provides an opportunity to configure the adaptive presentation controller after an adaptivity change.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func presentationController(_ presentationController: UIPresentationController, prepare adaptivePresentationController: UIPresentationController)
```

#### Discussion

The system calls this method during adaptation so the delegate can configure properties of the adaptive presentation controller before it presents.

For example, the system automatically adapts a view controller that presents as a popover in standard size classes to a sheet in compact size classes. You can implement this method to customize the sheet’s properties before it presents.

## Parameters

- `presentationController`: The presentation controller that is managing the adaptivity change.
- `adaptivePresentationController`: The adaptive presentation controller to prepare. Configure this presentation controller’s properties as necessary before it presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:prepare:))*