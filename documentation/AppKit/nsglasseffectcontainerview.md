# NSGlassEffectContainerView

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A view that efficiently merges descendant glass effect views together when they are within a specified proximity to each other.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class NSGlassEffectContainerView
```

```objc
@interface NSGlassEffectContainerView : NSView
```

#### Overview

> 💡 **Tip**: Using a glass effect container view can improve performance by reducing the number of passes required to render similar glass effect views.

## Topics

### Instance Properties
- [var contentView: NSView?](./nsglasseffectcontainerview/contentview.md)
  The view that contains descendant views to merge together when in proximity to each other.
- [var spacing: CGFloat](./nsglasseffectcontainerview/spacing.md)
  The proximity at which the glass effect container view begins merging eligible descendent glass effect views.

## Relationships

### Inherits From
- [NSView](./nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](./nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](./nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Liquid Glass effects
- [class NSGlassEffectView](./nsglasseffectview.md)
  A view that embeds its content view in a dynamic glass effect.
- [NSGlassEffectView.Style](./nsglasseffectview/style-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectcontainerview)*