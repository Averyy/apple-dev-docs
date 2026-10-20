# NSScrubberArrangedView

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An abstract base class for the views whose layout is managed by a scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
class NSScrubberArrangedView
```

```objc
@interface NSScrubberArrangedView : NSView
```

## Topics

### Managing selection and highlighting
- [var isHighlighted: Bool](./nsscrubberarrangedview/ishighlighted.md)
  A Boolean value that specifies whether the view is currently highlighted.
- [var isSelected: Bool](./nsscrubberarrangedview/isselected.md)
  A Boolean value that specifies whether the current view is selected.
### Controlling the layout
- [func apply(NSScrubberLayoutAttributes)](./nsscrubberarrangedview/apply%28_%29.md)
  Updates the layout of the arranged view to respect the provided layout attributes.

## Relationships

### Inherits From
- [NSView](./nsview.md)
### Inherited By
- [NSScrubberItemView](./nsscrubberitemview.md)
- [NSScrubberSelectionView](./nsscrubberselectionview.md)
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
- [class NSScrubberImageItemView](./nsscrubberimageitemview.md)
  A concrete view subclass for displaying images in a scrubber items.
- [class NSScrubberSelectionStyle](./nsscrubberselectionstyle.md)
  An abstract class that provides decorative accessory views for selected and highlighted items within a scrubber control.
- [class NSScrubberSelectionView](./nsscrubberselectionview.md)
  An abstract base class for specifying the appearance of a highlighted or selected item in a scrubber.
- [class NSScrubberTextItemView](./nsscrubbertextitemview.md)
  A concrete view subclass for displaying text for an item in a scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberarrangedview)*