# Apps

**Framework**: Technology Overviews

Offer custom features and services on Apple platforms using apps.

When you develop software for Apple platforms, start with an app and add [experiences](./system-experiences.md) to it later. Apps run natively on an Apple device to give people access to your company’s services or help people manage their information. On most platforms, people discover and install apps using the App Store.

Create apps using the app-builder technology that suits your development style. Apple offers several different app-builder technologies, which support different programming models and different Apple platforms:

- **SwiftUI** is the recommended technology for [building apps on all Apple platforms](./building-your-apps-content-with-swiftui.md) With SwiftUI, you build your app’s interface and content using a declarative programming model, in which you describe the behaviors and appearance you want, and SwiftUI handles the rest. To change your interface, modify the data variables driving the state of each view. SwiftUI detects these changes and updates views automatically, and can even animate the changes in the process.
- **UIKit** offers a traditional, object-oriented approach to [building apps](./building-your-apps-content-with-uikit-appkit.md) to run in [iOS](https://developer.apple.com/ios/), [iPadOS](https://developer.apple.com/ipados/), [tvOS](https://developer.apple.com/tvos/), [visionOS](https://developer.apple.com/visionos/), and even [macOS](../UIKit/mac-catalyst.md). Assemble your app from a library of objects, and write custom code to change your app’s interface and data.
- **AppKit** offers a traditional, object-oriented approach to [building apps](./building-your-apps-content-with-uikit-appkit.md) to run in [macOS](https://developer.apple.com/macos/). Assemble your app from a library of objects, and write custom code to change your app’s interface and data.

Regardless of the app-builder technology you choose, separate your [app’s data](./data-management.md) and the [interface](./interface.md) you use to display the data. Your data model includes the data structures you use to store information, and the logic you use to change the data. Your app’s interface is the visual expression of the data your app manages. App-builder technologies focus primarily on creating and managing your interface, handling input and other events, and managing interactions between your app and the system.

Build apps for the Apple platforms you want to support, taking advantage of the strengths of each platform. Each Apple device comes with specific hardware and software capabilities, along with frameworks to help you take advantage of those capabilities in your apps. Incorporate the technologies that make sense for your app’s content, and follow the guidance for each technology to ensure your app runs smoothly. For design guidance, consult the [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines).

## iOS and iPadOS

![An image of the landmarks app on iPhone and iPad.](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/interface-fundamentals-ios-landmarks@2x.png)

Build an [iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios) or [iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados) app people can take with them anywhere. Apps on iPhone and iPad help people get things done, access important or personal information, connect to your company’s products and services, entertain themselves, or perform many other types of tasks.

iOS and iPadOS apps can take advantage of many features unique to iPhone and iPad. Interactions with your app rely on touch and [Apple Pencil](../UIKit/handling-input-from-apple-pencil.md) input, which people use to interact directly with your content. Apps have access to [sensor data](./device-sensors.md) that can offer better awareness of the person’s location, the device’s orientation, and other details. On iPad, Magic Keyboard augments touch interactions with pointer-based navigation, [menu support](https://developer.apple.com/design/human-interface-guidelines/menus), and hover-based interactions. Other [system features](./apple-experiences.md) help you build your app’s core features or extend the reach of your data.

iPhone and iPad come in different sizes, and people can hold the device in a portrait or landscape orientation. To account for these differences, design your interface to adapt gracefully to any size. If you build your app with SwiftUI, these types of adaptations are built-in and require little extra work on your part. If you build your app with UIKit, add [Auto Layout constraints](../UIKit/view-layout.md) to specify the rules for how to update your interface. Device sizes also affect how you [lay out](https://developer.apple.com/design/human-interface-guidelines/layout-and-organization) your content and help people [navigate](https://developer.apple.com/design/human-interface-guidelines/navigation-and-search) it.

## macOS

![An image of the landmarks app on Mac.](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/interface-fundamentals-macos-landmarks@2x.png)

[Build a macOS app](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) to take advantage of the computational and graphics power of the Mac, and the extra space available to display your content. People use their Mac at home or work when they’re generally stationary, and perform tasks that require time or are easy to do with a mouse, trackpad, or keyboard. Create apps to support in-depth productivity tasks, play media or games, or take advantage of the larger display on Mac.

macOS apps often have plenty of space for displaying content. Apps can have multiple windows open simultaneously for different documents or tasks. People can drag content between an app’s windows, or between windows of different apps, to exchange data. Apps also have custom [menus](https://developer.apple.com/design/human-interface-guidelines/menus) to make frequently used commands readily accessible.

In macOS, windows have visible boundaries and optional controls so people can resize them, including [filling the entire display](https://developer.apple.com/design/human-interface-guidelines/going-full-screen) with a window’s content. macOS supports the same [navigation](https://developer.apple.com/design/human-interface-guidelines/navigation-and-search) techniques as other platforms, but with layout metrics suited for mouse and trackpad interactions. Make sure your interface handles size changes gracefully. If you build your app with SwiftUI, these types of adaptations are built-in and require little extra work on your part. If you build your app with AppKit, add [Auto Layout constraints](../AppKit/view-layout.md) to specify the rules for how to update your interface.

## tvOS

![An image of the Home Screen on a tvOS device.](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/interface-fundamentals-tvos-home-screen@2x.png)

[Build a tvOS app](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos) to deliver content to someone’s living room. Apps appear on the person’s television, which offers a large, high-resolution display with plenty of space for your custom content. Most apps play media, but you can also create apps to support fitness, games, education, and support for home-related tasks.

On Apple TV, create vibrant content that makes best use of the large television display. Embrace the [focus-based](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) navigation approach that relies primarily on the [Siri Remote](https://developer.apple.com/design/human-interface-guidelines/remotes), but don’t forget to support [game controllers](https://developer.apple.com/design/human-interface-guidelines/game-controls) and [voice-based interactions](https://developer.apple.com/design/human-interface-guidelines/siri) too. [Lockups](https://developer.apple.com/design/human-interface-guidelines/lockups) help you create more navigable content by combining multiple views into a single, selectable element. For example, a movie lockup might show the movie’s title, description, cast list, and post image in a single element.

## visionOS

![An illustration of a person wearing an Apple Vision Pro and viewing windows and a volume.](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/vision-conceptual.png)

[Build a visionOS app](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos) to deliver your app’s content with different levels of immersion. With [Passthrough](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences), visionOS integrates your content into person’s surroundings by mixing it with live video. Other immersion levels replace some or all of the person’s surroundings with digital content you provide.

visionOS apps offer the best environment for displaying 3D content through the stereoscopic displays of Apple Vision Pro. Display your app’s initial content in a traditional window to provide a safe and familiar starting point for interactions. Showcase 3D content in [a volume](../visionOS/adding-3d-content-to-your-app.md), a three-dimensional window you fill with content, to make it feel integral to the person’s environment. For fully immersive experiences, transition to a [Full Space](../visionOS/creating-fully-immersive-experiences.md) and use it to draw everything the person sees.

People [interact with content in visionOS](../visionOS/visionOS.md) primarily using eye movements and hand gestures, but can also perform interactions with connected Bluetooth input devices. Add [hover effects](../SwiftUI/view-input-and-events.md) to views to highlight the items people look at. Place frequently used tools and commands on the outside edge of your windows using [ornaments](../SwiftUI/view/ornament%28visibility,attachmentanchor,contentalignment,ornament%29.md).

If you work extensively with 3D content, visionOS offers integral support for [USD assets](../USD/creating-usd-files-for-apple-devices.md). Create these assets using your preferred tools and use [Reality Composer Pro](../RealityComposerPro/RealityComposerPro.md) and [RealityKit](../RealityKit/RealityKit.md) to integrate them into your app’s immersive scenes.

## watchOS

![An image of a widget in a Smart Stack on Apple Watch.](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/interface-fundamentals-watchos-smart-stack@2x.png)

![An image of a watch face with several complications on Apple Watch.](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/watch-complications-screenshot@2x.png)

![An image of the Workout app on Apple Watch.](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/interface-fundamentals-watchos-outdoor-run-workout@2x.png)

[Build a watchOS app](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos) to deliver highly relevant content in a timely manner. In watchOS, apps offer a familiar place to access content, and [system experiences](./system-experiences.md) offer flexible ways to access the same content:

- [*Widgets*](./system-experiences.md#Widgets) elevate a small amount of timely, personally relevant information, and display it where people can see it at a glance. On Apple Watch, widgets appear in [Smart Stacks](../WidgetKit/widget-suggestions-in-smart-stacks.md).
- [*Complications*](./system-experiences.md#Watch-complications) are small visual elements that appear on the watch face in predefined areas. Use them to display your app’s most crucial information, and to help people engage with your app’s content. [Build them](../WidgetKit/creating-accessory-widgets-and-watch-complications.md) using the [WidgetKit](../WidgetKit/WidgetKit.md) framework and deliver them with your app.
- [*Notifications*](./communication-and-connection.md#Keep-people-informed-with-notifications) display time-sensitive information, using haptics, sound, and visual cues to get the person’s attention. [Create notifications](../watchOS-Apps/notifications.md) locally from your app, or push notifications to Apple Watch remotely from a server. Provide a [custom interface](../UserNotificationsUI/UserNotificationsUI.md) to incorporate custom content, images, or media.

Plan to [support different sizes of Apple Watch](../watchOS-Apps/supporting-multiple-watch-sizes.md), ranging from 38mm to 45mm. On Apple Watch models that [support the Always-On display](../watchOS-Apps/designing-your-app-for-the-always-on-state.md), be prepared to update your app’s content regularly so that it’s always fresh.

## Related articles

- [Building your app’s content with SwiftUI](./building-your-apps-content-with-swiftui.md)
  Build your app for all Apple platforms using the Swift programming language and a modern approach.
- [Building your app’s content with UIKit and AppKit](./building-your-apps-content-with-uikit-appkit.md)
  Build your app using a traditional design approach and the Swift or Objective-C programming language.

## Topics

### App creation
- [Building your app’s content with SwiftUI](./building-your-apps-content-with-swiftui.md)
  Build your app for all Apple platforms using the Swift programming language and a modern approach.
- [Building your app’s content with UIKit and AppKit](./building-your-apps-content-with-uikit-appkit.md)
  Build your app using a traditional design approach and the Swift or Objective-C programming language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/apps)*