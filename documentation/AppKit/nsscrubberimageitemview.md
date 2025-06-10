# NSScrubberImageItemView

**Framework**: AppKit  
**Kind**: class

A concrete view subclass for displaying images in a scrubber items.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSScrubberImageItemView
```

#### Overview

Provide the image you want to display in the scrubber item to the [`image`](nsscrubberimageitemview/image.md) property. If you want finer control over the appearance of the image, you can access the underlying image view using the [`imageView`](nsscrubberimageitemview/imageview.md) property.

The image is scaled proportionally to fit the view’s frame. Use the [`imageAlignment`](nsscrubberimageitemview/imagealignment.md) property to determine how the scaled image is cropped within that frame.

## Topics

### Providing image content
- [var image: NSImage](nsscrubberimageitemview/image.md)
  The image displayed by the scrubber item.
- [var imageView: NSImageView](nsscrubberimageitemview/imageview.md)
  The image view that the scrubber item uses to display its image.
### Configuring the appearance
- [var imageAlignment: NSImageAlignment](nsscrubberimageitemview/imagealignment.md)
  The alignment of the image within the scrubber item.

## Relationships

### Inherits From
- [NSScrubberItemView](nsscrubberitemview.md)
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

- [class NSScrubberItemView](nsscrubberitemview.md)
  An item at a specific index position in the scrubber.
- [class NSScrubberArrangedView](nsscrubberarrangedview.md)
  An abstract base class for the views whose layout is managed by a scrubber.
- [class NSScrubberSelectionStyle](nsscrubberselectionstyle.md)
  An abstract class that provides decorative accessory views for selected and highlighted items within a scrubber control.
- [class NSScrubberSelectionView](nsscrubberselectionview.md)
  An abstract base class for specifying the appearance of a highlighted or selected item in a scrubber.
- [class NSScrubberTextItemView](nsscrubbertextitemview.md)
  A concrete view subclass for displaying text for an item in a scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberimageitemview)*