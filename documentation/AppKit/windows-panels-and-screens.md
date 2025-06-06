# Windows, Panels, and Screens

**Framework**: AppKit

Organize your view hierarchies and facilitate their display onscreen.

## Topics

### Windows
- [class NSWindow](nswindow.md)
  A window that an app displays on the screen.
- [class NSPanel](nspanel.md)
  A special kind of window that typically performs a function that is auxiliary to the main window.
- [protocol NSWindowDelegate](nswindowdelegate.md)
  A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.
- [class NSWindowTab](nswindowtab.md)
  A tab associated with a window that is part of a tabbing group.
- [class NSWindowTabGroup](nswindowtabgroup.md)
  A group of windows that display together as a single tabbed window.
### Window Restoration
- [protocol NSWindowRestoration](nswindowrestoration.md)
  A set of methods that restoration classes must implement to handle the recreation of windows.
- [protocol NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
  A set of methods used to associate a unique identifier with objects in your user interface.
### Screens
- [class NSScreen](nsscreen.md)
  An object that describes the attributes of a computer’s monitor or screen.
### Popovers
- [class NSPopover](nspopover.md)
  A means to display additional content related to existing content on the screen.
- [protocol NSPopoverDelegate](nspopoverdelegate.md)
  A set of optional methods that a popover delegate can implement to provide additional or custom functionality.
### Alerts
- [class NSAlert](nsalert.md)
  A modal dialog or sheet attached to a document window.
- [protocol NSAlertDelegate](nsalertdelegate.md)
  A set of optional methods implemented by the delegate of an [`NSAlert`](nsalert.md) object to respond to a user’s request for help.
### Open and Save Panels
- [class NSOpenPanel](nsopenpanel.md)
  A panel that prompts the user to select a file to open.
- [class NSSavePanel](nssavepanel.md)
  A panel that prompts the user for information about where to save a file.
- [protocol NSOpenSavePanelDelegate](nsopensavepaneldelegate.md)
  A set of methods for managing interactions with an open or save panel.
### Share Panel
- [class NSSharingServicePicker](nssharingservicepicker.md)
  A list of sharing services that the user can choose from.
- [protocol NSPreviewRepresentableActivityItem](nspreviewrepresentableactivityitem.md)
  An interface you adopt in custom objects that you want to share using the macOS share sheet.
- [class NSPreviewRepresentingActivityItem](nspreviewrepresentingactivityitem.md)
  A type that adds metadata to an item you share using the macOS share sheet.
### Print and PDF Panels
- [class NSPDFPanel](nspdfpanel.md)
  A Save or Export as PDF panel that’s consistent with the macOS user interface.
- [protocol NSPrintPanelAccessorizing](nsprintpanelaccessorizing.md)
  A set of methods that a Print panel object can use to get information from a printing accessory controller.
### Color Panels
- [class NSColorPanel](nscolorpanel.md)
  A standard user interface for selecting color in an app.
- [protocol NSColorPickingCustom](nscolorpickingcustom.md)
  A set of methods that provides a way to add color pickers—custom user interfaces for color selection—to an app’s color panel.
- [protocol NSColorPickingDefault](nscolorpickingdefault.md)
  A set of methods that provides basic behavior for a color picker.
- [class NSColorPicker](nscolorpicker.md)
  An abstract superclass that implements the default color picking protocol.
### Font Panels
- [class NSFontPanel](nsfontpanel.md)
  The Font panel—a user interface object that displays a list of available fonts, letting the user preview them and change the font used to display text.
- [NSFontPanel.ModeMask](nsfontpanel/modemask.md)
- [NSFontPanelValidation](nsfontpanelvalidation.md)
  A set of methods you use to tell the Font panel to display some or all of its elements.
- [protocol NSFontChanging](nsfontchanging.md)

## See Also

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
- [Sound, Speech, and Haptics](sound-speech-and-haptics.md)
  Play sounds and haptic feedback, and incorporate speech recognition and synthesis into your interface.
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/windows-panels-and-screens)*