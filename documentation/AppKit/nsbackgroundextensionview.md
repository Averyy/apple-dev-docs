# NSBackgroundExtensionView

**Framework**: AppKit  
**Kind**: class

A view that extends content to fill its own bounds.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class NSBackgroundExtensionView
```

#### Overview

A background extension view can be laid out to extend outside the safe area, such as under the titlebar, sidebar, or inspector. By default it lays out its content to stay within the safe area, and uses modifications of the content along the edges to fill the container view.

## Topics

### Instance Properties
- [var automaticallyPlacesContentView: Bool](nsbackgroundextensionview/automaticallyplacescontentview.md)
  Controls the automatic safe area placement of the `contentView` within the container.
- [var contentView: NSView?](nsbackgroundextensionview/contentview.md)
  The content view to extend to fill the `NSBackgroundExtensionView`.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbackgroundextensionview)*