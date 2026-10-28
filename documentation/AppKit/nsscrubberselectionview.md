# NSScrubberSelectionView

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An abstract base class for specifying the appearance of a highlighted or selected item in a scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
class NSScrubberSelectionView
```

```objc
@interface NSScrubberSelectionView : NSScrubberArrangedView
```

## Overview

Create a subclass to customize the selection or highlight appearance of an item in your scrubber control. You need to return an instance of your subclass from the [`makeSelectionView()`](./nsscrubberselectionstyle/makeselectionview%28%29.md) method on [`NSScrubberSelectionStyle`](./nsscrubberselectionstyle.md).

## Relationships

### Inherits From
- [NSScrubberArrangedView](./nsscrubberarrangedview.md)
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

### Scrubber items
- [class NSScrubberItemView](./nsscrubberitemview.md)
  An item at a specific index position in the scrubber.
- [class NSScrubberArrangedView](./nsscrubberarrangedview.md)
  An abstract base class for the views whose layout is managed by a scrubber.
- [class NSScrubberImageItemView](./nsscrubberimageitemview.md)
  A concrete view subclass for displaying images in a scrubber items.
- [class NSScrubberSelectionStyle](./nsscrubberselectionstyle.md)
  An abstract class that provides decorative accessory views for selected and highlighted items within a scrubber control.
- [class NSScrubberTextItemView](./nsscrubbertextitemview.md)
  A concrete view subclass for displaying text for an item in a scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberselectionview)*