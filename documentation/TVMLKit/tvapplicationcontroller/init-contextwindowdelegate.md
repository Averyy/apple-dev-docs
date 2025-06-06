# init(context:window:delegate:)

**Framework**: TVMLKit  
**Kind**: init

Initializes and returns an app controller.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
init(context: TVApplicationControllerContext, window: UIWindow?, delegate: (any TVApplicationControllerDelegate)?)
```

#### Return Value

The initialized [`TVApplicationController`](tvapplicationcontroller.md) object.

#### Discussion

An app controller coordinates activity between the JavaScript environments and tvOS. There are three options when presenting the application controller. If you provide a valid [`UIWindow`](https://developer.apple.com/documentation/UIKit/UIWindow) object, the application controller’s navigation controller is presented immediately and managed by [`TVApplicationController`](tvapplicationcontroller.md). If no window is provided, the navigation controller can be presented and dismissed manually within the binary app. Finally, if you wish to present native view controllers alongside a [`TVApplicationController`](tvapplicationcontroller.md) object, you can push additional view controllers onto [`navigationController`](tvapplicationcontroller/navigationcontroller.md).

## Parameters

- `context`: A   object containing information about the JavaScript app.
- `window`: A   object that presents the application controller’s navigation controller.
- `delegate`: The app controller delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/init(context:window:delegate:))*