# UIInterfaceOrientationMask

**Framework**: UIKit  
**Kind**: struct

Constants that specify a view controller’s supported interface orientations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
struct UIInterfaceOrientationMask
```

#### Overview

Starting in iOS 8, you should employ the [`UITraitCollection`](uitraitcollection.md) and [`UITraitEnvironment`](uitraitenvironment.md) APIs, and size class properties as used in those APIs, instead of using [`UIInterfaceOrientation`](uiinterfaceorientation.md) constants or otherwise writing your app in terms of interface orientation.

In earlier versions of iOS, you returned these constants from the [`supportedInterfaceOrientations(for:)`](uiapplication/supportedinterfaceorientations(for:).md) method or when determining which orientations to support in your app’s view controllers.

## Topics

### Constants
- [static var portrait: UIInterfaceOrientationMask](uiinterfaceorientationmask/portrait.md)
  The view controller supports a portrait interface orientation.
- [static var landscapeLeft: UIInterfaceOrientationMask](uiinterfaceorientationmask/landscapeleft.md)
  The view controller supports a landscape-left interface orientation.
- [static var landscapeRight: UIInterfaceOrientationMask](uiinterfaceorientationmask/landscaperight.md)
  The view controller supports a landscape-right interface orientation.
- [static var portraitUpsideDown: UIInterfaceOrientationMask](uiinterfaceorientationmask/portraitupsidedown.md)
  The view controller supports an upside-down portrait interface orientation.
- [static var landscape: UIInterfaceOrientationMask](uiinterfaceorientationmask/landscape.md)
  The view controller supports both landscape-left and landscape-right interface orientation.
- [static var all: UIInterfaceOrientationMask](uiinterfaceorientationmask/all.md)
  The view controller supports all interface orientations.
- [static var allButUpsideDown: UIInterfaceOrientationMask](uiinterfaceorientationmask/allbutupsidedown.md)
  The view controller supports all but the upside-down portrait interface orientation.
### Initializers
- [init(rawValue: UInt)](uiinterfaceorientationmask/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func application(UIApplication, supportedInterfaceOrientationsFor: UIWindow?) -> UIInterfaceOrientationMask](uiapplicationdelegate/application(_:supportedinterfaceorientationsfor:).md)
  Asks the delegate for the interface orientations to use for the view controllers in the specified window.
- [enum UIInterfaceOrientation](uiinterfaceorientation.md)
  Constants that specify the orientation of the app’s user interface.
- [class let invalidInterfaceOrientationException: NSExceptionName](uiapplication/invalidinterfaceorientationexception.md)
  An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask)*