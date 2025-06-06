# NSVisualEffectView

**Framework**: Appkit  
**Kind**: class

A view that adds translucency and vibrancy effects to the views in your interface.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSVisualEffectView
```

#### Overview

Use visual effect views primarily as background views for your app’s content. A visual effect view makes your foreground content more prominent by employing the following effects:

-  and the blurring of background content adds depth to your interface.
-  is a subtle blending of foreground and background colors to increase the contrast and make the foreground content stand out visually.

The material and blending mode you assign determines the exact appearance of the visual effect. Not all materials support transparency, and materials apply vibrancy in different ways. The appearance and behavior of materials can also change based on system settings, so always pick a material based on its intended use. For example, use the [`NSVisualEffectView.Material.sidebar`](nsvisualeffectview/material-swift.enum/sidebar.md) material when your view serves as the background of your window’s sidebar.  Don’t select materials based on the apparent colors they impart on your interface.

AppKit creates visual effect views automatically for window titlebars, popovers, and source list table views. You don’t need to add visual effect views to those elements of your interface.

##### Choosing a Translucency Effect for Your View

For visual effect views you create yourself, use the [`blendingMode`](nsvisualeffectview/blendingmode-swift.property.md) property to specify how and where you want the translucency applied.

-  uses the content behind the window as the background for your visual effect view. Behind-window blending makes your entire window stand out above other windows and apps on the desktop. Sheets and popovers use behind-window blending.
-  uses the window’s content as the background for your visual effect view. Typically, you use in-window blending with scrolling content, so that the scrolled content remains partially visible under other parts of your window chrome. Toolbars always use in-window blending.

![An illustration of a window whose title bar and side bar use visual effect views with different blending options. The title bar uses in-window blending which blends content from the window with the bar. The side bar uses behind-window blending, which allows part of the desktop to show through. ](https://docs-assets.developer.apple.com/published/153ccb58867a13d8d8a600691c57adf7/media-3198506%402x.png)

##### Enabling Vibrancy for Foreground Content

The presence of a visual effect view in your view hierarchy does not automatically add vibrancy to your content. For custom views, you must explicitly enable vibrancy by overriding the [`allowsVibrancy`](nsview/allowsvibrancy.md) property and returning [`true`](https://developer.apple.com/documentation/swift/true).

> **Note**:  AppKit views and controls automatically add vibrancy where appropriate. For example, [`NSTextField`](nstextfield.md) enables vibrancy to increase the contrast between the text and background. Don’t change the vibrancy settings of standard AppKit views and controls.

It is recommended that you enable vibrancy only in the leaf views of your view hierarchy. Subviews inherit the vibrancy of their parent. Once enabled in a parent view, a subview cannot turn off vibrancy. As a result, enabling vibrancy in a parent view can lead to subviews that look incorrect if they are not designed to take advantage of the vibrancy effect.

Vibrancy works best when your custom views contain grayscale content. Combining a grayscale foreground with a color background works well, because AppKit improves the contrast while only subtly changing the foreground hue. The same isn’t always true when blending two different color values. Dramatically different foreground and background hues can cancel each other out or result in colors that don’t match your original designs.

Instead of defining custom grayscale color assets, consider using the built-in colors [`labelColor`](nscolor/labelcolor.md), [`secondaryLabelColor`](nscolor/secondarylabelcolor.md), [`tertiaryLabelColor`](nscolor/tertiarylabelcolor.md), and [`quaternaryLabelColor`](nscolor/quaternarylabelcolor.md). While typically used with text, these colors are applicable with any app content. The built-in colors represent varying levels of contrast for your content, with [`labelColor`](nscolor/labelcolor.md) offering the most contrast, and [`quaternaryLabelColor`](nscolor/quaternarylabelcolor.md) offering the least contrast.

##### Subclassing Notes

If you subclass `NSVisualEffectView`:

- Always call `super` if you override [`viewDidMoveToWindow()`](nsview/viewdidmovetowindow().md) or [`viewWillMove(toWindow:)`](nsview/viewwillmove(towindow:).md).
- Do not override [`draw(_:)`](nsview/draw(_:).md) or [`updateLayer()`](nsview/updatelayer().md).

## Topics

### Specifying the Background Material
- [var material: NSVisualEffectView.Material](nsvisualeffectview/material-swift.property.md)
  The material shown by the visual effect view.
- [NSVisualEffectView.Material](nsvisualeffectview/material-swift.enum.md)
  Constants to specify the material shown by the visual effect view.
### Specifying the Effect Appearance
- [var blendingMode: NSVisualEffectView.BlendingMode](nsvisualeffectview/blendingmode-swift.property.md)
  A value indicating how the view’s contents blend with the surrounding content.
- [NSVisualEffectView.BlendingMode](nsvisualeffectview/blendingmode-swift.enum.md)
  Constants that specify whether the visual effect view blends with what’s either behind or within the window.
- [var isEmphasized: Bool](nsvisualeffectview/isemphasized.md)
  A Boolean value indicating whether to emphasize the look of the material.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nsvisualeffectview/interiorbackgroundstyle.md)
  The view’s interior background style.
### Masking the Visual Effect
- [var maskImage: NSImage?](nsvisualeffectview/maskimage.md)
  An image whose alpha channel masks the visual effect view’s material.
### Enabling or Disabling the Effect
- [var state: NSVisualEffectView.State](nsvisualeffectview/state-swift.property.md)
  A value that indicates whether a view has a visual effect applied.
- [NSVisualEffectView.State](nsvisualeffectview/state-swift.enum.md)
  Constants to specify how the material appearance should reflect window activity state.
### Handling Moves to a Different Window
- [func viewDidMoveToWindow()](nsvisualeffectview/viewdidmovetowindow.md)
  Notifies the view that it moved to a new window.
- [func viewWillMove(toWindow: NSWindow?)](nsvisualeffectview/viewwillmove(towindow:).md)
  Notifies the view immediately before it moves to a new window (which may be `nil`).

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

## See Also

- [class NSBox](nsbox.md)
  A stylized rectangular box with an optional title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nsvisualeffectview)*