# Views and Controls

**Framework**: AppKit

Present your content onscreen and handle user input and events.

#### Overview

Views and controls are the building blocks of your app’s user interface.

![A sample macOS app with the view broken down into label, text field, and button control elements.The window has the title New List. Beneath the title is a text field labeled name, with a text box containing the placeholder text Enter text here. Beneath that is a label titled color followed by seven selectable circles of color. In the bottom right hand corner is a enabled Cancel button followed by a disabled OK button side-by-side.](https://docs-assets.developer.apple.com/published/5493c5134f4713caea62664e3709803a/media-4098514%402x.png)

Views can host other views. Embedding one view inside another creates a containment relationship between the host view (known as the ) and the embedded view (known as the ). View hierarchies make it easier to manage views.

You can also use views to do any of the following:

- Respond to touches and other events (either directly or in coordination with gesture recognizers).
- Draw custom content using Core Graphics.
- Respond to focus changes.
- Animate the size, position, and appearance attributes of the view using Core Animation.

Favor AppKit views and controls whenever possible. These components adapt automatically to system changes, and many support appearance customizations to support the look and feel you want in your app. When AppKit doesn’t provide the exact view or control you need, you can create a custom view.

[`NSView`](nsview.md) is the root class for all views and defines their common behavior. [`NSControl`](nscontrol.md) defines additional behaviors that are specific to buttons, switches, and other views designed for user interactions.

For additional information about how to use views and controls, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/all-components).

## Topics

### View Fundamentals
- [class NSView](nsview.md)
  The infrastructure for drawing, printing, and handling events in an app.
- [class NSControl](nscontrol.md)
  A specialized view, such as a button or text field, that notifies your app of relevant events using the target-action design pattern.
- [class NSCell](nscell.md)
  A mechanism for displaying text or images in a view object without the overhead of a full [`NSView`](nsview.md) subclass.
- [class NSActionCell](nsactioncell.md)
  An active area inside a control.
### Container Views
- [Localization-Friendly Layouts in macOS](../xcode/localization-friendly_layouts_in_macos.md)
  This project demonstrates localization-friendly auto layout constraints. It uses `NSGridView` as a container view to achieve localized layouts.
- [Grid View](grid-view.md)
  Arrange views in a flexible grid, and handle the layout associated with those views.
- [class NSSplitView](nssplitview.md)
  A view that arranges two or more views in a linear stack running horizontally or vertically.
- [Organize Your User Interface with a Stack View](organize-your-user-interface-with-a-stack-view.md)
  Group individual views in your app’s user interface into a scrollable stack view.
- [class NSStackView](nsstackview.md)
  A view that arranges an array of views horizontally or vertically and updates their placement and sizing when the window size changes.
- [class NSTabView](nstabview.md)
  A multipage interface that displays one page at a time.
- [Scroll View](scroll-view.md)
  Provide an interface for navigating content that is too large to fit in the available space.
### Content Views
- [Browser View](browser-view.md)
  Provide a column-based interface for viewing and navigating hierarchical information.
- [Collection View](collection-view.md)
  Display one or more subviews in a highly configurable arrangement.
- [Outline View](outline-view.md)
  Display a list-based interface for hierarchical data, where each level of hierarchy is indented from the previous one.
- [Table View](table-view.md)
  Display custom data in rows and columns.
- [class NSTextView](nstextview.md)
  A view that draws text and handles user interactions with that text.
### Controls
- [Responding to control-based events using target-action](../UIKit/responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class NSButton](nsbutton.md)
  A control that defines an area on the screen that a user clicks to trigger an action.
- [class NSColorWell](nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [Combo Box](combo-box.md)
  Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [class NSComboButton](nscombobutton.md)
  A button with a pull-down menu and a default action.
- [Date Picker](date-picker.md)
  Display a calendar date and provide controls for editing the date value.
- [class NSImageView](nsimageview.md)
  A display of image data in a frame.
- [class NSLevelIndicator](nslevelindicator.md)
  A visual representation of a level or quantity, using discrete values.
- [Path Control](path-control.md)
  A display of a file system path or virtual path information.
- [class NSPopUpButton](nspopupbutton.md)
  A control for selecting an item from a list.
- [class NSProgressIndicator](nsprogressindicator.md)
  An interface that provides visual feedback to the user about the status of an ongoing task.
- [class NSRuleEditor](nsruleeditor.md)
  An interface for configuring a rule-based list of options.
- [class NSPredicateEditor](nspredicateeditor.md)
  A defined set of rules that allows the editing of predicate objects.
- [Search Field](search-field.md)
  Provide a text field that is optimized for text-based search interfaces.
- [class NSSegmentedControl](nssegmentedcontrol.md)
  Display one or more buttons in a single horizontal group.
- [Slider](slider.md)
  Display a range of values from which the user selects a single value.
- [class NSStepper](nsstepper.md)
  An interface with up and down arrow buttons for incrementing or decrementing a value.
- [Text Field](text-field.md)
  Provide a simple interface for displaying and editing text, including support for password fields and secure forms of text entry.
- [Token Field](token-field.md)
  Provide a text field whose text can be rendered in a visually distinct way so that users can recognize portions more easily.
- [Toolbar](toolbar.md)
  Provide a space for controls under a window’s title bar and above your custom content.
- [class NSSwitch](nsswitch.md)
  A control that offers a binary choice.
- [class NSMatrix](nsmatrix.md)
  A legacy interface for grouping radio buttons or other types of cells together.
### Visual Adornments
- [class NSVisualEffectView](nsvisualeffectview.md)
  A view that adds translucency and vibrancy effects to the views in your interface.
- [class NSBox](nsbox.md)
  A stylized rectangular box with an optional title.
### UI Validation
- [protocol NSUserInterfaceValidations](nsuserinterfacevalidations.md)
  A protocol that a custom class can adopt to manage the enabled state of a UI element.
- [protocol NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md)
  A protocol that a custom class can adopt to manage the automatic enablement of a UI control.
### Tool Tips
- [protocol NSViewToolTipOwner](nsviewtooltipowner.md)
  A set of methods for dynamically associating a tool tip with a view.
### Related types
- [enum NSRectAlignment](nsrectalignment.md)
  Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [struct NSDirectionalEdgeInsets](nsdirectionaledgeinsets.md)
  The inset distances for views, taking the user interface layout direction into account.
- [struct NSDirectionalRectEdge](nsdirectionalrectedge.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/views-and-controls)*