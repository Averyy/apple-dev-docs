# App design and UI

**Framework**: Technology Overviews

Choose a programming approach to build your app, create your app’s interface, and implement the fundamental behaviors that your app requires.

At the start of every new project, you need to choose an app-builder technology to use for your initial code. App-builder technologies define the programming approach you take for your app’s interface, event-handling code, and other behaviors. You can choose one of these programming approaches for your app, or combine the approaches.

Each platform defines the overall look for views and controls, and your app-builder technology determines how you create and manage your interface. Build your interface with standard views and controls, a mixture of standard and custom views, or entirely custom content.

[SwiftUI](../SwiftUI/SwiftUI.md) is the best option when you’re learning to program for Apple platforms, or when you want to create a new app. With SwiftUI, you build your app’s interface and content using a declarative programming model. With this model, you describe the behaviors and appearance you want, and SwiftUI creates and manages the interface for you. Changes are data driven, so when you update variables that affect the state of a view, SwiftUI refreshes your interface for you.

Use SwiftUI to build apps for [iOS](https://developer.apple.com/ios/), [iPadOS](https://developer.apple.com/ipados/), [macOS](https://developer.apple.com/macos/), [tvOS](https://developer.apple.com/tvos/), [visionOS](https://developer.apple.com/visionos/), and [watchOS](https://developer.apple.com/watchos/) and the [Swift](https://www.swift.org) programming language.

- Build apps and widgets using a declarative programming model and data-driven changes.
- Build your interface, and incorporate features like custom drawing and text editing.
- See live previews of your interface as you write the code for your views.
- Incorporate existing UIKit or AppKit views and view controllers into your interface.

![](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/SwiftUI-apps.png)

#### SwiftUI apps

[Read about SwiftUI](./swiftui.md)

[UIKit](../UIKit/UIKit.md) and [AppKit](../AppKit/AppKit.md) offer a more traditional, object-oriented approach to building apps. These frameworks provide a library of objects that you assemble and customize to achieve the behavior you want. For example, you assemble your interface from standard and custom views and place the logic for managing view interactions in custom controller objects. Each object manages its own behavior, and your custom code defines the overall behavior of your app.

Use UIKit to build apps for [iOS](https://developer.apple.com/ios/), [iPadOS](https://developer.apple.com/ipados/), [tvOS](https://developer.apple.com/tvos/), [visionOS](https://developer.apple.com/visionos/), and [Mac Catalyst](../UIKit/mac-catalyst.md). Use AppKit to build apps for [macOS](https://developer.apple.com/macos/). Build your app using either [Swift](https://www.swift.org) or the Objective-C programming language.

- Build apps using a library of objects and a model-view-controller architecture.
- Build your interface, and incorporate features like custom drawing and rich-text editing.
- Assemble your app’s view hierarchies using Xcode’s visual editor.
- Adopt SwiftUI views incrementally in your view hierarchies.

![](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/UIKit-and-AppKit-apps.png)

#### UIKit and AppKit apps

[Read about UIKit and AppKit](./uikit-appkit.md)

No matter which app-builder technology you choose, most of the components you use to build your interface are the same. Before you build your interface, learn about the different components available to you, and learn how different platforms use those components. You can also learn about other technologies that impact the design of your interface and how you display content.

- Learn about the windows, views, and other visual elements available to you.
- Explore the design approaches for each platform, and learn how to make your app stand out.
- Manage app-related assets, and learn how to load them locally or from a remote server.
- Support common features like internationalization, accessibility, undo and redo, and the pasteboard.
- Adapt iOS apps for dynamic resizing, vertical controls, and multiple displays on iPhone Duo. Read more at [Preparing your app for iPhone Duo](./preparing-your-app-for-iphone-duo.md).

![](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/window-based-interfaces.png)

#### Interface fundamentals

[Read about interface fundamentals](./interface-fundamentals.md)

Interfaces across Apple platforms feature a new dynamic material called Liquid Glass, which combines the optical properties of glass with a sense of fluidity. Learn how to leverage Liquid Glass to make sure your interface looks right at home on Apple platforms.

- Embrace the visual refresh for materials, controls, and app icons.
- Provide a universal navigation and search experience across platforms.
- Ensure your interface’s organization and layout looks consistent with other apps and system experiences.
- Adopt best practices for windows, modals, menus, and toolbars.
- Test your app to provide a great experience across platforms.

![](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/liquid-glass-technology-overview-thumbnail.png)

#### Liquid Glass

[Read about Liquid Glass](./liquid-glass.md)

## Topics

### App builder
- [SwiftUI apps](./swiftui.md)
  Build your app for all Apple platforms using the Swift programming language and a modern approach.
- [UIKit and AppKit apps](./uikit-appkit.md)
  Build your app using a traditional design approach and the Swift or Objective-C programming language.
### Interface
- [Interface fundamentals](./interface-fundamentals.md)
  Explore the components that go into building your app’s interface, and discover platform-specific features that improve the experience you offer to people.
- [Preparing your app for iPhone Duo](./preparing-your-app-for-iphone-duo.md)
  Update your iOS app to dynamically resize for inner and outer displays, adjust your layout for the folding display, and adapt bars for vertical layout.
- [Liquid Glass](./liquid-glass.md)
  Learn how to design and develop beautiful interfaces that leverage Liquid Glass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/app-design-and-ui)*