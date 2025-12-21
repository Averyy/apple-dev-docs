# NSButtonCell

**Framework**: AppKit  
**Kind**: class

An object that defines the user interface of a button or other clickable region of a view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSButtonCell
```

#### Overview

Setting the integer, float, double, or object value of an `NSButtonCell` object results in a call to [`state`](nscell/state.md) with the value converted to integer. In the case of [`objectValue`](nscell/objectvalue.md), `nil` is equivalent to `0`, and a non-`nil` object that doesn’t respond to [`intValue`](nscell/intvalue.md) sets the state to `1`. Otherwise, the state is set to the object’s [`intValue`](nscell/intvalue.md). Similarly, for most button types, querying the integer, float, double, or object value of an `NSButtonCell` returns the current state in the requested representation. In the case of [`objectValue`](nscell/objectvalue.md), this is an `NSNumber` containing [`true`](https://developer.apple.com/documentation/Swift/true) for on, [`false`](https://developer.apple.com/documentation/Swift/false) for off, and integer value `-1` for the mixed state. For accelerator buttons (type [`NSAcceleratorButton`](nsacceleratorbutton.md) or [`NSMultiLevelAcceleratorButton`](nsmultilevelacceleratorbutton.md)) on systems that support pressure sensitivity, querying [`doubleValue`](nscontrol/doublevalue.md) returns the amount of pressure applied while pressing the button.

The configuration of an [`NSButtonCell`](nsbuttoncell.md) object controls how the button object appears and behaves, but it’s [`NSButton`](nsbutton.md) that sends a message when the control is clicked. For more information on the behavior of [`NSButtonCell`](nsbuttoncell.md), see the [`NSButton`](nsbutton.md) and [`NSMatrix`](nsmatrix.md) class specifications, and [`Button Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Button.html#//apple_ref/doc/uid/10000019i).

##### Exceptions

In its implementation of the [`compare(_:)`](nscell/compare(_:).md) method (declared in `NSCell`), `NSButtonCell` raises an `NSBadComparisonException` if the `otherCell` argument is not of the `NSButtonCell` class.

##### Fonts

Setting the [`font`](nscell/font.md) property does nothing if the button has no title or alternate title. If the button cell has a key equivalent, its font is not changed, but the key equivalent’s font size is changed to match the new title font.

## Topics

### Creating the Cell
- [init(coder: NSCoder)](nsbuttoncell/init(coder:).md)
- [init(imageCell: NSImage?)](nsbuttoncell/init(imagecell:).md)
- [init(textCell: String)](nsbuttoncell/init(textcell:).md)
### Setting Titles
- [var alternateTitle: String](nsbuttoncell/alternatetitle.md)
  The string displayed by the button when it’s in its alternate state.
- [var attributedAlternateTitle: NSAttributedString](nsbuttoncell/attributedalternatetitle.md)
  The title displayed by the button when it’s in its alternate state, as an attributed string.
- [var attributedTitle: NSAttributedString](nsbuttoncell/attributedtitle.md)
  The title displayed by the button when it’s in its normal state as an attributed string.
- [var title: String!](nsbuttoncell/title.md)
  The title displayed on the button when it’s in its normal state.
### Managing Images
- [var alternateImage: NSImage?](nsbuttoncell/alternateimage.md)
  The image the button displays in its alternate state.
- [var imagePosition: NSControl.ImagePosition](nsbuttoncell/imageposition.md)
  The position of the button’s image relative to its title.
- [var imageScaling: NSImageScaling](nsbuttoncell/imagescaling.md)
  The scale factor for the button’s image.
### Managing the Repeat Interval
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nsbuttoncell/getperiodicdelay(_:interval:).md)
  Returns by reference the delay and interval periods for a continuous button.
- [func setPeriodicDelay(Float, interval: Float)](nsbuttoncell/setperiodicdelay(_:interval:).md)
  Sets the message delay and interval for the button.
### Managing the Key Equivalent
- [var keyEquivalent: String](nsbuttoncell/keyequivalent.md)
  The button’s key-equivalent character.
- [var keyEquivalentFont: NSFont?](nsbuttoncell/keyequivalentfont.md)
  The font used to draw the button’s key equivalent.
- [var keyEquivalentModifierMask: NSEvent.ModifierFlags](nsbuttoncell/keyequivalentmodifiermask.md)
  The mask that identifies the modifier keys for the button’s key equivalent.
- [func setKeyEquivalentFont(String, size: CGFloat)](nsbuttoncell/setkeyequivalentfont(_:size:).md)
  Sets by name and size of the font used to draw the key equivalent.
### Managing Graphics Attributes
- [var backgroundColor: NSColor?](nsbuttoncell/backgroundcolor.md)
  The background color of the button.
- [var bezelStyle: NSButton.BezelStyle](nsbuttoncell/bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var gradientType: NSButton.GradientType](nsbuttoncell/gradienttype.md)
  The gradient of the button’s border.
- [var imageDimsWhenDisabled: Bool](nsbuttoncell/imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isOpaque: Bool](nsbuttoncell/isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](nsbuttoncell/istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](nsbuttoncell/showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.
### Displaying the Cell
- [var highlightsBy: NSCell.StyleMask](nsbuttoncell/highlightsby.md)
  A set of flags that indicate how the button highlights when it receives a mouse-down event (that is, when the button is pressed).
- [func setButtonType(NSButton.ButtonType)](nsbuttoncell/setbuttontype(_:).md)
  Sets how the button highlights while pressed and how it shows its state.
- [var showsStateBy: NSCell.StyleMask](nsbuttoncell/showsstateby.md)
  The flags that indicate how the button cell shows its alternate state.
### Managing the Sound
- [var sound: NSSound?](nsbuttoncell/sound.md)
  The sound that’s played when the user presses the button (that is during a mouse-down event).
### Handling Events and Action Messages
- [func mouseEntered(with: NSEvent)](nsbuttoncell/mouseentered(with:).md)
  Draws the button’s border.
- [func mouseExited(with: NSEvent)](nsbuttoncell/mouseexited(with:).md)
  Erases the button’s border.
- [func performClick(Any?)](nsbuttoncell/performclick(_:).md)
  Simulates the user clicking the button with the pointer.
### Drawing the Button Content
- [func drawBezel(withFrame: NSRect, in: NSView)](nsbuttoncell/drawbezel(withframe:in:).md)
  Draws the border of the button using the current bezel style.
- [func drawImage(NSImage, withFrame: NSRect, in: NSView)](nsbuttoncell/drawimage(_:withframe:in:).md)
  Draws the image associated with the button’s current state.
- [func drawTitle(NSAttributedString, withFrame: NSRect, in: NSView) -> NSRect](nsbuttoncell/drawtitle(_:withframe:in:).md)
  Draws the button’s title centered vertically in a specified rectangle.
### Constants
- [NSButton.BezelStyle](nsbutton/bezelstyle-swift.enum.md)
  The set of bezel styles to style buttons in your app.
- [NSButton.ButtonType](nsbutton/buttontype.md)
  Button types that you can specify using [`setButtonType(_:)`](nsbuttoncell/setbuttontype(_:).md).
- [NSButton.GradientType](nsbutton/gradienttype.md)
  Specify the gradients used by the [`gradientType`](nsbuttoncell/gradienttype.md) property.

## Relationships

### Inherits From
- [NSActionCell](nsactioncell.md)
### Inherited By
- [NSMenuItemCell](nsmenuitemcell.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell)*