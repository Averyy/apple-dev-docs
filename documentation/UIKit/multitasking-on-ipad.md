# Multitasking on iPad

**Framework**: UIKit

Implement multitasking APIs to seamlessly integrate your app with iPadOS.

#### Overview

While your app’s scene runs in the foreground on iPad, other apps are likely to be running alongside it. Being aware of the environment your app may be running in and adopting the multitasking APIs are an essential part of integrating your apps with iPadOS.

The first step to creating a great multitasking experience for your users is to ensure your app’s scenes can adapt to different window sizes. Start by reading the [`Adaptivity and Layout`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/visual-design/adaptivity-and-layout/) section of the [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/). Also, consider that your app may not be running full screen, but in a smaller window through Slide Over or Split View. Discover your app’s environment with [`UITraitCollection`](uitraitcollection.md) and adapt to it by using Auto Layout, or by overriding [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) in your view controllers or views.

You can choose to allow multiple scenes in your app’s UI to run concurrently by setting the [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsMultipleScenes) property list key. Implement [`Scenes`](scenes.md) and read [`Managing your app’s life cycle`](managing-your-app-s-life-cycle.md) for an overview of how [`UISceneDelegate`](uiscenedelegate.md) interacts with the system multitasking events. For information on adopting the scene-based life cycle, see [`TN3187: Migrating to the UIKit scene-based life cycle`](https://developer.apple.com/documentation/Technotes/tn3187-Migrating-to-the-UIKit-scene-based-life-cycle).

Design your app’s scenes to display correctly in any interface orientation. In situations where you want to lock the app’s interface to its current orientation, call [`setNeedsUpdateOfPrefersInterfaceOrientationLocked()`](uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked().md), then return `true` as the value of [`prefersInterfaceOrientationLocked`](uiviewcontroller/prefersinterfaceorientationlocked.md), or override [`childViewControllerForInterfaceOrientationLock`](uiviewcontroller/childviewcontrollerforinterfaceorientationlock.md) to delegate the decision to a child view controller. Implement [`windowScene(_:didUpdateEffectiveGeometry:)`](uiwindowscenedelegate/windowscene(_:didupdateeffectivegeometry:).md) to observe orientation changes, as the system might change the interface orientation even if you signal a preference to lock it. The preference to lock the interface orientation lasts until your app stops presenting the scene, or you call `setNeedsUpdateOfPrefersInterfaceOrientationLocked()` again and return `false` as the value of `prefersInterfaceOrientationLocked`.

## Topics

### Adaptivity
- [class UITraitCollection](uitraitcollection.md)
  A collection of data that represents the environment for an individual element in your app’s user interface.
- [protocol UITraitEnvironment](uitraitenvironment.md)
  A set of methods that makes the iOS interface environment available to your app.
- [protocol UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.
### Scene Management
- [Scenes](scenes.md)
  Manage multiple instances of your app’s UI simultaneously, and direct resources to the appropriate instance of your UI.
- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md)
  Support side-by-side instances of your app’s interface and create new windows.

## See Also

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)
  Optimize your iPad app’s user experience by adopting desktop-class enhancements for multitasking with Stage Manager, document interactions, text editing, search, and more.
- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)
  Provide a compact, ergonomic tab bar for quick access to key parts of your app, and a sidebar for in-depth navigation.
- [Supporting desktop-class features in your iPad app](supporting-desktop-class-features-in-your-ipad-app.md)
  Enhance your iPad app by adding desktop-class features and document support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/multitasking-on-ipad)*