# NSGlassEffectView

**Framework**: AppKit  
**Kind**: class

A view that embeds its content view in a dynamic glass effect.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class NSGlassEffectView
```

## Topics

### Instance Properties
- [var contentView: NSView?](nsglasseffectview/contentview.md)
  The view to embed in glass.
- [var cornerRadius: CGFloat](nsglasseffectview/cornerradius.md)
  The amount of curvature for all corners of the glass.
- [var effectIsInteractive: Bool](nsglasseffectview/effectisinteractive.md)
  Enables interactive glass behavior, which adds a visual response to user interactions.
- [var style: NSGlassEffectView.Style](nsglasseffectview/style-swift.property.md)
  The style of glass this view uses.
- [var tintColor: NSColor?](nsglasseffectview/tintcolor.md)
  The color the glass effect view uses to tint the background and glass effect toward.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [NSGlassEffectView.Style](nsglasseffectview/style-swift.enum.md)
- [class NSGlassEffectContainerView](nsglasseffectcontainerview.md)
  A view that efficiently merges descendant glass effect views together when they are within a specified proximity to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectview)*