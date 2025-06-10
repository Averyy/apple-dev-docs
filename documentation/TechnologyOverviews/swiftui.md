# SwiftUI apps

**Framework**: Technology Overviews

Build your app for all Apple platforms using the Swift programming language and a modern approach.

[`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) is the best choice for creating new apps, the preferred choice for visionOS apps, and required for watchOS apps. Its declarative programming model and approach to interface construction makes it easier to create and maintain your app’s interface on multiple platforms simultaneously.

![A SwiftUI app running in macOS, iPadOS, and iOS.](https://docs-assets.developer.apple.com/published/ce193ec494e91d4150c3356442824213/landmarks-app-article-hero%402x.png)

#### Assemble Your Apps Core Content

When someone launches your app, your app needs to initialize itself, prepare its interface, check in with the system, begin its main event loop, and start handling events as quickly as possible. When you build your app using SwiftUI, you initialize your app’s custom data and SwiftUI handles the rest.

The main entry point for a SwiftUI app is the [`App`](https://developer.apple.com/documentation/SwiftUI/App) structure. You use this structure to initialize your app’s global data structures. You also use it to declare one or more scenes, where each scene corresponds to part of your app’s interface code. You specify your app’s scenes in the [`body`](https://developer.apple.com/documentation/SwiftUI/App/body-swift.property) property of the app structure. All [`Creating an Xcode project for an app`](https://developer.apple.com/documentation/Xcode/creating-an-xcode-project-for-an-app) contain an initial scene you can modify, and you can [`Bringing multiple windows to your SwiftUI app`](https://developer.apple.com/documentation/swiftui/bringing_multiple_windows_to_your_swiftui_app) as needed to support preference panes, tool palettes, alert panels, and other types of content.

Each of your app’s scenes contains a part of your interface. An app with a single main window can use a [`WindowGroup`](https://developer.apple.com/documentation/SwiftUI/WindowGroup) scene to display that window’s contents. If your app manages documents, you use a [`DocumentGroup`](https://developer.apple.com/documentation/SwiftUI/DocumentGroup) scene to specify contents of the document windows. Each scene contains the views you want to display in a particular window. At launch time, SwiftUI chooses an appropriate scene and displays it.

SwiftUI creates the app structure at launch time, so it’s the only object guaranteed to be present at startup. At startup, initialize the data structures you need to display your app’s initial interface. Keep your initialization code fast to minimize any delays in presenting your interface. If needed, move any noncritical work to background tasks that can finish after your app’s UI appears.

#### Declare Your Interface

[`Declaring a custom view`](https://developer.apple.com/documentation/SwiftUI/Declaring-a-Custom-View) involves telling SwiftUI what views you want to include in each scene, how you want them arranged, and what data each one contains. SwiftUI uses your declarations to build and manage your app’s actual interface. With this approach, your focus stays on [`Make data-driven changes`](swiftui#Make-data-driven-changes.md) and making sure that data is correct. SwiftUI assumes responsibility for your interface and making sure it stays consistent with your data.

An advantage of the declarative approach is that it’s easier to update your interface. Instead of writing code to update your views, you change the associated data and let SwiftUI handle the updates. The declarative approach even makes it easier to [`Animations`](https://developer.apple.com/documentation/SwiftUI/Animations) to your interface. All you have to do is specify which animations you want with only a few lines of code. SwiftUI performs the animations and even responds to interactions and changes while the animations run.

#### Preview Your Content Live

To help you design your views, Xcode provides intuitive design tools to [`Previewing your app’s interface in Xcode`](https://developer.apple.com/documentation/Xcode/previewing-your-apps-interface-in-xcode) while you build it. As you edit the code for your view, Xcode updates the preview next to your code
to reflect the changes you made. This immediate feedback lets you see if those changes match your expectations.

![A screenshot of Xcode with a preview of a SwiftUI view and the code for that view.](https://docs-assets.developer.apple.com/published/f859ffa79e6361cdd3e899766925ae00/swiftui-new-project%402x.png)

Xcode displays previews only when a source file includes a [`Previews in Xcode`](https://developer.apple.com/documentation/SwiftUI/Previews-in-Xcode). This macro tells Xcode what view to create and how to configure it. You can incorporate test data into your previews, and you can configure multiple previews with different content or configurations. You can even see your previews on different device types and with different system appearance settings.

#### Make Data Driven Changes

In SwiftUI, your app’s data model is the source of truth, and the way you modify that data drives your app’s behavior. When building your app’s interface, think about the types of data each view needs. A view might have properties that refer to part of your app’s data model, or have properties that store state information such as the current selection. The [`Model data`](https://developer.apple.com/documentation/SwiftUI/Model-data) you apply to each property declaration tell SwiftUI how to respond when the data in the property changes.

- Apply the [`Environment`](https://developer.apple.com/documentation/SwiftUI/Environment) property wrapper to create a local reference to a value in the [`EnvironmentValues`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues).

The [`Destination Video`](https://developer.apple.com/documentation/visionOS/destination-video) sample demonstrates how you use data to drive interface changes in a multiplatform app. The app uses SwiftUI to support iOS, iPadOS, macOS, tvOS, and visionOS using the same set of views and controls. See how you can build your app once and deploy it on multiple platforms.

#### Handle Events and Interactions

Interactions with your app can come from a variety of sources. On a Mac, people interact with your app primarily using the mouse and keyboard, but they can also use the trackpad of a MacBook Pro, an input tablet, or other input devices. On iPad, people interact by touching the screen, but can also interact with apps using Apple Pencil or a Magic Keyboard. SwiftUI takes all of the events coming from the system and distributes them to the views of your interface and your event-handling code.

SwiftUI also supports many other types of events that you might need to support, including:

- [`Clipboard`](https://developer.apple.com/documentation/SwiftUI/Clipboard) events
- [`Drag and drop`](https://developer.apple.com/documentation/SwiftUI/Drag-and-drop) events
- [`Focus`](https://developer.apple.com/documentation/SwiftUI/Focus)-related events that aid navigation and selection
- [`System events`](https://developer.apple.com/documentation/SwiftUI/System-events) to open URLs and user activity objects, handle background tasks, and import and export transferable data.

#### Explore Other Features

SwiftUI offers additional features to help you create the features you want. Use these features to differentiate your app’s content.

-  Use an [`Immersive spaces`](https://developer.apple.com/documentation/SwiftUI/Immersive-spaces) in your visionOS app to display content outside of a window or volume. Immersive spaces focus the person’s attention on your app’s content, removing other distractions, and optionally filling their field of vision with the content you supply.
-  SwiftUI includes a [`Canvas`](https://developer.apple.com/documentation/SwiftUI/Canvas) view for drawing outlined or filled paths, images, or text. SwiftUI also provides a variety of views that render specific [`Shapes`](https://developer.apple.com/documentation/SwiftUI/Shapes) directly. Use these views to create custom content in your interface.
-  If you already built an app with [`UIKit integration`](https://developer.apple.com/documentation/SwiftUI/UIKit-integration) or [`AppKit integration`](https://developer.apple.com/documentation/SwiftUI/AppKit-integration), create new views using SwiftUI and adopt them incrementally. If you have a SwiftUI app, you can similarly incorporate existing UIKit or AppKit views into your interface.
-  Some system frameworks provide standard views to use when implementing specific features. For example, you might want to adopt the specific button for initiating payments with Apple Pay. For these external views, use the [`Technology-specific views`](https://developer.apple.com/documentation/SwiftUI/Technology-specific-views) that SwiftUI offers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/swiftui)*