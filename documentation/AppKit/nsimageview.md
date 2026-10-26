# NSImageView

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A display of image data in a frame.

**Availability**:
- macOS

## Declaration

```swift
class NSImageView
```

```objc
@interface NSImageView : NSControl
```

#### Overview

Image views can be static or editable. A static image view only displays the image that you specify. An editable image view object lets the user change the displayed image. You can also configure an image view to allow copying, pasting, deleting, and dragging of the image.

> **Note**:  An image view calls its action method only when the user drags an image into the image view’s bounds, and the image view must be editable to receive dragged images. If you want to display an image and respond to clicks in the image, use an [NSButton](https://developer.apple.com/library/archive/technotes/tn2219/_index.html#//apple_ref/doc/uid/DTS10004624-CH1-SUBSECTION12) object instead.

## Topics

### Creating the view
- [convenience init(image: NSImage)](./nsimageview/init%28image%29.md)
  Creates a non-editable image view containing the provided image. The image is scaled proportionally down to fit the view, and is centered within the view.
### Configuring the cell
- [class NSImageCell](./nsimagecell.md)
  An `NSImageCell` object displays a single image (encapsulated in an [`NSImage`](./nsimage.md) object) in a frame. This class provides methods for choosing the frame and for aligning and scaling the image to fit the frame.
### Specifying the image
- [var symbolConfiguration: NSImage.SymbolConfiguration?](./nsimageview/symbolconfiguration.md)
  Specifies a combination of point size, weight, and scale to use when sizing and displaying symbol images.
- [var image: NSImage?](./nsimageview/image.md)
  The image displayed by the image view.
### Specifying the visual characteristics
- [var imageFrameStyle: NSImageView.FrameStyle](./nsimageview/imageframestyle.md)
  The style of frame that appears around the image.
- [var imageAlignment: NSImageAlignment](./nsimageview/imagealignment.md)
  The alignment of the cell’s image inside the image view.
- [var imageScaling: NSImageScaling](./nsimageview/imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.
- [var animates: Bool](./nsimageview/animates.md)
  A Boolean value indicating whether the image view automatically plays animated images.
- [var contentTintColor: NSColor?](./nsimageview/contenttintcolor.md)
  A tint color to be used when rendering template image content.
### Specifying the dynamic range
- [var imageDynamicRange: NSImage.DynamicRange](./nsimageview/imagedynamicrange.md)
  The resolved dynamic range of the fully resolved image content.
- [var preferredImageDynamicRange: NSImage.DynamicRange](./nsimageview/preferredimagedynamicrange.md)
  The preferred dynamic range when displaying an image in the receiving image view.
- [class var defaultPreferredImageDynamicRange: NSImage.DynamicRange](./nsimageview/defaultpreferredimagedynamicrange.md)
  The default preferred image dynamic range.
### Responding to user events
- [var isEditable: Bool](./nsimageview/iseditable.md)
  A Boolean value indicating whether the user can drag a new image into the image view.
- [var allowsCutCopyPaste: Bool](./nsimageview/allowscutcopypaste.md)
  A Boolean value indicating whether the image view lets the user cut, copy, and paste the image contents.
### Configuring symbol effects
- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./nsimageview/addsymboleffect%28_,options,animated%29-4kete.md)
  Adds an indefinite symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./nsimageview/addsymboleffect%28_,options,animated%29-4p7p7.md)
  Adds a discrete symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./nsimageview/addsymboleffect%28_,options,animated%29-66ckm.md)
  Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [func setSymbolImage(NSImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions)](./nsimageview/setsymbolimage%28_,contenttransition,options%29.md)
  Sets a symbol image using the specified content-transition effect and options.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./nsimageview/removesymboleffect%28oftype,options,animated%29-8bszd.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./nsimageview/removesymboleffect%28oftype,options,animated%29-4c6vq.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./nsimageview/removesymboleffect%28oftype,options,animated%29-8tk6g.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](./nsimageview/removeallsymboleffects%28options,animated%29.md)
  Removes all symbol effects from the image view, using the specified options and animation setting.
- [- addSymbolEffect:](./nsimageview/addsymboleffect_.md)
  Adds a symbol effect to the image view with default options and animation.
- [- addSymbolEffect:options:](./nsimageview/addsymboleffect_options_.md)
  Adds a symbol effect to the image view with the specified options and default animation.
- [- addSymbolEffect:options:animated:](./nsimageview/addsymboleffect_options_animated_.md)
  Adds a symbol effect to the image view with the specified options and animation.
- [- setSymbolImage:withContentTransition:](./nsimageview/setsymbolimage_withcontenttransition_.md)
  Sets a symbol image using the specified content-transition effect.
- [- setSymbolImage:withContentTransition:options:](./nsimageview/setsymbolimage_withcontenttransition_options_.md)
  Sets a symbol image using the specified content-transition effect and options.
- [- removeSymbolEffectOfType:](./nsimageview/removesymboleffectoftype_.md)
  Removes the symbol effect that matches the specified effect type.
- [- removeSymbolEffectOfType:options:](./nsimageview/removesymboleffectoftype_options_.md)
  Removes the symbol effect that matches the specified effect type, using the specified options.
- [- removeSymbolEffectOfType:options:animated:](./nsimageview/removesymboleffectoftype_options_animated_.md)
  Removes the symbol effect that matches the specified effect type, using the specified options and animation setting.
- [- removeAllSymbolEffects](./nsimageview/removeallsymboleffects.md)
  Removes all symbol effects from the image view.
- [- removeAllSymbolEffectsWithOptions:](./nsimageview/removeallsymboleffectswithoptions_.md)
  Removes all symbol effects from the image view, using the specified options.
- [- removeAllSymbolEffectsWithOptions:animated:](./nsimageview/removeallsymboleffectswithoptions_animated_.md)
  Removes all symbol effects from the image view, using the specified options and animation setting.

## Relationships

### Inherits From
- [NSControl](./nscontrol.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityImage](./nsaccessibilityimage.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](./nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](./nsdraggingdestination.md)
- [NSMenuItemValidation](./nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controls
- [Responding to control-based events using target-action](../UIKit/responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class NSButton](./nsbutton.md)
  A control that defines an area on the screen that a user clicks to trigger an action.
- [class NSColorWell](./nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [Combo Box](./combo-box.md)
  Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [class NSComboButton](./nscombobutton.md)
  A button with a pull-down menu and a default action.
- [Date Picker](./date-picker.md)
  Display a calendar date and provide controls for editing the date value.
- [class NSLevelIndicator](./nslevelindicator.md)
  A visual representation of a level or quantity, using discrete values.
- [Path Control](./path-control.md)
  A display of a file system path or virtual path information.
- [class NSPopUpButton](./nspopupbutton.md)
  A control for selecting an item from a list.
- [class NSProgressIndicator](./nsprogressindicator.md)
  An interface that provides visual feedback to the user about the status of an ongoing task.
- [class NSRuleEditor](./nsruleeditor.md)
  An interface for configuring a rule-based list of options.
- [class NSPredicateEditor](./nspredicateeditor.md)
  A defined set of rules that allows the editing of predicate objects.
- [Search Field](./search-field.md)
  Provide a text field that is optimized for text-based search interfaces.
- [class NSSegmentedControl](./nssegmentedcontrol.md)
  Display one or more buttons in a single horizontal group.
- [Slider](./slider.md)
  Display a range of values from which the user selects a single value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview)*