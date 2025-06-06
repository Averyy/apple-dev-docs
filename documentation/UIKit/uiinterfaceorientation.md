# UIInterfaceOrientation

**Framework**: UIKit  
**Kind**: enum

Constants that specify the orientation of the app’s user interface.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum UIInterfaceOrientation
```

#### Overview

Starting in iOS 8, you should employ the [`UITraitCollection`](uitraitcollection.md) and [`UITraitEnvironment`](uitraitenvironment.md) APIs, and size class properties as used in those APIs, instead of using [`UIInterfaceOrientation`](uiinterfaceorientation.md) constants or otherwise writing your app in terms of interface orientation.

In earlier versions of iOS, you used these constants in the [`statusBarOrientation`](uiapplication/statusbarorientation.md) property and the [`setStatusBarOrientation(_:animated:)`](uiapplication/setstatusbarorientation(_:animated:).md) method.

> ❗ **Important**:  Notice that [`UIDeviceOrientation.landscapeRight`](uideviceorientation/landscaperight.md) is assigned to [`UIInterfaceOrientation.landscapeLeft`](uiinterfaceorientation/landscapeleft.md) and [`UIDeviceOrientation.landscapeLeft`](uideviceorientation/landscapeleft.md) is assigned to [`UIInterfaceOrientation.landscapeRight`](uiinterfaceorientation/landscaperight.md). The reason for this is that rotating the device requires rotating the content in the opposite direction.

 Notice that [`UIDeviceOrientation.landscapeRight`](uideviceorientation/landscaperight.md) is assigned to [`UIInterfaceOrientation.landscapeLeft`](uiinterfaceorientation/landscapeleft.md) and [`UIDeviceOrientation.landscapeLeft`](uideviceorientation/landscapeleft.md) is assigned to [`UIInterfaceOrientation.landscapeRight`](uiinterfaceorientation/landscaperight.md). The reason for this is that rotating the device requires rotating the content in the opposite direction.

## Topics

### Orientations
- [UIInterfaceOrientation.unknown](uiinterfaceorientation/unknown.md)
  The orientation of the device is unknown.
- [UIInterfaceOrientation.portrait](uiinterfaceorientation/portrait.md)
  The device is in portrait mode, with the device upright and the Home button on the bottom.
- [UIInterfaceOrientation.portraitUpsideDown](uiinterfaceorientation/portraitupsidedown.md)
  The device is in portrait mode but is upside down, with the device upright and the Home button at the top.
- [UIInterfaceOrientation.landscapeLeft](uiinterfaceorientation/landscapeleft.md)
  The device is in landscape mode, with the device upright and the Home button on the left.
- [UIInterfaceOrientation.landscapeRight](uiinterfaceorientation/landscaperight.md)
  The device is in landscape mode, with the device upright and the Home button on the right.
### Orientation Checks
- [var isLandscape: Bool](uiinterfaceorientation/islandscape.md)
  A Boolean value that indicates whether the user interface is currently presented in a landscape orientation.
- [var isPortrait: Bool](uiinterfaceorientation/isportrait.md)
  A Boolean value that indicates whether the user interface is currently presented in a portrait orientation.
### Initializers
- [init?(rawValue: Int)](uiinterfaceorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func application(UIApplication, supportedInterfaceOrientationsFor: UIWindow?) -> UIInterfaceOrientationMask](uiapplicationdelegate/application(_:supportedinterfaceorientationsfor:).md)
  Asks the delegate for the interface orientations to use for the view controllers in the specified window.
- [struct UIInterfaceOrientationMask](uiinterfaceorientationmask.md)
  Constants that specify a view controller’s supported interface orientations.
- [class let invalidInterfaceOrientationException: NSExceptionName](uiapplication/invalidinterfaceorientationexception.md)
  An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinterfaceorientation)*