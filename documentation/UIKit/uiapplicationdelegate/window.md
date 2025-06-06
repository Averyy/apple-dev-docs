# window

**Framework**: UIKit  
**Kind**: property

The window to use when presenting a storyboard.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var window: UIWindow? { get set }
```

#### Discussion

This property contains the window used to present the app’s visual content on the device’s main screen.

Implementation of this property is required if your app’s `Info.plist` file contains the `UIMainStoryboardFile` key. Fortunately, the Xcode project templates usually include a synthesized declaration of the property automatically for the app delegate. The default value of this synthesized property is `nil`, which causes the app to create a generic [`UIWindow`](uiwindow.md) object and assign it to the property. If you want to provide a custom window for your app, you must implement the getter method of this property and use it to create and return your custom window.

For more information about the [`UIMainStoryboardFile`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW9) key, see [`Information Property List Key Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/window)*