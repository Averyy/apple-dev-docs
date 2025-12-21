# App organization

**Framework**: SwiftUI

Define the entry point and top-level structure of your app.

#### Overview

Describe your app’s structure declaratively, much like you declare a view’s appearance. Create a type that conforms to the [`App`](app.md) protocol and use it to enumerate the [`Scenes`](scenes.md) that represent aspects of your app’s user interface.

![None](https://docs-assets.developer.apple.com/published/37814b39f4f1ecc76cd13f967145c10e/app-organization-hero%402x.png)

SwiftUI enables you to write code that works across all of Apple’s platforms. However, it also enables you to tailor your app to the specific capabilities of each platform. For example, if you need to respond to the callbacks that the system traditionally makes on a UIKit, AppKit, or WatchKit app’s delegate, define a delegate object and instantiate it in your app structure using an appropriate delegate adaptor property wrapper, like [`UIApplicationDelegateAdaptor`](uiapplicationdelegateadaptor.md).

For platform-specific design guidance, see [`Getting started`](https://developer.apple.com/design/Human-Interface-Guidelines/getting-started) in the Human Interface Guidelines.

## Topics

### Creating an app
- [Destination Video](../visionOS/destination-video.md)
  Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Hello World](../visionOS/World.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Backyard Birds: Building an app with SwiftData and widgets](backyard-birds-sample.md)
  Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
- [Food Truck: Building a SwiftUI multiplatform app](food-truck-building-a-swiftui-multiplatform-app.md)
  Create a single codebase and app target for Mac, iPad, and iPhone.
- [Fruta: Building a feature-rich app with SwiftUI](../AppClip/fruta-building-a-feature-rich-app-with-swiftui.md)
  Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- [Migrating to the SwiftUI life cycle](migrating-to-the-swiftui-life-cycle.md)
  Use a scene-based life cycle in SwiftUI while keeping your existing codebase.
- [protocol App](app.md)
  A type that represents the structure and behavior of an app.
### Targeting iOS and iPadOS
- [UILaunchScreen](../BundleResources/Information-Property-List/UILaunchScreen.md)
  The user interface to show while an app launches.
- [UILaunchScreens](../BundleResources/Information-Property-List/UILaunchScreens.md)
  The user interfaces to show while an app launches in response to different URL schemes.
- [struct UIApplicationDelegateAdaptor](uiapplicationdelegateadaptor.md)
  A property wrapper type that you use to create a UIKit app delegate.
### Targeting macOS
- [struct NSApplicationDelegateAdaptor](nsapplicationdelegateadaptor.md)
  A property wrapper type that you use to create an AppKit app delegate.
### Targeting watchOS
- [struct WKApplicationDelegateAdaptor](wkapplicationdelegateadaptor.md)
  A property wrapper that is used in `App` to provide a delegate from WatchKit.
- [struct WKExtensionDelegateAdaptor](wkextensiondelegateadaptor.md)
  A property wrapper type that you use to create a WatchKit extension delegate.
### Targeting tvOS
- [Creating a tvOS media catalog app in SwiftUI](creating-a-tvos-media-catalog-app-in-swiftui.md)
  Build standard content lockups and rows of content shelves for your tvOS app.
### Handling system recenter events
- [enum WorldRecenterPhase](worldrecenterphase.md)
  A type that represents information associated with a phase of a system recenter event. Values of this type are passed to the closure specified in View.onWorldRecenter(action:).

## See Also

- [Scenes](scenes.md)
  Declare the user interface groupings that make up the parts of your app.
- [Windows](windows.md)
  Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md)
  Display unbounded content in a person’s surroundings.
- [Documents](documents.md)
  Enable people to open and manage documents.
- [Navigation](navigation.md)
  Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md)
  Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md)
  Provide immediate access to frequently used commands and controls.
- [Search](search.md)
  Enable people to search for text or other content within your app.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system, like by adding a Widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/app-organization)*