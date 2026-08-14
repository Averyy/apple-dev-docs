# NSGlassEffectContainerView

**Framework**: AppKit  
**Kind**: class

A view that efficiently merges descendant glass effect views together when they are within a specified proximity to each other.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class NSGlassEffectContainerView
```

#### Overview

> 💡 **Tip**: Using a glass effect container view can improve performance by reducing the number of passes required to render similar glass effect views.

## Topics

### Instance Properties
- [var contentView: NSView?](nsglasseffectcontainerview/contentview.md)
  The view that contains descendant views to merge together when in proximity to each other.
- [var spacing: CGFloat](nsglasseffectcontainerview/spacing.md)
  The proximity at which the glass effect container view begins merging eligible descendent glass effect views.

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

- [class NSGlassEffectView](nsglasseffectview.md)
  A view that embeds its content view in a dynamic glass effect.
- [NSGlassEffectView.Style](nsglasseffectview/style-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectcontainerview)*