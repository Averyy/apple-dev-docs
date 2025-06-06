# invalidInterfaceOrientationException

**Framework**: UIKit  
**Kind**: property

An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class let invalidInterfaceOrientationException: NSExceptionName
```

#### Discussion

This exception is thrown if a view controller or the app returns `0` instead of a valid set of supported interface orientation values. It is also thrown if the orientation returned by a view controller’s [`preferredInterfaceOrientationForPresentation`](uiviewcontroller/preferredinterfaceorientationforpresentation.md) method does not match one of the view controller’s supported orientations.

## See Also

- [func application(UIApplication, supportedInterfaceOrientationsFor: UIWindow?) -> UIInterfaceOrientationMask](uiapplicationdelegate/application(_:supportedinterfaceorientationsfor:).md)
  Asks the delegate for the interface orientations to use for the view controllers in the specified window.
- [enum UIInterfaceOrientation](uiinterfaceorientation.md)
  Constants that specify the orientation of the app’s user interface.
- [struct UIInterfaceOrientationMask](uiinterfaceorientationmask.md)
  Constants that specify a view controller’s supported interface orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/invalidinterfaceorientationexception)*