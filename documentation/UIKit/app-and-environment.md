# App and environment

**Framework**: UIKit

Manage life-cycle events and your app’s UI scenes, and get information about traits and the environment in which your app runs.

#### Overview

From the moment a person opens your app, a number of things can happen that your app may need to handle or adjust to, such as switching to another app, receiving a call, switching Dark Mode on or off, or rotating the device. UIKit communicates some changes as life cycle events, and others as trait changes.

Your app displays its interface in one or more scenes. On iPhone, your app only shows one scene. On iPad, Mac, and Apple Vision Pro, a person can create and manage multiple instances of your app’s user interface simultaneously, in different windows or side by side. Each instance of your UI displays different content, or displays the same content in a different way. For example, a person can display one instance of the Calendar app showing a specific day, and another showing an entire month.

UIKit communicates details about the current environment using , which reflect a combination of device settings, interface settings, and user preferences. For example, you use traits to detect whether Dark Mode is active for the current view or view controller. Consult [`Adapting your app when traits change`](adapting-your-app-when-traits-change.md) when you want to customize your app based on the current environment, and update it based on trait changes. Review [`Providing data to the view hierarchy with custom traits`](providing-data-to-the-view-hierarchy-with-custom-traits.md) to share data in your view hierarchy using custom traits.

In iOS 18 and later, combine Swift Observation with UIKit’s automatic tracking to update your views automatically when model data changes. Mark your model classes with the `@Observable` macro, then reference observable properties in supported methods. Then, UIKit automatically tracks property access and updates your views when those properties change.

Access device-specific information like battery state, proximity sensor data, and device orientation through [`UIDevice`](uidevice.md), and check status bar configuration using [`UIStatusBarManager`](uistatusbarmanager.md).

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
### Data observation
- [Updating views automatically with observation tracking](updating-views-automatically-with-observation-tracking.md)
  Use Swift Observation and UIKit’s automatic tracking to update your views in response to model data updates.
- [Automatic observation tracking](automatic-observation-tracking.md)
  Simplify updating views when data changes by making updates in methods that support automatic observation tracking.
### Adaptivity and traits
- [Traits and the trait environment](traits-and-the-trait-environment.md)
  Get information about traits and the environment in which your app runs, and share data with your view hierarchy.
- [Responding to changing display modes on Apple TV](responding-to-changing-display-modes-on-apple-tv.md)
  Change images and resources dynamically when the screen gamut on your device changes.
### iPad, Mac, and Apple Vision Pro
- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)
  Optimize your iPad app’s user experience by adopting desktop-class enhancements for multitasking with Stage Manager, document interactions, text editing, search, and more.
- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)
  Provide a compact, ergonomic tab bar for quick access to key parts of your app, and a sidebar for in-depth navigation.
- [Supporting desktop-class features in your iPad app](supporting-desktop-class-features-in-your-ipad-app.md)
  Enhance your iPad app by adding desktop-class features and document support.
- [Multitasking on iPad, Mac, and Apple Vision Pro](multitasking-on-ipad-mac-and-apple-vision-pro.md)
  Implement multitasking APIs to seamlessly integrate your app with iPadOS, macOS, and visionOS.
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