# NSScrubberSelectionView

**Framework**: AppKit  
**Kind**: class

An abstract base class for specifying the appearance of a highlighted or selected item in a scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
class NSScrubberSelectionView
```

#### Overview

Create a subclass to customize the selection or highlight appearance of an item in your scrubber control. You need to return an instance of your subclass from the [`makeSelectionView()`](nsscrubberselectionstyle/makeselectionview().md) method on [`NSScrubberSelectionStyle`](nsscrubberselectionstyle.md).

## Relationships

### Inherits From
- [NSScrubberArrangedView](nsscrubberarrangedview.md)
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

- [class NSScrubberItemView](nsscrubberitemview.md)
  An item at a specific index position in the scrubber.
- [class NSScrubberArrangedView](nsscrubberarrangedview.md)
  An abstract base class for the views whose layout is managed by a scrubber.
- [class NSScrubberImageItemView](nsscrubberimageitemview.md)
  A concrete view subclass for displaying images in a scrubber items.
- [class NSScrubberSelectionStyle](nsscrubberselectionstyle.md)
  An abstract class that provides decorative accessory views for selected and highlighted items within a scrubber control.
- [class NSScrubberTextItemView](nsscrubbertextitemview.md)
  A concrete view subclass for displaying text for an item in a scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberselectionview)*