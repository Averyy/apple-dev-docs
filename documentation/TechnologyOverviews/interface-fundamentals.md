# Interface fundamentals

**Framework**: Technology Overviews

Explore the components that go into building your app’s interface, and discover platform-specific features that improve the experience you offer to people.

To build your app’s interface, you can use standard system views, draw content yourself, or mix custom drawing with the standard views. Regardless of how you create your content, all interfaces rely on some standard components to present that content:

-  are the primary containers for your app’s content, and they also facilitate system-related interactions. Every [`Windows`](https://developer.apple.com/documentation/SwiftUI/Windows), [`Windows and screens`](https://developer.apple.com/documentation/UIKit/windows-and-screens), and [`Windows, Panels, and Screens`](https://developer.apple.com/documentation/AppKit/windows-panels-and-screens) app has at least one [`Windows`](https://developer.apple.com/design/Human-Interface-Guidelines/windows), and some platforms let your app display multiple windows simultaneously. Windows in macOS, iPadOS, and visionOS can have a visible border and controls to change the size of the window. Windows in iOS, tvOS, and watchOS have no visible appearance of their own.
-  manage instances of your app’s interface in iOS, iPadOS, tvOS, visionOS, and watchOS. Every [`Scenes`](https://developer.apple.com/documentation/SwiftUI/Scenes) and [`Scenes`](https://developer.apple.com/documentation/UIKit/scenes) app has at least one scene, and you can create additional scenes to manage distinct experiences. Each scene manages the data for one instance of your interface and any relevant system behaviors. For example, each scene object handles transitions between the foreground and background execution states for that scene. AppKit apps don’t use scenes.
-  display specific types of content in your interface. [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI), [`Views and controls`](https://developer.apple.com/documentation/UIKit/views-and-controls), and [`Views and Controls`](https://developer.apple.com/documentation/AppKit/views-and-controls) provide views for displaying standard types of content like [`Image views`](https://developer.apple.com/design/Human-Interface-Guidelines/image-views), [`Text views`](https://developer.apple.com/design/Human-Interface-Guidelines/text-views), [`Collections`](https://developer.apple.com/design/Human-Interface-Guidelines/collections), [`Pickers`](https://developer.apple.com/design/Human-Interface-Guidelines/pickers), [`Buttons`](https://developer.apple.com/design/Human-Interface-Guidelines/buttons), [`Toggles`](https://developer.apple.com/design/Human-Interface-Guidelines/toggles), and much more. They also define the architecture that you use to create custom views and display any content you want.
-  are a [`VolumetricWindowStyle`](https://developer.apple.com/documentation/SwiftUI/VolumetricWindowStyle) of window that you use to [`Adding 3D content to your app`](https://developer.apple.com/documentation/visionOS/adding-3d-content-to-your-app) in visionOS.

The app-builder technologies you use to create your app maintain a separation between your app’s data and the views and other interface elements you use to display that data. Your data model objects are always the source of truth for your app’s content. When you configure a view, you pass a copy of your data to the view for display purposes. If interactions with a view cause a value to change, your app’s infrastructure is responsible for synchronizing the changes with your data objects. When you use SwiftUI, this process is more automatic, but with UIKit and AppKit you synchronize the changes yourself.

#### Choose a Design Approach for the Target Platform

The platform you target naturally affects the approach you take to building your interface. You want apps to feel like they belong on a given platform, which might require you to tweak your interface on each platform.

##### Ios and Ipados

Design [`Designing for iOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-ios) and [`Designing for iPadOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-ipados) apps as experiences people can take with them anywhere. Apps in iOS fill the screen, and apps in iPadOS need to be flexible enough to fill all or part of the screen. Because space is more constrained, interfaces make greater use of [`Layout and organization`](https://developer.apple.com/design/Human-Interface-Guidelines/layout-and-organization) and [`Navigation and search`](https://developer.apple.com/design/Human-Interface-Guidelines/navigation-and-search) elements to organize content.

iOS and iPadOS apps need to handle different iPhone and iPad sizes and orientations gracefully. Make sure your app’s interface adjusts automatically to size changes. In SwiftUI, automatic layout is an integral part of the interface-creation process. In UIKit, adopt [`View layout`](https://developer.apple.com/documentation/UIKit/view-layout) to adjust your interface at appropriate times. Take advantage of the Xcode interface editors so you can see how your interface looks in different configurations.

On iPad, don’t forget to support features that people can access from Magic Keyboard and Apple Pencil. Magic Keyboard adds pointer-based navigation, [`Menus`](https://developer.apple.com/design/Human-Interface-Guidelines/menus), and hover-based interactions. Apple Pencil enables [`Handling input from Apple Pencil`](https://developer.apple.com/documentation/UIKit/handling-input-from-apple-pencil) and also lets you capture altitude, azimuth, and pressure information, which a drawing app can use for content creation.

##### Macos

[`Designing for macOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-macos) app to take advantage of the power, space, and flexibility of a Mac. Mac gives you more space for your content, but that doesn’t mean you want a cluttered interface. Take advantage of the same [`Navigation and search`](https://developer.apple.com/design/Human-Interface-Guidelines/navigation-and-search) techniques as other platforms to create interfaces that present what people need when they need it.

Make sure your windows support flexible layouts and adapt to different sizes and modes. In SwiftUI, automatic layout is an integral part of the interface-creation process. In AppKit, adopt [`View Layout`](https://developer.apple.com/documentation/AppKit/view-layout) to adjust your interface at appropriate times. Adopt [`Going full screen`](https://developer.apple.com/design/Human-Interface-Guidelines/going-full-screen) mode for windows to give people the option to view your app in a distraction-free environment.

The menu bar along the top of the desktop displays your app’s menus. Identify your app’s relevant actions, and craft [`Menus`](https://developer.apple.com/design/Human-Interface-Guidelines/menus) that reflect how people interact with your content.

##### Tvos

[`Designing for tvOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-tvos) with [`Focus and selection`](https://developer.apple.com/design/Human-Interface-Guidelines/focus-and-selection) in mind. Most interactions with your app occur through the [`Remotes`](https://developer.apple.com/design/Human-Interface-Guidelines/remotes). People use the directional buttons on the remote to change focus from one part of your UI to another. They then use the select button to act on the focused item, or the Menu button to navigate back to the previous screen. Make navigation as straightforward as possible, and minimize text input and other complex interactions.

[`Lockups`](https://developer.apple.com/design/Human-Interface-Guidelines/lockups) are one way to simplify navigation and promote consistency among similar items in your UI. A lockup is a group of related views that you combine into a single, selectable element. For example, a movie lockup might include the movie’s title, description, cast list, and poster image. When someone selects a movie, tvOS places focus on the entire lockup instead of on individual items.

##### Visionos

[`Designing for visionOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-visionos) around an initial window to provide a familiar starting point for interactions. Add depth-based offsets to specific views to emphasize parts of your window, or to indicate a change in modality. [`Adding 3D content to your app`](https://developer.apple.com/documentation/visionOS/adding-3d-content-to-your-app) directly into your view layouts to place them side by side with your 2D views. Add [`Input and event modifiers`](https://developer.apple.com/documentation/SwiftUI/View-Input-and-Events) to highlight elements when someone looks at them. Place frequently used tools and commands on the outside edge of your windows using [`ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`](https://developer.apple.com/documentation/SwiftUI/View/ornament(visibility:attachmentAnchor:contentAlignment:ornament:)).

Showcase your app’s 3D content by [`Adding 3D content to your app`](https://developer.apple.com/documentation/visionOS/adding-3d-content-to-your-app), or add a Full Space to [`Creating fully immersive experiences in your app`](https://developer.apple.com/documentation/visionOS/creating-fully-immersive-experiences). Build and animate your app’s 3D content as [`USD Assets`](https://developer.apple.com/documentation/RealityKit/realitykit-usd-assets) and incorporate them into your scenes using [`RealityKit`](https://developer.apple.com/documentation/RealityKit).

##### Watchos

[`Designing for watchOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-watchos) to deliver only the most relevant content in a timely manner. Be prepared to [`Supporting multiple watch sizes`](https://developer.apple.com/documentation/watchOS-Apps/supporting-multiple-watch-sizes), ranging from 38mm to 45mm. On Apple Watch models that [`Designing your app for the Always On state`](https://developer.apple.com/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state), be prepared to keep your app’s content up-to-date. In addition to the app you build, support the following additional interfaces:

-  elevate a small amount of timely, personally relevant information, and display it where people can see it at a glance. On Apple Watch, widgets appear in [`Increasing the visibility of widgets in Smart Stacks`](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks).
-  are small visual elements that appear on the watch face in predefined areas. Use them to display your app’s most crucial information, and to help people engage with your app’s content. [`Creating accessory widgets and watch complications`](https://developer.apple.com/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications) using the [`WidgetKit`](https://developer.apple.com/documentation/WidgetKit) framework and deliver them with your app.
-  display time-sensitive information, using haptics, sound, and visual cues to get the person’s attention. [`Notifications`](https://developer.apple.com/documentation/watchOS-Apps/notifications) locally from your app, or push notifications to Apple Watch remotely from a server. Provide a [`User Notifications UI`](https://developer.apple.com/documentation/UserNotificationsUI) to incorporate custom content, images, or media.

#### Manage Assets for Your Interface

Store images, colors, and appearance-sensitive items in asset catalogs. Interfaces need to adapt to different appearances, including light and dark appearances and accessibility settings for people with visual impairments. [`Asset catalogs`](files-and-directories#Asset-catalogs.md) simplify the process of loading these items into your app. Request the item you want and let the asset catalog return the best variant for the device.

Store critical resources inside your app [`Bundles`](files-and-directories#Bundles.md), and store larger assets on a server and download them later. Your app bundle must contain all of the resources required to launch and run your app. For larger assets that aren’t critical to your app’s execution, store them on the App Store or your own server and download them using the [`Background Assets`](https://developer.apple.com/documentation/BackgroundAssets) framework.

To load resource files present in your app bundle:

- Load image assets using the [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) type (SwiftUI), [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) type (UIKit), or [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) type (AppKit). Each type provides methods to load images from a file or asset catalog.
- Load color assets using the [`Color`](https://developer.apple.com/documentation/SwiftUI/Color) type (SwiftUI), [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) type (UIKit), or [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) type (AppKit).
- Locate other resource files in your bundle using the [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) type. This type returns the URL for the filename you specify.

#### Apply Standard Behaviors to Your Interface

There are a few features you always want to build into your interface:

- . Size and position the views of your interface using a rules-based approach, which allows your app to adapt automatically to different device sizes and orientations. Automatic layout is integral to SwiftUI, but you must add specific rules to your [`View layout`](https://developer.apple.com/documentation/UIKit/view-layout) and [`View Layout`](https://developer.apple.com/documentation/AppKit/view-layout) interfaces.
- . Prepare your app for localization using the [`Foundation`](https://developer.apple.com/documentation/Foundation) framework, which provides code to [`Data Formatting`](https://developer.apple.com/documentation/Foundation/data-formatting) for different languages and regions. Ensure your UI looks good for both left-to-right and [`Right to left`](https://developer.apple.com/design/Human-Interface-Guidelines/right-to-left) languages. [`Localization`](https://developer.apple.com/documentation/Xcode/localization) app resources and add them to your Xcode project.
- . Apple builds [`Accessibility`](https://developer.apple.com/documentation/Accessibility) into its technologies, and screen readers and other accessibility features use that information to help people navigate your app. Review the default information that [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI), [`Accessibility for UIKit`](https://developer.apple.com/documentation/UIKit/accessibility-for-uikit), and [`Accessibility for AppKit`](https://developer.apple.com/documentation/AppKit/accessibility-for-appkit) provide and make improvements based on your content. In addition, review your app’s focus-based navigation to make sure it’s simple and intuitive.
- . Identify the actions people take in your app and build tasks that you can easily [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager).
- . Support data exchange in your app and the rest of the system through Cut, Copy, and Paste operations. A pasteboard type in [`Clipboard`](https://developer.apple.com/documentation/SwiftUI/Clipboard), [`Documents, Data, and Pasteboard`](https://developer.apple.com/documentation/AppKit/documents-data-and-pasteboard), and [`Documents, data, and pasteboard`](https://developer.apple.com/documentation/UIKit/documents-data-and-pasteboard) manages the content you transfer to it.

#### Consider Platform Specific Behaviors in Your Design

When making decisions about how to build your interface, the platform you target affects some of the decisions you must make. Some features might impact your interface on one platform, but not on others. The following table lists the types of decisions to consider, and the support each platform offers.

| Feature | iOS | iPadOS | macOS | tvOS | visionOS | watchOS |
| --- | --- | --- | --- | --- | --- | --- |
| Supported app-builder technologies | SwiftUI, UIKit | SwiftUI, UIKit | SwiftUI, AppKit | SwiftUI, UIKit, [`TVUIKit`](https://developer.apple.com/documentation/TVUIKit) | SwiftUI, UIKit | SwiftUI |
| Full-screen content mode | Yes | Yes | Available | Yes | Available | Yes |
| [`Supporting Dark Mode in your interface`](https://developer.apple.com/documentation/UIKit/supporting-dark-mode-in-your-interface) | Yes | Yes | Yes | Yes | No | No |
| [`Scaling Fonts Automatically`](https://developer.apple.com/documentation/UIKit/scaling-fonts-automatically) | Yes | Yes | No | No | Yes | Yes |
| Multiple windows support | Yes* | Yes | Yes | No | Yes | No |
| Menu types | Context | Main, context | Main, context, Dock | None | Main, context | None |
| Primary interaction type | Touch | Touch, Apple Pencil, Magic Keyboard | Mouse, keyboard | Siri Remote | Eyes, hands | Touch, Digital Crown |
| Bluetooth keyboard support | Yes | Yes | Yes | No | Yes | No |
| Background task availability | Limited | Limited | Yes | No | Limited | No |
| [`CarPlay`](https://developer.apple.com/documentation/CarPlay) support | Yes | No | No | No | No | No |

* - iOS supports multiple windows when an external display is connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/interface-fundamentals)*