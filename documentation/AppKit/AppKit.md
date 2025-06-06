# AppKit

**Framework**: Appkit  
**Kind**: module

Construct and manage a graphical, event-driven user interface for your macOS app.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

#### Overview

AppKit contains the objects you need to build the user interface for a macOS app. In addition to drawing windows, buttons, panels, and text fields, it handles all the event management and interaction between your app, people, and macOS.

![An image of a MacBook Pro showing Calendar, Maps, and the Dock on the screen.](https://docs-assets.developer.apple.com/published/5dd2fc2d7bcc09ecaf739c3d145f92cd/media-4209947%402x.png)

Aside from drawing and managing interactions, AppKit handles printing, animating, as well as creating documents with large amounts of data efficiently. The framework also contains built-in support for localization and accessibility to ensure that your app reaches as many people as possible.

AppKit also works with [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI), so you can implement parts of your AppKit app in SwiftUI or mix interface elements between the two frameworks. For example, you can place AppKit views and view controllers inside SwiftUI views, and vice versa.

> **Note**:  For information about bringing your iPad app to Mac, see [`Mac Catalyst`](https://developer.apple.com/documentation/UIKit/mac-catalyst). To build an iOS app, you can use SwiftUI to create an app that works across all of Apple’s platforms, or use [`UIKit`](https://developer.apple.com/documentation/UIKit) to create an app for iOS only.

## Topics

### Essentials
- [AppKit updates](../Updates/AppKit.md)
  Learn about important changes to AppKit.
- [Protecting the User’s Privacy](../UIKit/protecting-the-user-s-privacy.md)
  Secure personal data, and respect user preferences for how data is used.
- [Porting your macOS apps to Apple silicon](../Apple-Silicon/porting-your-macos-apps-to-apple-silicon.md)
  Create a version of your macOS app that runs on both Apple silicon and Intel-based Mac computers.
### App Structure
- [App and Environment](app-and-environment.md)
  Learn about the objects that you use to interact with the system.
- [Documents, Data, and Pasteboard](documents-data-and-pasteboard.md)
  Organize your app’s data and preferences, and share that data on the pasteboard or in iCloud.
- [Cocoa Bindings](cocoa-bindings.md)
  Automatically synchronize your data model with your app’s interface using Cocoa Bindings.
- [Resource Management](resource-management.md)
  Manage the storyboards and nib files containing your app’s user interface, and learn how to load data that is stored in resource files.
- [App Extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system.
### User Interface
- [Views and Controls](views-and-controls.md)
  Present your content onscreen and handle user input and events.
- [View Management](view-management.md)
  Manage your user interface, including the size and position of views in a window.
- [View Layout](view-layout.md)
  Position and size views using a stack view or Auto Layout constraints.
- [Appearance Customization](appearance-customization.md)
  Add Dark Mode support to your app, and use appearance proxies to modify your UI.
- [Animation](animation.md)
  Animate your views and other content to create a more engaging experience for users.
- [Windows, Panels, and Screens](windows-panels-and-screens.md)
  Organize your view hierarchies and facilitate their display onscreen.
- [Sound, Speech, and Haptics](sound-speech-and-haptics.md)
  Play sounds and haptic feedback, and incorporate speech recognition and synthesis into your interface.
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
### User Interactions
- [Mouse, Keyboard, and Trackpad](mouse-keyboard-and-trackpad.md)
  Handle events related to mouse, keyboard, and trackpad input.
- [Menus, Cursors, and the Dock](menus-cursors-and-the-dock.md)
  Implement menus and cursors to facilitate interactions with your app, and use your app’s Dock tile to convey updated information.
- [Gestures](gestures.md)
  Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Touch Bar](touch-bar.md)
  Display interactive content and controls in the Touch Bar.
- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [Accessibility for AppKit](accessibility-for-appkit.md)
  Make your AppKit apps accessible to everyone who uses macOS.
### Graphics, Drawing, Color, and Printing
- [Images and PDF](images-and-pdf.md)
  Create and manage images, in bitmap, PDF, and other formats.
- [Drawing](drawing.md)
  Draw shapes, images, and other content on the screen.
- [Color](color.md)
  Represent colors using built-in or custom formats, and give users options for selecting and applying colors.
- [Printing](printing.md)
  Display the system print panels and manage the printing process.
### Text
- [Text Display](text-display.md)
  Display text and check spelling.
- [TextKit](textkit.md)
  Manage text storage and perform custom layout of text-based content in your app’s views.
- [Fonts](fonts.md)
  Manage the fonts used to display text.
- [Writing Tools](writing-tools.md)
  Add support for Writing Tools to your app’s text views.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Review symbols that are no longer supported, and find the replacements to use instead.
### Reference
- [Enumerations](enumerations.md)
  Enumerations for use with multiple classes.
- [Constants](constants.md)
  Constants for use with multiple classes.
- [Data Types](data-types.md)
  Data types for use with multiple classes.
- [Macros](macros.md)
  Macros for use with multiple classes.
### Protocols
- [protocol NSTextSuggestionsDelegate](nstextsuggestionsdelegate.md)
  A protocol for suggestion delegates of text fields to conform to in order to provide text suggestions in response to the user typing.
- [protocol NSViewContentSelectionInfo](nsviewcontentselectioninfo.md)
### Structures
- [struct NSSuggestionItem](nssuggestionitem.md)
  The items that appear in suggestion menus.
- [struct NSSuggestionItemResponse](nssuggestionitemresponse.md)
  Describes the result of a batch of suggestion items from a search
- [struct NSSuggestionItemSection](nssuggestionitemsection.md)
  Describes a section of suggestions items in a suggestions menu
### Variables
- [var NSPasteboardCommunicationError: Int](nspasteboardcommunicationerror.md)
- [var NSPasteboardContentsNotAvailableError: Int](nspasteboardcontentsnotavailableerror.md)
- [var NSPasteboardErrorMaximum: Int](nspasteboarderrormaximum.md)
- [var NSPasteboardErrorMinimum: Int](nspasteboarderrorminimum.md)
- [var NSPasteboardInvalidArgumentError: Int](nspasteboardinvalidargumenterror.md)
- [var NSPasteboardMiscellaneousError: Int](nspasteboardmiscellaneouserror.md)
### Macros
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSViewController)](preview(_:traits:body:)-55ljx.md)
  Preview an NSViewController.
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSView)](preview(_:traits:body:)-7pfjp.md)
  Preview an NSView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit)*