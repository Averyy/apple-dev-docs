# UILayoutGuide

**Framework**: UIKit  
**Kind**: class

A rectangular area that can interact with Auto Layout.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UILayoutGuide
```

#### Overview

Use layout guides to replace the placeholder views you may have created to represent inter-view spaces or encapsulation in your user interface. Traditionally, there were a number of Auto Layout techniques that required placeholder views. A placeholder view is an empty view that does not have any visual elements of its own and serves only to define a rectangular region in the view hierarchy. For example, if you wanted to use constraints to define the size or location of an empty space between views, you needed to use a placeholder view to represent that space. If you wanted to center a group of objects, you needed a placeholder view to contain those objects. Similarly, placeholder views could be used to contain and encapsulate part of your user interface. Placeholder views let you break up a large, complex user interface into self-contained, modular chunks. When used properly, they could greatly simplify your Auto Layout constraint logic.

There are a number of costs associated with adding placeholder views to your view hierarchy. First, there is the cost of creating and maintaining the view itself. Second, the placeholder view is a full member of the view hierarchy, which means that it adds overhead to every task the hierarchy performs. Worst of all, the invisible placeholder view can intercept messages that are intended for other views, causing problems that are very difficult to find.

The [`UILayoutGuide`](uilayoutguide.md) class is designed to perform all the tasks previously performed by placeholder views, but to do it in a safer, more efficient manner. Layout guides do not define a new view. They do not participate in the view hierarchy. Instead, they simply define a rectangular region in their owning view’s coordinate system that can interact with Auto Layout.

##### Creating Layout Guides

To create a layout guide, you must perform the following steps:

1. Instantiate a new layout guide.
2. Add the layout guide to a view by calling the view’s [`addLayoutGuide(_:)`](uiview/addlayoutguide(_:).md) method.
3. Define the position and size of the layout guide using Auto Layout.

You can use these guides to define the space between elements in your layout. The following example shows layout guides used to define an equal spacing between a series of views.

A layout guide can also act as an opaque box that contains other views and controls, letting you encapsulate parts of your view and break up your layout into modular chunks.

> **Note**:  Layout guides provides a lightweight method for encapsulating part of your layout. Note that this technique only affects how Auto Layout interacts with the encapsulated views. It does not change the view hierarchy in any way. However, this is not the only way to create modular user interfaces. Container views and container view controllers provide an even greater degree of encapsulation, letting you separate the layout, the view hierarchy and even the related view controller code. For more information, see [`Adaptivity and Size Changes`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/TheAdaptiveModel.html#//apple_ref/doc/uid/TP40007457-CH18) in [`View Controller Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457). Additionally, layout constraints do not fully encapsulate their contents. The system still compares the priority of optional constraints inside the layout guide with the priority of optional constraints outside the guide.

## Topics

### Working with layout guides
- [var identifier: String](uilayoutguide/identifier.md)
  A string used to identify the layout guide.
- [var layoutFrame: CGRect](uilayoutguide/layoutframe.md)
  The layout guide’s frame in its owning view’s coordinate system.
- [var owningView: UIView?](uilayoutguide/owningview.md)
  The view that owns this layout guide.
### Creating constraints using layout anchors
- [var bottomAnchor: NSLayoutYAxisAnchor](uilayoutguide/bottomanchor.md)
  A layout anchor representing the bottom edge of the layout guide’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](uilayoutguide/centerxanchor.md)
  A layout anchor representing the horizontal center of the layout guide’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](uilayoutguide/centeryanchor.md)
  A layout anchor representing the vertical center of the layout guide’s frame.
- [var heightAnchor: NSLayoutDimension](uilayoutguide/heightanchor.md)
  A layout anchor representing the height of the layout guide’s frame.
- [var leadingAnchor: NSLayoutXAxisAnchor](uilayoutguide/leadinganchor.md)
  A layout anchor representing the leading edge of the layout guide’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](uilayoutguide/leftanchor.md)
  A layout anchor representing the left edge of the layout guide’s frame.
- [var rightAnchor: NSLayoutXAxisAnchor](uilayoutguide/rightanchor.md)
  A layout anchor representing the right edge of the layout guide’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](uilayoutguide/topanchor.md)
  A layout anchor representing the top edge of the layout guide’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](uilayoutguide/trailinganchor.md)
  A layout anchor representing the trailing edge of the layout guide’s frame.
- [var widthAnchor: NSLayoutDimension](uilayoutguide/widthanchor.md)
  A layout anchor representing the width of the layout guide’s frame.
### Debugging the layout guide
- [func constraintsAffectingLayout(for: NSLayoutConstraint.Axis) -> [NSLayoutConstraint]](uilayoutguide/constraintsaffectinglayout(for:).md)
  The constraints that impact the layout of the guide.
- [var hasAmbiguousLayout: Bool](uilayoutguide/hasambiguouslayout.md)
  A Boolean value indicating whether the constraints impacting the layout guide specify its location ambiguously.
### Handling keyboard layout
- [var keyboardLayoutGuide: UIKeyboardLayoutGuide](uiview/keyboardlayoutguide.md)
  A layout guide that tracks the keyboard’s position in your app’s layout.
- [class UIKeyboardLayoutGuide](uikeyboardlayoutguide.md)
  A layout guide that represents the space the keyboard occupies in your app’s layout.
- [class UITrackingLayoutGuide](uitrackinglayoutguide.md)
  A layout guide that automatically activates and deactivates layout constraints depending on its proximity to edges.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIFocusGuide](uifocusguide.md)
- [UITrackingLayoutGuide](uitrackinglayoutguide.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## See Also

- [class NSLayoutDimension](nslayoutdimension.md)
  A factory class for creating size-based layout constraint objects using a fluent API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguide)*