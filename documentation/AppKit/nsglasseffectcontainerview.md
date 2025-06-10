# NSGlassEffectContainerView

**Framework**: AppKit  
**Kind**: class

NSGlassContainerView allows similar NSGlassViews in appropriate proximity to eachother to be merged together. Additionally, NSGlassContainerView can reduce the number of passes required to render similar glass views.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
class NSGlassEffectContainerView
```

## Topics

### Instance Properties
- [var contentView: NSView?](nsglasseffectcontainerview/contentview.md)
  NSGlassViews that are descendents of an NSGlassContainerView’s contentView will 1) have their z-order elevated above that of the contentView 2) if the NSGlassViews are sufficiently similar, they will merge together in close proximity 3) can process similar NSGlassViews as a batch, to improve performance.
- [var spacing: CGFloat](nsglasseffectcontainerview/spacing.md)
  Controls the proximity at which descendent NSGlassViews will begin merging with eachother, if they are otherwise eligable. The default value (0) is sufficient for batch processing the effects of eligable NSGlassViews, while avoiding distortion and merging effects for views in close proximity.

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

- [class NSGlassEffectView](nsglasseffectview.md)
  NSGlassView embeds its content view in a dynamic glass effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectcontainerview)*