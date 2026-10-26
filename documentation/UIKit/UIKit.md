# UIKit

**Framework**: UIKit  
**Kind**: module  
**Role**: Framework

Construct and manage a graphical, event-driven user interface for your iOS, iPadOS, or tvOS app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Mentions

- [About focus interactions for Apple TV](./about-focus-interactions-for-apple-tv.md)
- [Supporting VoiceOver in your app](./supporting-voiceover-in-your-app.md)

#### Overview

UIKit provides a variety of features for building apps, including components you can use to construct the core infrastructure of your iOS, iPadOS, or tvOS apps. The framework provides the window and view architecture for implementing your UI, the event-handling infrastructure for delivering Multi-Touch and other types of input to your app, and the main run loop for managing interactions between the user, the system, and your app.

![An image of the Landmarks sample app on iPad and iPhone showing the Mount Fuji landmark.](https://developer.apple.com/tutorials/images/com.apple.uikit/Landmarks-Building-an-app-with-Liquid-Glass-1@2x.png)

UIKit also includes support for animations, documents, drawing and printing, text management and display, search, app extensions, resource management, and getting information about the current device. You can also customize accessibility support, and localize your app’s interface for different languages, countries, or cultural regions.

UIKit works seamlessly with the [SwiftUI](../SwiftUI/SwiftUI.md) framework, so you can implement parts of your UIKit app in SwiftUI or mix interface elements between the two frameworks. For example, you can place UIKit views and view controllers inside SwiftUI views, and vice versa.

To build a macOS app, you can use [SwiftUI](../SwiftUI/SwiftUI.md) to create an app that works across all of Apple’s platforms, or use [AppKit](../AppKit/AppKit.md) to create an app for Mac only. Alternatively, you can bring your UIKit iPad app to the Mac with [Mac Catalyst](./mac-catalyst.md).

> ❗ **Important**:  Use UIKit classes only from your app’s main thread or main dispatch queue, unless otherwise indicated in the documentation for those classes. This restriction particularly applies to classes that derive from [`UIResponder`](./uiresponder.md) or that involve manipulating your app’s user interface in any way.

## Topics

### Essentials
- [Adopting Liquid Glass](../TechnologyOverviews/adopting-liquid-glass.md)
  Find out how to bring the new material to your app.
- [UIKit updates](../Updates/uikit.md)
  Learn about important changes to UIKit.
- [About app development with UIKit](./about-app-development-with-uikit.md)
  Learn about the basic support that UIKit and Xcode provide for your iOS and tvOS apps.
- [Protecting the User’s Privacy](./protecting-the-user-s-privacy.md)
  Secure personal data, and respect user preferences for how data is used.
### App structure
- [App and environment](./app-and-environment.md)
  Manage life-cycle events and your app’s UI scenes, and get information about traits and the environment in which your app runs.
- [Documents, data, and pasteboard](./documents-data-and-pasteboard.md)
  Organize your app’s data and share that data on the pasteboard.
- [Resource management](./resource-management.md)
  Manage the images, strings, storyboards, and nib files that you use to implement your app’s interface.
- [App extensions](./app-extensions.md)
  Extend your app’s basic functionality to other parts of the system.
- [Interprocess communication](./interprocess-communication.md)
  Display activity-based services to people.
- [Mac Catalyst](./mac-catalyst.md)
  Create a version of your iPad app that users can run on a Mac device.
### User interface
- [Views and controls](./views-and-controls.md)
  Present your content onscreen and define the interactions allowed with that content.
- [View controllers](./view-controllers.md)
  Manage your interface using view controllers and facilitate navigation around your app’s content.
- [View layout](./view-layout.md)
  Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.
- [Appearance customization](./appearance-customization.md)
  Apply Liquid Glass to views, support Dark Mode in your app, customize the appearance of bars, and use appearance proxies to modify your UI.
- [Animation and haptics](./animation-and-haptics.md)
  Provide feedback to users using view-based animations and haptics.
- [Windows and screens](./windows-and-screens.md)
  Provide a container for your view hierarchies and other content.
### User interactions
- [Touches, presses, and gestures](./touches-presses-and-gestures.md)
  Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Menus and shortcuts](./menus-and-shortcuts.md)
  Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.
- [Drag and drop](./drag-and-drop.md)
  Bring drag and drop to your app by using interaction APIs with your views.
- [Pointer interactions](./pointer-interactions.md)
  Support pointer interactions in your custom controls and views.
- [Apple Pencil interactions](./apple-pencil-interactions.md)
  Handle user interactions like double tap and squeeze on Apple Pencil.
- [Focus-based navigation](./focus-based-navigation.md)
  Navigate the interface of your UIKit app using a remote, game controller, or keyboard.
- [Accessibility for UIKit](./accessibility-for-uikit.md)
  Make your UIKit apps accessible to everyone who uses iOS and tvOS.
### Graphics, drawing, and printing
- [Images and PDF](./images-and-pdf.md)
  Create and manage images, including those that use bitmap and PDF formats.
- [Drawing](./drawing.md)
  Configure your app’s drawing environment using colors, renderers, draw paths, strings, and shadows.
- [Printing](./printing.md)
  Display the system print panels and manage the printing process.
### Text
- [Text display and fonts](./text-display-and-fonts.md)
  Display text, manage fonts, and check spelling.
- [TextKit](./textkit.md)
  Manage text storage and perform custom layout of text-based content in your app’s views.
- [Keyboards and input](./keyboards-and-input.md)
  Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.
- [Writing Tools](./writing-tools.md)
  Add support for Writing Tools to your app’s text views.
- [Handwriting recognition](./handwriting-recognition.md)
  Configure text fields and custom views that accept text to handle input from Apple Pencil.
### Reference
- [UIKit Enumerations](./uikit-enumerations.md)
- [UIKit Constants](./uikit-constants.md)
  This document describes constants that are used throughout the UIKit framework.
- [UIKit Data Types](./uikit-data-types.md)
  The UIKit framework defines data types that are used in multiple places throughout the framework.
- [UIKit Functions](./uikit-functions.md)
  The UIKit framework defines a number of functions, many of them used in graphics and drawing operations.
### Deprecated
- [Deprecated symbols](./deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Classes
- [UIBarMinimization](./uibarminimization-c.class.md)
  A configuration that controls how a navigation bar minimizes in response to scrolling.
- [UITraitNavigationTitleAlignment](./uitraitnavigationtitlealignment-c.class.md)
  A trait that reports the alignment the navigation bar resolved for its title.
- [UITraitSystemPrefersReducedResourceUsage](./uitraitsystemprefersreducedresourceusage-c.class.md)
### Variables
- [UIApplicationSystemPrefersReducedResourceUsageDidChangeNotification](./uiapplication/systemprefersreducedresourceusagedidchangenotification.md)
  A notification that posts when [`systemPrefersReducedResourceUsage`](./uiapplication/systemprefersreducedresourceusage.md) changes.
- [UIDocumentDidMoveToWritableLocationNotification](./uidocument/didmovetowritablelocationnotification.md)
  A notification that the document posts when copying the file from a readonly location in order to write changes. This notification will be posted on the file presenter queue.
- [UIDocumentDidMoveToWritableLocationOldURLKey](./uidocument/didmovetowritablelocationoldurlkey.md)
  The key in a `UIDocumentDidMoveToWritableLocationNotification`’s `userInfo` dictionary that contains the previous readonly file URL.
### Macros
- [UIFOCUS_SUPPORTS_UIKIT](./uifocus_supports_uikit.md)
### Enumerations
- [UIGlassEffectStyle](./uiglasseffect/style.md)
- [UIMenuElementImageVisibility](./uimenuelement/imagevisibility.md)
  Visibility options for a menu element’s image.
- [UINavigationItemTitleAlignment](./uinavigationitem/titlealignment-swift.enum.md)
- [UISheetPresentationControllerPlacement](./uisheetpresentationcontroller/placement.md)
- [UITabBarControllerSidebarPlacement](./uitabbarcontroller/sidebar-swift.class/placement.md)
- [UIWritingToolsCoordinatorTextDecoration](./uiwritingtoolscoordinator/textdecoration.md)
  Use the `UIWritingToolsCoordinator.TextDecoration` constants to determine the type of decoration to be applied to a preview for grammar animation. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement the delegate method [`writingToolsCoordinator:requestsPreviewForTextAnimation:ofRange:inContext:textDecoration:completion:`](./uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_,requestspreviewfor,of,in,textdecoration,completion%29.md) to provide both forms of previews, based on the specified decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit)*