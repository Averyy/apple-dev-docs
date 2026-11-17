# Interface fundamentals

**Framework**: Technology Overviews

Explore the components that go into building your app’s interface, and discover platform-specific features that improve the experience you offer to people.

To build your app’s interface, you can use standard system views, draw content yourself, or mix custom drawing with the standard views. Regardless of how you create your content, all interfaces rely on some standard components to present that content:

- *Windows* are the primary containers for your app’s content, and they also facilitate system-related interactions. Every [SwiftUI](../SwiftUI/windows.md), [UIKit](../UIKit/windows-and-screens.md), and [AppKit](../AppKit/windows-panels-and-screens.md) app has at least one [window](https://developer.apple.com/design/human-interface-guidelines/windows), and some platforms let your app display multiple windows simultaneously. Windows in macOS, iPadOS, and visionOS can have a visible border and controls to change the size of the window. Windows in iOS, tvOS, and watchOS have no visible appearance of their own.
- *Scenes* manage instances of your app’s interface in iOS, iPadOS, tvOS, visionOS, and watchOS. Every [SwiftUI](../SwiftUI/scenes.md) and [UIKit](../UIKit/scenes.md) app has at least one scene, and you can create additional scenes to manage distinct experiences. Each scene manages the data for one instance of your interface and any relevant system behaviors. For example, each scene object handles transitions between the foreground and background execution states for that scene. AppKit apps don’t use scenes.
- *Views and controls* display specific types of content in your interface. [SwiftUI](../SwiftUI/SwiftUI.md), [UIKit](../UIKit/views-and-controls.md), and [AppKit](../AppKit/views-and-controls.md) provide views for displaying standard types of content like [images](https://developer.apple.com/design/human-interface-guidelines/image-views), [text](https://developer.apple.com/design/human-interface-guidelines/text-views), [collections](https://developer.apple.com/design/human-interface-guidelines/collections), [pickers](https://developer.apple.com/design/human-interface-guidelines/pickers), [buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), [toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), and much more. They also define the architecture that you use to create custom views and display any content you want.
- *Volumes* are a [specific type](../SwiftUI/volumetricwindowstyle.md) of window that you use to [showcase 2D and 3D content](../visionOS/adding-3d-content-to-your-app.md) in visionOS.

The app-builder technologies you use to create your app maintain a separation between your app’s data and the views and other interface elements you use to display that data. Your data model objects are always the source of truth for your app’s content. When you configure a view, you pass a copy of your data to the view for display purposes. If interactions with a view cause a value to change, your app’s infrastructure is responsible for synchronizing the changes with your data objects. When you use SwiftUI, this process is more automatic, but with UIKit and AppKit you synchronize the changes yourself.

## Manage assets for your interface

Most apps incorporate data from external files into their content. For example, an app’s interface might incorporate images, icons, audio, textures, and other types of content. An app can also store data files with any content, and use them to configure views or other parts of the app. All of these external files are assets for you to manage.

For images in your app’s interface, [use SF Symbols](../UIKit/configuring-and-displaying-symbol-images-in-your-ui.md) whenever possible. The [SF Symbols app](https://developer.apple.com/sf-symbols/) offers a vast collection of configurable, vector-based images that adapt naturally to appearance and size changes. They also blend well with the San Francisco system font, resulting in a consistent look across Apple platforms.

![An image of the SF Symbols app icon.](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/interface-fundamentals-sf-symbols-app-icon@2x.png)

Store images, colors, and appearance-sensitive items in asset catalogs. Interfaces need to adapt to different appearances, including light and dark appearances and accessibility settings for people with visual impairments. [Asset catalogs](./files-and-directories.md#Asset-catalogs) simplify the process of loading these items into your app. Request the item you want and let the asset catalog return the best variant for the device.

Store critical resources inside your app [bundle](./files-and-directories.md#Bundles), and store larger assets on a server and download them later. Your app bundle must contain all of the resources required to launch and run your app. For larger assets that aren’t critical to your app’s execution, store them on the App Store or your own server and download them using the [Background Assets](../BackgroundAssets/BackgroundAssets.md) framework.

To load resource files present in your app bundle:

- Load image assets using the [`Image`](../SwiftUI/image.md) type (SwiftUI), [`UIImage`](../UIKit/uiimage.md) type (UIKit), or [`NSImage`](../AppKit/nsimage.md) type (AppKit). Each type provides methods to load images from a file or asset catalog.
- Load color assets using the [`Color`](../SwiftUI/color.md) type (SwiftUI), [`UIColor`](../UIKit/uicolor.md) type (UIKit), or [`NSColor`](../AppKit/nscolor.md) type (AppKit).
- Locate other resource files in your bundle using the [`Bundle`](../Foundation/bundle.md) type. This type returns the URL for the filename you specify.

## Apply standard behaviors to your interface

There are a few features you always want to build into your interface:

- *Automatic layout*. Size and position the views of your interface using a rules-based approach, which allows your app to adapt automatically to different device sizes and orientations. Automatic layout is integral to SwiftUI, but you must add specific rules to your [UIKit](../UIKit/view-layout.md) and [AppKit](../AppKit/view-layout.md) interfaces.
- *Internationalization*. Prepare your app for localization using the [Foundation](../Foundation/Foundation.md) framework, which provides code to [format strings, dates, times, currencies, and numbers](../Foundation/data-formatting.md) for different languages and regions. Ensure your UI looks good for both left-to-right and [right-to-left](https://developer.apple.com/design/human-interface-guidelines/right-to-left) languages. [Localize](../Xcode/localization.md) app resources and add them to your Xcode project.
- *Accessibility*. Apple builds [accessibility support](../Accessibility/Accessibility.md) into its technologies, and screen readers and other accessibility features use that information to help people navigate your app. Review the default information that [SwiftUI](../SwiftUI/SwiftUI.md), [UIKit](../UIKit/accessibility-for-uikit.md), and [AppKit](../AppKit/accessibility-for-appkit.md) provide and make improvements based on your content. In addition, review your app’s focus-based navigation to make sure it’s simple and intuitive.
- *Undo support*. Identify the actions people take in your app and build tasks that you can easily [undo or redo](../Foundation/undomanager.md).
- *Pasteboard*. Support data exchange in your app and the rest of the system through Cut, Copy, and Paste operations. A pasteboard type in [SwiftUI](../SwiftUI/clipboard.md), [UIKit](../AppKit/documents-data-and-pasteboard.md), and [AppKit](../UIKit/documents-data-and-pasteboard.md) manages the content you transfer to it.

## Consider platform-specific behaviors in your design

When making decisions about how to build your interface, the platform you target affects some of the decisions you must make. Some features might impact your interface on one platform, but not on others. The following table lists the types of decisions to consider, and the support each platform offers.

| Feature | iOS | iPadOS | macOS | tvOS | visionOS | watchOS |
| --- | --- | --- | --- | --- | --- | --- |
| Supported app-builder technologies | SwiftUI, UIKit | SwiftUI, UIKit | SwiftUI, AppKit | SwiftUI, UIKit, [TVUIKit](../TVUIKit/TVUIKit.md) | SwiftUI, UIKit | SwiftUI |
| Full-screen content mode | Yes | Yes | Available | Yes | Available | Yes |
| [Dark Mode](../UIKit/supporting-dark-mode-in-your-interface.md) | Yes | Yes | Yes | Yes | No | No |
| [Dynamic Type](../UIKit/scaling-fonts-automatically.md) | Yes | Yes | No | No | Yes | Yes |
| Multiple windows support | Yes* | Yes | Yes | No | Yes | No |
| Menu types | Context | Main, context | Main, context, Dock | None | Main, context | None |
| Primary interaction type | Touch | Touch, Apple Pencil, Magic Keyboard | Mouse, keyboard | Siri Remote | Eyes, hands | Touch, Digital Crown |
| Bluetooth keyboard support | Yes | Yes | Yes | No | Yes | No |
| Background task availability | Limited | Limited | Yes | No | Limited | No |
| [CarPlay](../CarPlay/CarPlay.md) support | Yes | No | No | No | No | No |

* - iOS supports multiple windows when an external display is connected.

## Related articles

- [Preparing your app for iPhone Duo](./preparing-your-app-for-iphone-duo.md)
  Update your iOS app to dynamically resize for inner and outer displays, adjust your layout for the folding display, and adapt bars for vertical layout.

## Topics

### Interface design
- [Preparing your app for iPhone Duo](./preparing-your-app-for-iphone-duo.md)
  Update your iOS app to dynamically resize for inner and outer displays, adjust your layout for the folding display, and adapt bars for vertical layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/interface-fundamentals)*