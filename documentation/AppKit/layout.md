# Layout

**Framework**: AppKit

Specify the size and position your view relative to other nearby views using rules that update your view hierarchy automatically.

## Topics

### Respecting the View’s Safe Area
- [var safeAreaRect: NSRect](nsview/safearearect.md)
  A rectangle in the view’s coordinate system that contains the unobscured portion of the view.
- [var safeAreaInsets: NSEdgeInsets](nsview/safeareainsets.md)
  The distances from the edges of your view that define the safe area.
- [var additionalSafeAreaInsets: NSEdgeInsets](nsview/additionalsafeareainsets.md)
  Custom insets that you specify to modify your view’s safe area
- [var safeAreaLayoutGuide: NSLayoutGuide](nsview/safearealayoutguide.md)
  The layout guide you use to position content inside your view’s safe area.
### Managing the Content Layout Direction
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](nsview/userinterfacelayoutdirection.md)
  The layout direction for content in the view.
### Opting In to Auto Layout
- [class var requiresConstraintBasedLayout: Bool](nsview/requiresconstraintbasedlayout.md)
  Returns a Boolean value indicating whether the view depends on the constraint-based layout system.
- [var translatesAutoresizingMaskIntoConstraints: Bool](nsview/translatesautoresizingmaskintoconstraints.md)
  A Boolean value indicating whether the view’s autoresizing mask is translated into constraints for the constraint-based layout system.
### Creating Constraints Using Layout Anchors
- [var bottomAnchor: NSLayoutYAxisAnchor](nsview/bottomanchor.md)
  A layout anchor representing the bottom edge of the view’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](nsview/centerxanchor.md)
  A layout anchor representing the horizontal center of the view’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](nsview/centeryanchor.md)
  A layout anchor representing the vertical center of the view’s frame.
- [var firstBaselineAnchor: NSLayoutYAxisAnchor](nsview/firstbaselineanchor.md)
  A layout anchor representing the baseline for the topmost line of text in the view.
- [var heightAnchor: NSLayoutDimension](nsview/heightanchor.md)
  A layout anchor representing the height of the view’s frame.
- [var lastBaselineAnchor: NSLayoutYAxisAnchor](nsview/lastbaselineanchor.md)
  A layout anchor representing the baseline for the bottommost line of text in the view.
- [var leadingAnchor: NSLayoutXAxisAnchor](nsview/leadinganchor.md)
  A layout anchor representing the leading edge of the view’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](nsview/leftanchor.md)
  A layout anchor representing the left edge of the view’s frame.
- [var rightAnchor: NSLayoutXAxisAnchor](nsview/rightanchor.md)
  A layout anchor representing the right edge of the view’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](nsview/topanchor.md)
  A layout anchor representing the top edge of the view’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](nsview/trailinganchor.md)
  A layout anchor representing the trailing edge of the view’s frame.
- [var widthAnchor: NSLayoutDimension](nsview/widthanchor.md)
  A layout anchor representing the width of the view’s frame.
### Managing the View’s Constraints
- [var constraints: [NSLayoutConstraint]](nsview/constraints.md)
  Returns the constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](nsview/addconstraint(_:).md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](nsview/addconstraints(_:).md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](nsview/removeconstraint(_:).md)
  Removes the specified constraint from the view.
- [func removeConstraints([NSLayoutConstraint])](nsview/removeconstraints(_:).md)
  Removes the specified constraints from the view.
### Measuring in Auto Layout
- [var fittingSize: NSSize](nsview/fittingsize.md)
  The minimum size of the view that satisfies the constraints it holds.
- [var intrinsicContentSize: NSSize](nsview/intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](nsview/invalidateintrinsiccontentsize.md)
  Invalidates the view’s intrinsic content size.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsview/contentcompressionresistancepriority(for:).md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsview/setcontentcompressionresistancepriority(_:for:).md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsview/contenthuggingpriority(for:).md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsview/setcontenthuggingpriority(_:for:).md)
  Sets the priority with which a view resists being made larger than its intrinsic size.
- [class let noIntrinsicMetric: CGFloat](nsview/nointrinsicmetric.md)
  A value that tells the layout system to ignore the intrinsic size value for a given dimension.
### Managing Layout Guides
- [func addLayoutGuide(NSLayoutGuide)](nsview/addlayoutguide(_:).md)
  Adds the provided layout guide to the view.
- [func removeLayoutGuide(NSLayoutGuide)](nsview/removelayoutguide(_:).md)
  Removes the provided layout guide from the view.
- [var layoutGuides: [NSLayoutGuide]](nsview/layoutguides.md)
  The array of layout guide objects owned by this view.
- [var layoutMarginsGuide: NSLayoutGuide](nsview/layoutmarginsguide.md)
  A layout guide that provides the recommended amount of padding for content inside of a view.
### Aligning Views with Auto Layout
- [func alignmentRect(forFrame: NSRect) -> NSRect](nsview/alignmentrect(forframe:).md)
  Returns the view’s alignment rectangle for a given frame.
- [func frame(forAlignmentRect: NSRect) -> NSRect](nsview/frame(foralignmentrect:).md)
  Returns the view’s frame for a given alignment rectangle.
- [var alignmentRectInsets: NSEdgeInsets](nsview/alignmentrectinsets.md)
  The insets (in points) from the view’s frame that define its content rectangle.
- [var baselineOffsetFromBottom: CGFloat](nsview/baselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its baseline.
- [var firstBaselineOffsetFromTop: CGFloat](nsview/firstbaselineoffsetfromtop.md)
  The distance (in points) between the top of the view’s alignment rectangle and its topmost baseline.
- [var lastBaselineOffsetFromBottom: CGFloat](nsview/lastbaselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its bottommost baseline.
### Triggering Auto Layout
- [var needsLayout: Bool](nsview/needslayout.md)
  A Boolean value indicating whether the view needs a layout pass before it can be drawn.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func layoutSubtreeIfNeeded()](nsview/layoutsubtreeifneeded.md)
  Updates the layout of the receiving view and its subviews based on the current views and constraints.
- [var needsUpdateConstraints: Bool](nsview/needsupdateconstraints.md)
  A Boolean value indicating whether the view’s constraints need to be updated.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.
- [func updateConstraintsForSubtreeIfNeeded()](nsview/updateconstraintsforsubtreeifneeded.md)
  Updates the constraints for the receiving view and its subviews.
### Enabling and Disabling Constraints
- [var isHorizontalContentSizeConstraintActive: Bool](nsview/ishorizontalcontentsizeconstraintactive.md)
  A Boolean value that indicates whether the view’s horizontal size constraints are active.
- [var isVerticalContentSizeConstraintActive: Bool](nsview/isverticalcontentsizeconstraintactive.md)
  A Boolean value that indicates whether the view’s vertical size constraints are active.
### Debugging Auto Layout
- [func constraintsAffectingLayout(for: NSLayoutConstraint.Orientation) -> [NSLayoutConstraint]](nsview/constraintsaffectinglayout(for:).md)
  Returns the constraints impacting the layout of the view for a given orientation.
- [var hasAmbiguousLayout: Bool](nsview/hasambiguouslayout.md)
  A Boolean value indicating whether the constraints impacting the layout of the view incompletely specify the location of the view.
- [func exerciseAmbiguityInLayout()](nsview/exerciseambiguityinlayout.md)
  Randomly changes the frame of a view with an ambiguous layout between the different valid values.
### Resizing Subviews
- [var autoresizesSubviews: Bool](nsview/autoresizessubviews.md)
  A Boolean value indicating whether the view applies the autoresizing behavior to its subviews when its frame size changes.
- [var autoresizingMask: NSView.AutoresizingMask](nsview/autoresizingmask-swift.property.md)
  The options that determine how the view is resized relative to its superview.
- [NSView.AutoresizingMask](nsview/autoresizingmask-swift.struct.md)
  Constants that specify the autoresizing behaviors for views.
- [func resizeSubviews(withOldSize: NSSize)](nsview/resizesubviews(witholdsize:).md)
  Informs the view’s subviews that the view’s bounds rectangle size has changed.
- [func resize(withOldSuperviewSize: NSSize)](nsview/resize(witholdsuperviewsize:).md)
  Informs the view that the bounds size of its superview has changed.

## See Also

- [Drawing](nsview-drawing.md)
  Draw the content of custom views and update that content when the view’s size or appearance changes.
- [Printing](nsview-printing.md)
  Create a printable version of your view’s content and handle pagination and printer-related behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/layout)*