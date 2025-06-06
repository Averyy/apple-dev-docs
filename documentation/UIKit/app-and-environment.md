# App and environment

**Framework**: UIKit

Manage life-cycle events and your app’s UI scenes, and get information about traits and the environment in which your app runs.

#### Overview

In iOS 13 and later, a person can create and manage multiple instances of your app’s user interface simultaneously, and switch between them using the app switcher. On iPad, a person can also display multiple instances of your app side by side. Each instance of your UI displays different content, or displays the same content in a different way. For example, a person can display one instance of the Calendar app showing a specific day, and another showing an entire month.

UIKit communicates details about the current environment using , which reflect a combination of device settings, interface settings, and user preferences. For example, you use traits to detect whether Dark Mode is active for the current view or view controller. Consult the current trait collection of your [`UIView`](uiview.md) or [`UIViewController`](uiviewcontroller.md) object when you want to customize its contents based on the current environment. Adopt the [`UITraitEnvironment`](uitraitenvironment.md) protocol in other objects when you want them to receive trait notification changes.

## Topics

### Life cycle
- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md)
  Respond to system notifications when your app is in the foreground or background, and handle other significant system-related events.
- [Responding to the launch of your app](responding-to-the-launch-of-your-app.md)
  Initialize your app’s data structures, prepare your app to run, and respond to any launch-time requests from the system.
- [class UIApplication](uiapplication.md)
  The centralized point of control and coordination for apps running in iOS.
- [protocol UIApplicationDelegate](uiapplicationdelegate.md)
  A set of methods to manage shared behaviors for your app.
- [Scenes](scenes.md)
  Manage multiple instances of your app’s UI simultaneously, and direct resources to the appropriate instance of your UI.
### Device environment
- [class UIDevice](uidevice.md)
  A representation of the current device.
- [class UIStatusBarManager](uistatusbarmanager.md)
  An object that describes the configuration of the status bar.
### Adaptivity
- [Automatic trait tracking](automatic-trait-tracking.md)
  Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [Responding to changing display modes on Apple TV](responding-to-changing-display-modes-on-apple-tv.md)
  Change images and resources dynamically when the screen gamut on your device changes.
- [class UITraitCollection](uitraitcollection.md)
  A collection of data that represents the environment for an individual element in your app’s user interface.
- [protocol UITraitEnvironment](uitraitenvironment.md)
  A set of methods that makes the iOS interface environment available to your app.
- [protocol UITraitChangeObservable](uitraitchangeobservable-67e94.md)
  A type that calls your code in reaction to changes in the trait environment.
- [protocol UIMutableTraits](uimutabletraits-13ja5.md)
  A mutable container of traits.
- [protocol UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.
### Custom traits
- [protocol UIMutableTraits](uimutabletraits-13ja5.md)
  A mutable container of traits.
- [typealias UITrait](uitrait-9423.md)
  A type representing a trait in a trait collection.
- [protocol UITraitDefinition](uitraitdefinition-64c15.md)
  A type representing a trait in a trait collection.
### iPad
- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)
  Optimize your iPad app’s user experience by adopting desktop-class enhancements for multitasking with Stage Manager, document interactions, text editing, search, and more.
- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)
  Provide a compact, ergonomic tab bar for quick access to key parts of your app, and a sidebar for in-depth navigation.
- [Supporting desktop-class features in your iPad app](supporting-desktop-class-features-in-your-ipad-app.md)
  Enhance your iPad app by adding desktop-class features and document support.
- [Multitasking on iPad](multitasking-on-ipad.md)
  Implement multitasking APIs to seamlessly integrate your app with iPadOS.
### Guided Access
- [protocol UIGuidedAccessRestrictionDelegate](uiguidedaccessrestrictiondelegate.md)
  A set of methods you use to add custom restrictions for the Guided Access feature in iOS.
- [static func guidedAccessRestrictionState(forIdentifier: String) -> UIAccessibility.GuidedAccessRestrictionState](uiaccessibility/guidedaccessrestrictionstate(foridentifier:).md)
  Returns the restriction state for the specified guided access restriction.
### Architecture
- [Updating your app from 32-bit to 64-bit architecture](updating-your-app-from-32-bit-to-64-bit-architecture.md)
  Ensure that your app behaves as expected by adapting it to support later versions of the operating system.
- [func UIApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?, String?) -> Int32](uiapplicationmain(_:_:_:_:)-1yub7.md)
  Creates the application object and the application delegate and sets up the event cycle.

## See Also

- [Documents, data, and pasteboard](documents-data-and-pasteboard.md)
  Organize your app’s data and share that data on the pasteboard.
- [Resource management](resource-management.md)
  Manage the images, strings, storyboards, and nib files that you use to implement your app’s interface.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system.
- [Interprocess communication](interprocess-communication.md)
  Display activity-based services to people.
- [Mac Catalyst](mac-catalyst.md)
  Create a version of your iPad app that users can run on a Mac device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/app-and-environment)*