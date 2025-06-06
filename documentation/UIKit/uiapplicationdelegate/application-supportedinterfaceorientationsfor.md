# application(_:supportedInterfaceOrientationsFor:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the interface orientations to use for the view controllers in the specified window.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, supportedInterfaceOrientationsFor window: UIWindow?) -> UIInterfaceOrientationMask
```

#### Return Value

A bit mask of the [`UIInterfaceOrientationMask`](uiinterfaceorientationmask.md) constants that indicate the orientations to use for the view controllers.

#### Discussion

This method returns the total set of interface orientations supported by the app. When determining whether to rotate a particular view controller, the orientations returned by this method are intersected with the orientations supported by the root view controller or topmost presented view controller. The app and view controller must agree before the rotation is allowed.

If you do not implement this method, the app uses the values in the `UIInterfaceOrientation` key of the app’s `Info.plist` as the default interface orientations.

## Parameters

- `application`: Your singleton app object.
- `window`: The window whose interface orientations you want to retrieve.

## See Also

- [enum UIInterfaceOrientation](uiinterfaceorientation.md)
  Constants that specify the orientation of the app’s user interface.
- [struct UIInterfaceOrientationMask](uiinterfaceorientationmask.md)
  Constants that specify a view controller’s supported interface orientations.
- [class let invalidInterfaceOrientationException: NSExceptionName](uiapplication/invalidinterfaceorientationexception.md)
  An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:supportedinterfaceorientationsfor:))*