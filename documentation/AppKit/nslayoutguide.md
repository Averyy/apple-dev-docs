# NSLayoutGuide

**Framework**: Appkit  
**Kind**: class

A rectangular area that can interact with Auto Layout.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class NSLayoutGuide
```

#### Overview

Use layout guides to replace the placeholder views you may have created to represent inter-view spaces or encapsulation in your user interface. Traditionally, there were a number of Auto Layout techniques that required placeholder views. A placeholder view is an empty view that does not have any visual elements of its own and serves only to define a rectangular region in the view hierarchy. For example, if you wanted to use constraints to define the size or location of an empty space between views, you needed to use a placeholder view to represent that space. If you wanted to center a group of objects, you needed a placeholder view to contain those objects. Similarly, placeholder views could be used to contain and encapsulate part of your user interface. Placeholder views let you break up a large, complex user interface into self-contained, modular chunks. When used properly, they could greatly simplify your Auto Layout constraint logic.

There are a number of costs associated with adding placeholder views to your view hierarchy. First, there is the cost of creating and maintaining the view itself. Second, the placeholder view is a full member of the view hierarchy, which means that it adds overhead to every task the hierarchy performs. Worst of all, the invisible placeholder view can intercept messages that are intended for other views, causing problems that are very difficult to find.

The [`NSLayoutGuide`](nslayoutguide.md) class is designed to perform all the tasks previously performed by placeholder views, but to do it in a safer, more efficient manner. Layout guides are not views. They do not use as much memory, and they do not participate in the view hierarchy. Instead, they simply define a rectangular region in their owning view’s coordinate system that can interact with Auto Layout.

##### Creating Layout Guides

To create a layout guide, perform the following steps:

1. Instantiate a new layout guide.
2. Add the layout guide to a view by calling the view’s [`addLayoutGuide(_:)`](nsview/addlayoutguide(_:).md) method .
3. Define the position and size of the layout guide using Auto Layout.

You can use these guides to define the space between elements in your layout. The following example shows how to use layout guides to define an equal spacing between a series of views.

A layout guide can also act as an opaque box that contains other views and controls, letting you encapsulate parts of your view and break up your layout into modular chunks.

> **Note**:  Layout constraints do not fully encapsulate their contents. The system still compares the priority of optional constraints inside the layout guide with the priority of optional constraints outside the guide.

## Topics

### Working With Layout Guides
- [var identifier: NSUserInterfaceItemIdentifier](nslayoutguide/identifier.md)
  A string used to identify the layout guide.
- [var frame: NSRect](nslayoutguide/frame.md)
  The layout guide’s frame in its owning view’s coordinate system.
- [var owningView: NSView?](nslayoutguide/owningview.md)
  The view that owns this layout guide.
### Creating Constraints Using Layout Anchors
- [var bottomAnchor: NSLayoutYAxisAnchor](nslayoutguide/bottomanchor.md)
  A layout anchor representing the bottom edge of the layout guide’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](nslayoutguide/centerxanchor.md)
  A layout anchor representing the horizontal center of the layout guide’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](nslayoutguide/centeryanchor.md)
  A layout anchor representing the vertical center of the layout guide’s frame.
- [var heightAnchor: NSLayoutDimension](nslayoutguide/heightanchor.md)
  A layout anchor representing the height of the layout guide’s frame.
- [var leadingAnchor: NSLayoutXAxisAnchor](nslayoutguide/leadinganchor.md)
  A layout anchor representing the leading edge of the layout guide’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](nslayoutguide/leftanchor.md)
  A layout anchor representing the left edge of the layout guide’s frame.
- [var rightAnchor: NSLayoutXAxisAnchor](nslayoutguide/rightanchor.md)
  A layout anchor representing the right edge of the layout guide’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](nslayoutguide/topanchor.md)
  A layout anchor representing the top edge of the layout guide’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](nslayoutguide/trailinganchor.md)
  A layout anchor representing the trailing edge of the layout guide’s frame.
- [var widthAnchor: NSLayoutDimension](nslayoutguide/widthanchor.md)
  A layout anchor representing the width of the layout guide’s frame.
### Instance Properties
- [var hasAmbiguousLayout: Bool](nslayoutguide/hasambiguouslayout.md)
### Instance Methods
- [func constraintsAffectingLayout(for: NSLayoutConstraint.Orientation) -> [NSLayoutConstraint]](nslayoutguide/constraintsaffectinglayout(for:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)

## See Also

- [class NSLayoutDimension](nslayoutdimension.md)
  A factory class for creating size-based layout constraint objects using a fluent API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nslayoutguide)*