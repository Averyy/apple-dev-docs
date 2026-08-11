# NSView

**Framework**: AppKit  
**Kind**: class

The infrastructure for drawing, printing, and handling events in an app.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSView
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)
- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Overview

You typically don’t use [`NSView`](nsview.md) objects directly. Instead, you use objects that descend from [`NSView`](nsview.md) or you subclass [`NSView`](nsview.md) yourself and override its methods to implement the behavior you need. An instance of the [`NSView`](nsview.md) class (or one of its subclasses) is commonly known as a view object, or simply as a view.

Views handle the presentation and interaction with your app’s visible content. You arrange one or more views inside an [`NSWindow`](nswindow.md) object, which acts as a wrapper for your content. A view object defines a rectangular region for drawing and receiving mouse events. Views handle other chores as well, including the dragging of icons and working with the [`NSScrollView`](nsscrollview.md) class to support efficient scrolling.

AppKit handles most of your app’s [`NSView`](nsview.md) management. Unless you’re implementing a concrete subclass of [`NSView`](nsview.md) or working intimately with the content of the view hierarchy at runtime, you don’t need to know much about this class’s interface. For any view, there are many methods that you can use as-is. The following methods are commonly used.

- [`frame`](nsview/frame.md) returns the location and size of the [`NSView`](nsview.md) object.
- [`bounds`](nsview/bounds.md) returns the internal origin and size of the [`NSView`](nsview.md) object.
- [`needsDisplay`](nsview/needsdisplay.md) determines whether the [`NSView`](nsview.md) object needs to be redrawn.
- [`window`](nsview/window.md) returns the [`NSWindow`](nswindow.md) object that contains the [`NSView`](nsview.md) object.
- [`draw(_:)`](nsview/draw(_:).md) draws the [`NSView`](nsview.md) object. (All subclasses must implement this method, but it’s rarely invoked explicitly.) An alternative to drawing is to update the layer directly using the [`updateLayer()`](nsview/updatelayer().md) method.

For more information on how `NSView` instances handle event and action messages, see [`Event Handling`](event-handling.md). For more information on displaying tooltips and contextual menus, see [`Displaying Contextual Menus`](nsmenu#Displaying-Contextual-Menus.md) and [`Managing Tooltips`](nswindow#Managing-Tooltips.md).

##### Subclassing Notes

`NSView` is perhaps the most important class in AppKit when it comes to subclassing and inheritance. Most user-interface objects you see in a Cocoa application are objects that inherit from `NSView`. If you want to create an object that draws itself in a special way, or that responds to mouse clicks in a special way, you would create a custom subclass of `NSView` (or of a class that inherits from `NSView`).

###### Handling Events in Your Subclass

If you subclass [`NSView`](nsview.md) directly and handle specific types of events, don’t call `super` in the implementations of your event-related methods. Views inherit their event-handling capabilities from their [`NSResponder`](nsresponder.md) parent class. The default behavior for responders is to pass events up the responder chain, which isn’t the behavior you typically want for a custom view. Therefore, don’t call `super` if your view implements any of the following methods and handles the event:

- [`mouseDown(with:)`](nsresponder/mousedown(with:).md)
- [`mouseDragged(with:)`](nsresponder/mousedragged(with:).md)
- [`mouseUp(with:)`](nsresponder/mouseup(with:).md)
- [`mouseMoved(with:)`](nsresponder/mousemoved(with:).md)
- [`mouseEntered(with:)`](nsresponder/mouseentered(with:).md)
- [`mouseExited(with:)`](nsresponder/mouseexited(with:).md)
- [`rightMouseDragged(with:)`](nsresponder/rightmousedragged(with:).md)
- [`rightMouseUp(with:)`](nsresponder/rightmouseup(with:).md)
- [`otherMouseDown(with:)`](nsresponder/othermousedown(with:).md)
- [`otherMouseDragged(with:)`](nsresponder/othermousedragged(with:).md)
- [`otherMouseUp(with:)`](nsresponder/othermouseup(with:).md)
- [`scrollWheel(with:)`](nsresponder/scrollwheel(with:).md)
- [`keyDown(with:)`](nsresponder/keydown(with:).md)
- [`keyUp(with:)`](nsresponder/keyup(with:).md)
- [`flagsChanged(with:)`](nsresponder/flagschanged(with:).md)
- [`tabletPoint(with:)`](nsresponder/tabletpoint(with:).md)
- [`tabletProximity(with:)`](nsresponder/tabletproximity(with:).md)

> **Note**:  `NSView` changes the default behavior of [`rightMouseDown(with:)`](nsresponder/rightmousedown(with:).md) so that it calls [`menu(for:)`](nsview/menu(for:).md) and, if non `nil`, presents the contextual menu. In macOS 10.7 and later, if the event is not handled, `NSView` passes the event up the responder chain. Because of these behaviorial changes, call `super` when implementing [`rightMouseDown(with:)`](nsresponder/rightmousedown(with:).md) in your custom `NSView` subclasses.

If your view descends from a class other than `NSView`, call `super` to let the parent view handle any events that you don’t.

## Topics

### Creating a view object
- [init(frame: NSRect)](nsview/init(frame:).md)
  Initializes and returns a newly allocated `NSView` object with a specified frame rectangle.
- [init?(coder: NSCoder)](nsview/init(coder:).md)
  Initializes a view using from data in the specified coder object.
- [func prepareForReuse()](nsview/prepareforreuse.md)
  Restores the view to an initial state so that it can be reused.
### Configuring the view
- [View Hierarchy](view-hierarchy.md)
  Manage the subviews, superview, and window of a view and respond to notifications when the view hierarchy changes.
- [View Coordinates](view-coordinates.md)
  Manage the frame and bounds rectangles that determine the size and position of the view in the view hierarchy.
- [Appearance](nsview-appearance.md)
  Change the view’s visibility, vibrancy, and focus ring and respond to appearance-related changes.
- [Core Animation Support](core-animation-support.md)
  Manage the layer object that provides the view’s visual representation and accelerates drawing operations.
- [Related UI](related-ui.md)
  Manage contextual menus, cursors, tool tips, and other system-provided windows and content.
### Managing the view’s content
- [Layout](layout.md)
  Specify the size and position your view relative to other nearby views using rules that update your view hierarchy automatically.
- [Drawing](nsview-drawing.md)
  Draw the content of custom views and update that content when the view’s size or appearance changes.
- [Printing](nsview-printing.md)
  Create a printable version of your view’s content and handle pagination and printer-related behaviors.
- [protocol NSViewContentSelectionInfo](nsviewcontentselectioninfo.md)
### Managing interactions
- [Event Handling](event-handling.md)
  Respond to mouse, keyboard, touch, and tablet events and gestures that originate inside your view.
### Observing bounds and frame changes
- [NSView.BoundsDidChangeMessage](nsview/boundsdidchangemessage.md)
- [NSView.FrameDidChangeMessage](nsview/framedidchangemessage.md)
### Detecting content for Apple Intelligence and Siri
- [var appEntityUIElementProvider: ((NSView, AppEntityUIElementsContext) -> [AppEntityUIElement])?](nsview/appentityuielementprovider.md)
  A closure that provides app entity identifiers to make custom view content discoverable by Apple Intelligence and Siri when it appears onscreen.
### Configuring corners
- [var cornerConfiguration: NSViewCornerConfiguration?](nsview/cornerconfiguration.md)
  Defines the corner styles (e.g., square, capsule, concentric, etc) for the view’s corners.
- [var effectiveCornerRadii: NSViewCornerRadii?](nsview/effectivecornerradii.md)
  The effective radius of each corner in the view, calculated based on the corner configuration (`cornerConfiguration`). This value is `nil` when the corner configuration is `nil`.
- [func invalidateCornerConfiguration()](nsview/invalidatecornerconfiguration.md)
  Invalidates the corner configuration, causing both the configuration and its dependencies to be recomputed.
- [func viewDidChangeEffectiveCornerRadii()](nsview/viewdidchangeeffectivecornerradii.md)
  Informs the view that its effective corner radii changed. This method should be overridden to apply the corner radii to the view as required.
### Managing text selection
- [var textSelectionManager: NSTextSelectionManager?](nsview/textselectionmanager.md)
  The text selection manager for this view.
### Supporting writing tools
- [var writingToolsCoordinator: NSWritingToolsCoordinator?](nsview/writingtoolscoordinator.md)
### Getting layout regions
- [NSView.LayoutRegion](nsview/layoutregion.md)
- [func edgeInsets(for: NSView.LayoutRegion) -> NSEdgeInsets](nsview/edgeinsets(for:).md)
- [func layoutGuide(for: NSView.LayoutRegion) -> NSLayoutGuide](nsview/layoutguide(for:).md)
- [func rect(for: NSView.LayoutRegion) -> NSRect](nsview/rect(for:).md)
### Adopting compact control metrics
- [var prefersCompactControlSizeMetrics: Bool](nsview/preferscompactcontrolsizemetrics.md)
  When this property is `YES`, any `NSControl`s in the view or its descendants will be sized with compact metrics compatible with macOS 15.0 and earlier. Defaults to `NO`.
### Managing gesture exclusivity
- [var exclusiveGestureBehavior: NSView.ExclusiveGestureBehavior](nsview/exclusivegesturebehavior-swift.property.md)
  Declares whether gesture recognizers should be exclusive in this view and its subviews.
- [NSView.ExclusiveGestureBehavior](nsview/exclusivegesturebehavior-swift.enum.md)
  Exclusive gesture behavior
### Invalidating view state
- [NSView.Invalidations](nsview/invalidations.md)
  Changes that cause aspects of a view to be invalid and require an update.
### Deprecated
- [Deprecated Symbols](nsview-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSResponder](nsresponder.md)
### Inherited By
- [NSBackgroundExtensionView](nsbackgroundextensionview.md)
- [NSBox](nsbox.md)
- [NSClipView](nsclipview.md)
- [NSCollectionView](nscollectionview.md)
- [NSControl](nscontrol.md)
- [NSGlassEffectContainerView](nsglasseffectcontainerview.md)
- [NSGlassEffectView](nsglasseffectview.md)
- [NSGridView](nsgridview.md)
- [NSOpenGLView](nsopenglview.md)
- [NSProgressIndicator](nsprogressindicator.md)
- [NSRulerView](nsrulerview.md)
- [NSScrollView](nsscrollview.md)
- [NSScrubber](nsscrubber.md)
- [NSScrubberArrangedView](nsscrubberarrangedview.md)
- [NSSplitView](nssplitview.md)
- [NSStackView](nsstackview.md)
- [NSTabView](nstabview.md)
- [NSTableCellView](nstablecellview.md)
- [NSTableHeaderView](nstableheaderview.md)
- [NSTableRowView](nstablerowview.md)
- [NSText](nstext.md)
- [NSTextInsertionIndicator](nstextinsertionindicator.md)
- [NSVisualEffectView](nsvisualeffectview.md)
### Conforms To
- [AppEntityAnnotatable](../AppIntents/AppEntityAnnotatable.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [PlaygroundLiveViewable](../playgroundsupport/playgroundliveviewable.md)

## See Also

- [class NSControl](nscontrol.md)
  A specialized view, such as a button or text field, that notifies your app of relevant events using the target-action design pattern.
- [class NSCell](nscell.md)
  A mechanism for displaying text or images in a view object without the overhead of a full [`NSView`](nsview.md) subclass.
- [class NSActionCell](nsactioncell.md)
  An active area inside a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview)*