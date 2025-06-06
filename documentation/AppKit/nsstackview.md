# NSStackView

**Framework**: AppKit  
**Kind**: class

A view that arranges an array of views horizontally or vertically and updates their placement and sizing when the window size changes.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
class NSStackView
```

#### Overview

A stack view employs Auto Layout (the system’s constraint-based layout feature) to arrange and align an array of views according to your specification. To use a stack view effectively, you need to understand the basics of Auto Layout constraints as described in [`Auto Layout Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853).

##### Basic Features of Stack Views

A stack view supports vertical and horizontal layouts and interacts dynamically with window resizing and Cocoa animations. You can easily reconfigure the contents of a stack view at runtime. That is, after you create and configure a stack view in Interface Builder, you can add or remove views dynamically without explicitly working with layout constraints. For example, if you configure a stack view with three checkboxes and dynamically add a fourth, the stack view automatically adds constraints as needed, according to the stack view’s configuration. The new checkbox gains dynamic layout configuration from the stack view.

Stack views are nestable: a stack view is a valid element in the [`views`](nsstackview/views.md) array of another stack view.

> ❗ **Important**:  Do not add views or constraints to a stack view’s private views. A stack view’s private views might change in future versions of macOS and are not guaranteed to be encoded or decoded with the [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) class.

 Do not add views or constraints to a stack view’s private views. A stack view’s private views might change in future versions of macOS and are not guaranteed to be encoded or decoded with the [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) class.

For more information on [`NSStackView`](nsstackview.md), see [`Organize Your User Interface with a Stack View`](organize-your-user-interface-with-a-stack-view.md).

##### Layout Direction and Gravity Areas

A stack view has three so-called  that each identify a section of the stack view’s layout. A horizontal stack view, which is the default type, has a leading, a center, and a trailing gravity area. The ordering of these areas depends on the value of the stack view’s [`userInterfaceLayoutDirection`](nsview/userinterfacelayoutdirection.md) property (inherited from the [`NSView`](nsview.md) class). In a left to right language, the leading gravity area in a horizontal stack view is on the left. To enforce a left to right layout independently of language, explicitly set the layout direction by calling the inherited [`userInterfaceLayoutDirection`](nsview/userinterfacelayoutdirection.md) method on your stack view instance.

To specify vertical layout, use the [`orientation`](nsstackview/orientation.md) property and the [`NSUserInterfaceLayoutOrientation.vertical`](nsuserinterfacelayoutorientation/vertical.md) constant from the [`NSUserInterfaceLayoutOrientation`](nsuserinterfacelayoutorientation.md) enumeration. In a vertical stack view, the gravity areas always are top, center, and bottom.

##### View Detachment and Hiding

A stack view can automatically detach and reattach its views in response to layout changes, such as window resizing performed by the user, or resizing/repositioning of another view in the same view hierarchy. A view in a detached state is not present in the stack view’s view hierarchy, but it still consumes memory. A view that is hidden, but not detached, remains part of the view hierarchy and continues to participate in Auto Layout, but it is not visible and doesn’t receive input events.

To allow views to detach, set the so-called  for a stack view to a value lower than its default of [`required`](nslayoutconstraint/priority-swift.struct/required.md). See the [`setClippingResistancePriority(_:for:)`](nsstackview/setclippingresistancepriority(_:for:).md) method.

You can influence which views detach first (and reattach last). Do this by setting the so-called  for each view whose detachment order you want to specify. A view with a lower visibility priority detaches before one with a higher priority, and reattaches after it. See the [`NSStackView.VisibilityPriority`](nsstackview/visibilitypriority.md) enumeration and the [`setVisibilityPriority(_:for:)`](nsstackview/setvisibilitypriority(_:for:).md) method.

To explicitly detach a view from a stack view, call the [`setVisibilityPriority(_:for:)`](nsstackview/setvisibilitypriority(_:for:).md) method with a value of [`notVisible`](nsstackview/visibilitypriority/notvisible.md). To explicitly reattach a view to a stack view, call the same method with a value of [`mustHold`](nsstackview/visibilitypriority/musthold.md). If you hide a view that belongs to a stack view (by setting the view’s [`isHidden`](nsview/ishidden.md) property to [`true`](https://developer.apple.com/documentation/swift/true)), the view detaches from the stack view by default. Use the [`detachesHiddenViews`](nsstackview/detacheshiddenviews.md) property to change the default behavior.

The system calls a stack view delegate method when a view is about to be detached and when a view has been reattached, giving you the opportunity to run code at those times. See [`NSStackViewDelegate`](nsstackviewdelegate.md).

## Topics

### Creating a Stack View
- [convenience init(views: [NSView])](nsstackview/init(views:).md)
  Creates and returns a stack view with a specified array of views.
### Responding to Stack-Related Changes
- [var delegate: (any NSStackViewDelegate)?](nsstackview/delegate.md)
  The delegate object for the stack view.
- [protocol NSStackViewDelegate](nsstackviewdelegate.md)
  A set of methods you use to respond to a stack view detaching and reattaching views.
### Managing Views in Gravity Areas
- [func addView(NSView, in: NSStackView.Gravity)](nsstackview/addview(_:in:).md)
  Adds a view to the end of the stack view gravity area.
- [func insertView(NSView, at: Int, in: NSStackView.Gravity)](nsstackview/insertview(_:at:in:).md)
  Adds a view to a stack view gravity area at a specified index position.
- [func setViews([NSView], in: NSStackView.Gravity)](nsstackview/setviews(_:in:).md)
  Specifies an array of views for a specified gravity area in the stack view, replacing any previous views in that area.
- [func removeView(NSView)](nsstackview/removeview(_:).md)
  Removes a specified view from the stack view.
- [NSStackView.Gravity](nsstackview/gravity.md)
  The gravity areas available in a stack view.
### Managing the Arranged Subviews
- [func addArrangedSubview(NSView)](nsstackview/addarrangedsubview(_:).md)
  Adds the specified view to the end of the arranged subviews list.
- [func insertArrangedSubview(NSView, at: Int)](nsstackview/insertarrangedsubview(_:at:).md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeArrangedSubview(NSView)](nsstackview/removearrangedsubview(_:).md)
  Removes the provided view from the stack’s array of arranged subviews.
- [var arrangedSubviews: [NSView]](nsstackview/arrangedsubviews.md)
  The array of views arranged by the stack view.
### Inspecting a Stack View
- [var views: [NSView]](nsstackview/views.md)
  The array of views owned by the stack view.
- [func views(in: NSStackView.Gravity) -> [NSView]](nsstackview/views(in:).md)
  Returns the array of views in the specified gravity area in the stack view.
- [var detachedViews: [NSView]](nsstackview/detachedviews.md)
  An array that contains the detached views from all the stack view’s gravity areas.
- [func clippingResistancePriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsstackview/clippingresistancepriority(for:).md)
  Returns the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.
- [func huggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsstackview/huggingpriority(for:).md)
  Returns the Auto Layout priority for the stack view to minimize its size to fit its contained views as closely as possible, for a specified user interface axis.
### Configuring the Stack View Layout
- [var orientation: NSUserInterfaceLayoutOrientation](nsstackview/orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [enum NSUserInterfaceLayoutOrientation](nsuserinterfacelayoutorientation.md)
  The stack view layout directions, and user interface axes for hugging priority and clipping resistance.
- [var alignment: NSLayoutConstraint.Attribute](nsstackview/alignment.md)
  The view alignment within the stack view.
- [var spacing: CGFloat](nsstackview/spacing.md)
  The minimum spacing, in points, between adjacent views in the stack view.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)
- [var edgeInsets: NSEdgeInsets](nsstackview/edgeinsets.md)
  The geometric padding, in points, inside the stack view, surrounding its views.
- [var hasEqualSpacing: Bool](nsstackview/hasequalspacing.md)
  A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.
- [var distribution: NSStackView.Distribution](nsstackview/distribution-swift.property.md)
- [NSStackView.Distribution](nsstackview/distribution-swift.enum.md)
### Configuring Views in a Stack View
- [func customSpacing(after: NSView) -> CGFloat](nsstackview/customspacing(after:).md)
  Returns the custom spacing, in points, between a specified view in the stack view and the view that follows it.
- [func setCustomSpacing(CGFloat, after: NSView)](nsstackview/setcustomspacing(_:after:).md)
  Specifies the custom spacing, in points, between a specified view and the view that follows it in the stack view.
- [func visibilityPriority(for: NSView) -> NSStackView.VisibilityPriority](nsstackview/visibilitypriority(for:).md)
  Returns the visibility priority for a specified view in the stack view.
- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](nsstackview/setvisibilitypriority(_:for:).md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [NSStackView.VisibilityPriority](nsstackview/visibilitypriority.md)
  The various Auto Layout priorities for a view in the stack view to remain attached.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)
### Configuring Dynamic Behavior for a Stack View
- [var detachesHiddenViews: Bool](nsstackview/detacheshiddenviews.md)
  A Boolean value that indicates whether the stack view removes hidden views from its view hierarchy.
- [func setClippingResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsstackview/setclippingresistancepriority(_:for:).md)
  Sets the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.
- [func setHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsstackview/sethuggingpriority(_:for:).md)
  Sets the Auto Layout priority for the stack view to minimize its size, for a specified user interface axis.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
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
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview)*