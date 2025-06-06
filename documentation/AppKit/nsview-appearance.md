# Appearance

**Framework**: AppKit

Change the view’s visibility, vibrancy, and focus ring and respond to appearance-related changes.

## Topics

### Showing and Hiding the View
- [var isHidden: Bool](nsview/ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [var isHiddenOrHasHiddenAncestor: Bool](nsview/ishiddenorhashiddenancestor.md)
  A Boolean value indicating whether the view is hidden from sight because it, or one of its ancestors, is marked as hidden.
- [func viewDidHide()](nsview/viewdidhide.md)
  Invoked when the view is hidden, either directly, or in response to an ancestor being hidden.
- [func viewDidUnhide()](nsview/viewdidunhide.md)
  Invoked when the view is unhidden, either directly, or in response to an ancestor being unhidden
### Responding to Appearance Changes
- [func viewDidChangeEffectiveAppearance()](nsview/viewdidchangeeffectiveappearance.md)
  Informs the view that its effective appearance changed.
- [func viewDidChangeBackingProperties()](nsview/viewdidchangebackingproperties.md)
  Responds when the view’s backing store properties change.
### Getting the Vibrancy Setting
- [var allowsVibrancy: Bool](nsview/allowsvibrancy.md)
  A Boolean value indicating whether the view ensures it is vibrant on top of other content.
### Drawing the Focus Ring
- [var focusRingType: NSFocusRingType](nsview/focusringtype.md)
  The type of focus ring drawn around the view.
- [var focusRingMaskBounds: NSRect](nsview/focusringmaskbounds.md)
  The focus ring mask bounds, specified in the view’s coordinate space.
- [func drawFocusRingMask()](nsview/drawfocusringmask.md)
  Draws the focus ring mask for the view.
- [func noteFocusRingMaskChanged()](nsview/notefocusringmaskchanged.md)
  Invoked to notify the view that the focus ring mask requires updating.
- [func setKeyboardFocusRingNeedsDisplay(NSRect)](nsview/setkeyboardfocusringneedsdisplay(_:).md)
  Invalidates the area around the focus ring.
- [class var defaultFocusRingType: NSFocusRingType](nsview/defaultfocusringtype.md)
  Returns the default focus ring type.
### Displaying a Find Indicator
- [var isDrawingFindIndicator: Bool](nsview/isdrawingfindindicator.md)
  A Boolean value indicating whether the view or one of its ancestors is being drawn for a find indicator.
### Configuring a Cell’s Background
- [NSView.BackgroundStyle](nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.

## See Also

- [View Hierarchy](view-hierarchy.md)
  Manage the subviews, superview, and window of a view and respond to notifications when the view hierarchy changes.
- [View Coordinates](view-coordinates.md)
  Manage the frame and bounds rectangles that determine the size and position of the view in the view hierarchy.
- [Core Animation Support](core-animation-support.md)
  Manage the layer object that provides the view’s visual representation and accelerates drawing operations.
- [Related UI](related-ui.md)
  Manage contextual menus, cursors, tool tips, and other system-provided windows and content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview-appearance)*