# NSWindow.Depth

**Framework**: AppKit  
**Kind**: enum

A type that represents the depth, or amount of memory, for a single pixel in a window or screen.

**Availability**:
- macOS 10.6+

## Declaration

```swift
enum Depth
```

#### Overview

A depth of `0` indicates default depth. Don’t make window depths persistent because they aren’t the same across systems.

Use the functions [`colorSpaceName`](nswindow/depth/colorspacename.md), [`bitsPerPixel`](nswindow/depth/bitsperpixel.md), and [`isPlanar`](nswindow/depth/isplanar.md) to extract info from an `NSWindowDepth` value.

Use [`NSBestDepth`](nsbestdepth.md) to compute window depths. [`NSBestDepth`](nsbestdepth.md) tries to accommodate all the parameters (match or better). If there are multiple matches, this function uses color space first, then bits per sample (`bps`), then `planar`, then bits per pixel (`bpp)` to determine the closest match. Use `0` for `bpp` to indicate the default, the same as the number of bits per plane: either `bps` or `bps` * [`numberOfColorComponents`](nscolorspacename/numberofcolorcomponents.md). You may use other values as hints to provide backing stores of different configurations — for instance, 8-bit color.

You can also use one of the explicit bit depths defined in `Explicit Window Depth Limits` for the `NSWindow` property [`depthLimit`](nswindow/depthlimit.md).

## Topics

### Constants
- [NSWindow.Depth.onehundredtwentyeightBitRGB](nswindow/depth/onehundredtwentyeightbitrgb.md)
  One hundred and twenty eight bit RGB depth limit.
- [NSWindow.Depth.sixtyfourBitRGB](nswindow/depth/sixtyfourbitrgb.md)
  Sixty four bit RGB depth limit.
- [NSWindow.Depth.twentyfourBitRGB](nswindow/depth/twentyfourbitrgb.md)
  Twenty four bit RGB depth limit.
### Accessing Depth Details
- [static var availableDepths: [NSWindow.Depth]](nswindow/depth/availabledepths.md)
  An array that contains all available windows depths.
- [static func bestDepth(colorSpaceName: NSColorSpaceName, bitsPerSample: Int, bitsPerPixel: Int, isPlanar: Bool) -> (NSWindow.Depth, isExactMatch: Bool)](nswindow/depth/bestdepth(colorspacename:bitspersample:bitsperpixel:isplanar:).md)
  Determines the best window depth that most closely matches the given properties.
- [var bitsPerPixel: Int](nswindow/depth/bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](nswindow/depth/bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](nswindow/depth/colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var isPlanar: Bool](nswindow/depth/isplanar.md)
  Returns whether the specified window depth is planar.
### Initializers
- [init?(rawValue: Int32)](nswindow/depth/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSWindow.SelectionDirection](nswindow/selectiondirection.md)
  Constants that specify the direction a window is currently using to change the key view.
- [NSWindow.ButtonType](nswindow/buttontype.md)
  Constants that provide a way to access standard title bar buttons.
- [NSRunLoop—Ordering Modes for NSWindow](nsrunloop-ordering-modes-for-nsw.md)
  Constants that specify the priority for runloop messages.
- [NSWindow.BackingStoreType](nswindow/backingstoretype.md)
  Constants that specify how the window device buffers the drawing done in a window.
- [NSWindow.OrderingMode](nswindow/orderingmode.md)
  Constants that let you specify how a window is ordered relative to another window.
- [NSWindow.SharingType](nswindow/sharingtype-swift.enum.md)
  Constants that represent the access levels other processes can have to a window’s content.
- [NSWindow.NumberListOptions](nswindow/numberlistoptions.md)
  Options to use when retrieving window numbers from the system.
- [NSWindow.AnimationBehavior](nswindow/animationbehavior-swift.enum.md)
  Constants that control the automatic window animation behavior windows use when ordering to the front or out of view.
- [NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct.md)
  Window collection behaviors related to Mission Control, Spaces, and Stage Manager.
- [NSWindow.OcclusionState](nswindow/occlusionstate-swift.struct.md)
  Specifies whether the window is occluded.
- [NSWindow.TitleVisibility](nswindow/titlevisibility-swift.enum.md)
  Specifies the appearance of the window’s title bar area.
- [NSWindow.UserTabbingPreference](nswindow/usertabbingpreference-swift.enum.md)
  A value that indicates the user’s preference for window tabbing.
- [NSWindow.TabbingMode](nswindow/tabbingmode-swift.enum.md)
  The preferred tabbing behavior of a window.
- [Application Kit Version for Deferred Window Display Support](application-kit-version-for-deferred-window-display-support.md)
  The version of the AppKit.framework containing a specific bug fix or capability.
- [Application Kit Version for Custom Sheet Position](application-kit-version-for-custom-sheet-position.md)
  The version of the AppKit.framework containing a specific bug fix or capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depth)*