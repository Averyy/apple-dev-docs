# NSButtonCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that defines the user interface of a button or other clickable region of a view.

**Availability**:
- macOS

## Declaration

```swift
class NSButtonCell
```

```objc
@interface NSButtonCell : NSActionCell
```

## Overview

Setting the integer, float, double, or object value of an `NSButtonCell` object results in a call to [`state`](./nscell/state.md) with the value converted to integer. In the case of [`objectValue`](./nscell/objectvalue.md), `nil` is equivalent to `0`, and a non-`nil` object that doesn’t respond to [`intValue`](./nscell/intvalue.md) sets the state to `1`. Otherwise, the state is set to the object’s [`intValue`](./nscell/intvalue.md). Similarly, for most button types, querying the integer, float, double, or object value of an `NSButtonCell` returns the current state in the requested representation. In the case of [`objectValue`](./nscell/objectvalue.md), this is an `NSNumber` containing [`true`](../Swift/true.md) for on, [`false`](../Swift/false.md) for off, and integer value `-1` for the mixed state. For accelerator buttons (type [`NSAcceleratorButton`](./nsacceleratorbutton.md) or [`NSMultiLevelAcceleratorButton`](./nsmultilevelacceleratorbutton.md)) on systems that support pressure sensitivity, querying [`doubleValue`](./nscontrol/doublevalue.md) returns the amount of pressure applied while pressing the button.

The configuration of an [`NSButtonCell`](./nsbuttoncell.md) object controls how the button object appears and behaves, but it’s [`NSButton`](./nsbutton.md) that sends a message when the control is clicked. For more information on the behavior of [`NSButtonCell`](./nsbuttoncell.md), see the [`NSButton`](./nsbutton.md) and [`NSMatrix`](./nsmatrix.md) class specifications.

### Exceptions

In its implementation of the [`compare(_:)`](./nscell/compare%28_%29.md) method (declared in `NSCell`), `NSButtonCell` raises an `NSBadComparisonException` if the `otherCell` argument is not of the `NSButtonCell` class.

### Fonts

Setting the [`font`](./nscell/font.md) property does nothing if the button has no title or alternate title. If the button cell has a key equivalent, its font is not changed, but the key equivalent’s font size is changed to match the new title font.

## Topics

### Creating the Cell
- [init(coder: NSCoder)](./nsbuttoncell/init%28coder%29.md)
- [init(imageCell: NSImage?)](./nsbuttoncell/init%28imagecell%29.md)
- [init(textCell: String)](./nsbuttoncell/init%28textcell%29.md)
### Setting Titles
- [var alternateTitle: String](./nsbuttoncell/alternatetitle.md)
  The string displayed by the button when it’s in its alternate state.
- [var attributedAlternateTitle: NSAttributedString](./nsbuttoncell/attributedalternatetitle.md)
  The title displayed by the button when it’s in its alternate state, as an attributed string.
- [var attributedTitle: NSAttributedString](./nsbuttoncell/attributedtitle.md)
  The title displayed by the button when it’s in its normal state as an attributed string.
- [var title: String!](./nsbuttoncell/title.md)
  The title displayed on the button when it’s in its normal state.
### Managing Images
- [var alternateImage: NSImage?](./nsbuttoncell/alternateimage.md)
  The image the button displays in its alternate state.
- [var imagePosition: NSControl.ImagePosition](./nsbuttoncell/imageposition.md)
  The position of the button’s image relative to its title.
- [var imageScaling: NSImageScaling](./nsbuttoncell/imagescaling.md)
  The scale factor for the button’s image.
### Managing the Repeat Interval
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./nsbuttoncell/getperiodicdelay%28_,interval%29.md)
  Returns by reference the delay and interval periods for a continuous button.
- [func setPeriodicDelay(Float, interval: Float)](./nsbuttoncell/setperiodicdelay%28_,interval%29.md)
  Sets the message delay and interval for the button.
### Managing the Key Equivalent
- [var keyEquivalent: String](./nsbuttoncell/keyequivalent.md)
  The button’s key-equivalent character.
- [var keyEquivalentModifierMask: NSEvent.ModifierFlags](./nsbuttoncell/keyequivalentmodifiermask.md)
  The mask that identifies the modifier keys for the button’s key equivalent.
### Managing Graphics Attributes
- [var backgroundColor: NSColor?](./nsbuttoncell/backgroundcolor.md)
  The background color of the button.
- [var bezelStyle: NSButton.BezelStyle](./nsbuttoncell/bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var imageDimsWhenDisabled: Bool](./nsbuttoncell/imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isOpaque: Bool](./nsbuttoncell/isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](./nsbuttoncell/istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](./nsbuttoncell/showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.
### Displaying the Cell
- [var highlightsBy: NSCell.StyleMask](./nsbuttoncell/highlightsby.md)
  A set of flags that indicate how the button highlights when it receives a mouse-down event (that is, when the button is pressed).
- [func setButtonType(NSButton.ButtonType)](./nsbuttoncell/setbuttontype%28_%29.md)
  Sets how the button highlights while pressed and how it shows its state.
- [var showsStateBy: NSCell.StyleMask](./nsbuttoncell/showsstateby.md)
  The flags that indicate how the button cell shows its alternate state.
### Managing the Sound
- [var sound: NSSound?](./nsbuttoncell/sound.md)
  The sound that’s played when the user presses the button (that is during a mouse-down event).
### Handling Events and Action Messages
- [func mouseEntered(with: NSEvent)](./nsbuttoncell/mouseentered%28with%29.md)
  Draws the button’s border.
- [func mouseExited(with: NSEvent)](./nsbuttoncell/mouseexited%28with%29.md)
  Erases the button’s border.
- [func performClick(Any?)](./nsbuttoncell/performclick%28_%29.md)
  Simulates the user clicking the button with the pointer.
### Drawing the Button Content
- [func drawBezel(withFrame: NSRect, in: NSView)](./nsbuttoncell/drawbezel%28withframe,in%29.md)
  Draws the border of the button using the current bezel style.
- [func drawImage(NSImage, withFrame: NSRect, in: NSView)](./nsbuttoncell/drawimage%28_,withframe,in%29.md)
  Draws the image associated with the button’s current state.
- [func drawTitle(NSAttributedString, withFrame: NSRect, in: NSView) -> NSRect](./nsbuttoncell/drawtitle%28_,withframe,in%29.md)
  Draws the button’s title centered vertically in a specified rectangle.
### Constants
- [NSButton.BezelStyle](./nsbutton/bezelstyle-swift.enum.md)
  The set of bezel styles to style buttons in your app.
- [NSButton.ButtonType](./nsbutton/buttontype.md)
  Button types that you can specify using [`setButtonType(_:)`](./nsbuttoncell/setbuttontype%28_%29.md).
### Deprecated
- [Deprecated symbols](./nsbuttoncell-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Inherits From
- [NSActionCell](./nsactioncell.md)
### Inherited By
- [NSMenuItemCell](./nsmenuitemcell.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell)*