# AUPannerView

**Framework**: CoreAudioKit  
**Kind**: class

A view that provides a specialized user interface for a Cocoa-based panner audio unit.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class AUPannerView
```

## Topics

### Creating a Panner View
- [init(audioUnit: AudioUnit)](aupannerview/init(audiounit:).md)
  Creates a panner view for an audio unit.
### Accessing the Audio Unit
- [var audioUnit: AudioUnit](aupannerview/audiounit.md)
  The panner audio unit associated with the generic panner view.

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AUViewController](auviewcontroller.md)
  The base class to extend when creating a custom user interface for an audio unit.
- [class AUAudioUnitViewConfiguration](auaudiounitviewconfiguration.md)
  A configuration object that describes how to present the audio unit’s user interface.
- [class AUGenericView](augenericview.md)
  A view that provides a generic user interface for a Cocoa audio unit.
- [protocol AUCustomViewPersistentData](aucustomviewpersistentdata.md)
  A protocol that defines the methods an Audio Unit host calls to manage view data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/aupannerview)*