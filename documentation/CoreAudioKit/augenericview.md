# AUGenericView

**Framework**: CoreAudioKit  
**Kind**: class  
**Role**: Class

A view that provides a generic user interface for a Cocoa audio unit.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class AUGenericView
```

```objc
@interface AUGenericView : NSView
```

## Topics

### Creating a Generic View
- [init(audioUnit: AudioUnit)](./augenericview/init%28audiounit%29.md)
  Creates a generic view for an audio unit, setting all display flags.
- [init(audioUnit: AudioUnit, displayFlags: AUGenericViewDisplayFlags)](./augenericview/init%28audiounit,displayflags%29.md)
  Initializes a generic view for an audio unit, setting specific display flags.
### Configuring a View
- [var showsExpertParameters: Bool](./augenericview/showsexpertparameters.md)
  Indicates whether or not controls for expert audio unit parameters are displayed in the generic view.
### Accessing the Audio Unit
- [var audioUnit: AudioUnit](./augenericview/audiounit.md)
  The audio unit associated with the generic view.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [AUCustomViewPersistentData](./aucustomviewpersistentdata.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Audio Units
- [class AUViewController](./auviewcontroller.md)
  The base class to extend when creating a custom user interface for an audio unit.
- [class AUAudioUnitViewConfiguration](./auaudiounitviewconfiguration.md)
  A configuration object that describes how to present the audio unit’s user interface.
- [class AUPannerView](./aupannerview.md)
  A view that provides a specialized user interface for a Cocoa-based panner audio unit.
- [protocol AUCustomViewPersistentData](./aucustomviewpersistentdata.md)
  A protocol that defines the methods an Audio Unit host calls to manage view data.
- [AUViewControllerBase](./auviewcontrollerbase.md)
  A type definition that indicates the the platform’s Audio Unit view controller base class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/augenericview)*