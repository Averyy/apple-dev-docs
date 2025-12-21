# NSGlassEffectView

**Framework**: AppKit  
**Kind**: class

A view that embeds its content view in a dynamic glass effect.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
class NSGlassEffectView
```

## Topics

### Instance Properties
- [var contentView: NSView?](nsglasseffectview/contentview.md)
  The view to embed in glass.
- [var cornerRadius: CGFloat](nsglasseffectview/cornerradius.md)
  The amount of curvature for all corners of the glass.
- [var style: NSGlassEffectView.Style](nsglasseffectview/style-swift.property.md)
  The style of glass this view uses.
- [var tintColor: NSColor?](nsglasseffectview/tintcolor.md)
  The color the glass effect view uses to tint the background and glass effect toward.

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

- [NSGlassEffectView.Style](nsglasseffectview/style-swift.enum.md)
- [class NSGlassEffectContainerView](nsglasseffectcontainerview.md)
  A view that efficiently merges descendant glass effect views together when they are within a specified proximity to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectview)*