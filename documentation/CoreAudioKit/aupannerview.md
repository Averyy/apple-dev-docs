# AUPannerView

**Framework**: CoreAudioKit  
**Kind**: class

A view that provides a specialized user interface for a Cocoa-based panner audio unit.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
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
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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