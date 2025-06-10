# NSGlassEffectView

**Framework**: AppKit  
**Kind**: class

NSGlassView embeds its content view in a dynamic glass effect.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
class NSGlassEffectView
```

## Topics

### Instance Properties
- [var contentView: NSView?](nsglasseffectview/contentview.md)
  The view to be embedded in glass. Note that only the contentView of the NSGlassView is guaranteed to be placed inside the glass effect. Arbitrary subviews are not guaranteed any specific behavior regarding z-order against the content view or glass effect.
- [var cornerRadius: CGFloat](nsglasseffectview/cornerradius.md)
  Controls the amount of curvature for all corners of the glass.
- [var tintColor: NSColor?](nsglasseffectview/tintcolor.md)
  Modifies the background and effect to tint toward the provided tint color.

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

- [class NSGlassEffectContainerView](nsglasseffectcontainerview.md)
  NSGlassContainerView allows similar NSGlassViews in appropriate proximity to eachother to be merged together. Additionally, NSGlassContainerView can reduce the number of passes required to render similar glass views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectview)*