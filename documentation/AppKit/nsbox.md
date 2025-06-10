# NSBox

**Framework**: AppKit  
**Kind**: class

A stylized rectangular box with an optional title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSBox
```

#### Overview

Use box objects to visually group the contents of your window. For example, you might use boxes to group related views. Use an [`NSBox`](nsbox.md) object to configure the appearance of the box.

##### Subclassing Notes

An `NSBox` object is a view that draws a line around its rectangular bounds and that displays a title on or near the line (or might display neither line nor title). You can adjust the style of the line (bezel, grooved, or plain) as well as the placement and font of the title. An `NSBox` also has a content view to which other views can be added; it thus offers a way for an application to group related views. You could create a custom subclass of `NSBox` that alters or augments its appearance or that modifies its grouping behavior. For example, you might add color to the lines or background, add a new line style, or have the views in the group automatically snap to an invisible grid when added.

###### Methods to Override

You must override the [`draw(_:)`](nsview/draw(_:).md) method (inherited from `NSView`) if you want to customize the appearance of your `NSBox` objects. Depending on the visual effect you’re trying to achieve, you may have to invoke `super`‘s implementation first. For example, if you are compositing a small image in a corner of the box, you would invoke the superclass implementation first. If you’re adding a new style of line, you would provide a way to store a request for this line type (such as a boolean instance variable and related accessor methods). Then, in [`draw(_:)`](nsview/draw(_:).md), if a request for this line type exists, you would draw the entire view yourself (that is, without calling `super`). Otherwise, you would invoke the superclass implementation.

If you wish to change grouping behavior or other behavioral characteristics of the `NSBox` class, consider overriding [`contentView`](nsbox/contentview.md), [`sizeToFit()`](nsbox/sizetofit().md), or [`addSubview(_:)`](nsview/addsubview(_:).md) (inherited from `NSView`).

###### Special Considerations

If you are drawing the custom `NSBox` entirely by yourself, and you want it to look exactly like the superclass object (except for your changes), it may take some effort and time to get the details right.

## Topics

### Configuring Boxes
- [var borderRect: NSRect](nsbox/borderrect.md)
  The rectangle in which the receiver’s border is drawn.
- [var boxType: NSBox.BoxType](nsbox/boxtype-swift.property.md)
  The receiver’s box type.
- [var borderType: NSBorderType](nsbox/bordertype.md)
  The receiver’s border type.
- [var isTransparent: Bool](nsbox/istransparent.md)
  A Boolean value that indicates whether the receiver is transparent.
- [var title: String](nsbox/title.md)
  The receiver’s title.
- [var titleFont: NSFont](nsbox/titlefont.md)
  The font object used to draw the receiver’s title.
- [var titlePosition: NSBox.TitlePosition](nsbox/titleposition-swift.property.md)
  A constant representing the title position.
- [var titleCell: Any](nsbox/titlecell.md)
  The cell used to display the receiver’s title.
- [var titleRect: NSRect](nsbox/titlerect.md)
  The rectangle in which the receiver’s title is drawn.
### Customizing
- [var borderColor: NSColor](nsbox/bordercolor.md)
  The color of the receiver’s border when the receiver is a custom box with a simple line border.
- [var borderWidth: CGFloat](nsbox/borderwidth.md)
  The width of the receiver’s border when the receiver is a custom box with a simple line border.
- [var cornerRadius: CGFloat](nsbox/cornerradius.md)
  The radius of the receiver’s corners when the receiver is a custom box with a simple line border.
- [var fillColor: NSColor](nsbox/fillcolor.md)
  The color of the receiver’s background when the receiver is a custom box with a simple line border.
### Managing Content
- [var contentView: NSView?](nsbox/contentview.md)
  The receiver’s content view.
- [var contentViewMargins: NSSize](nsbox/contentviewmargins.md)
  The distances between the border and the content view.
### Sizing
- [func setFrameFromContentFrame(NSRect)](nsbox/setframefromcontentframe(_:).md)
  Places the receiver so its content view lies on the specified frame.
- [func sizeToFit()](nsbox/sizetofit.md)
  Resizes and moves the receiver’s content view so it just encloses its subviews.
### Constants
- [NSBox.TitlePosition](nsbox/titleposition-swift.enum.md)
  Specify the location of a box’s title with respect to its border.
- [NSBox.BoxType](nsbox/boxtype-swift.enum.md)
  These constants and data type identifies box types, which, in conjunction with a box’s border type, define the appearance of the box.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSVisualEffectView](nsvisualeffectview.md)
  A view that adds translucency and vibrancy effects to the views in your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox)*