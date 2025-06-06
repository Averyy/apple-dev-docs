# CoreAudioKit

**Framework**: CoreAudioKit  
**Kind**: module

Add user interfaces to audio units.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- visionOS 1.0+

#### Overview

Core Audio Kit provides views and controllers to use when building Audio Unit user interfaces.

## Topics

### Audio Units
- [class AUViewController](auviewcontroller.md)
  The base class to extend when creating a custom user interface for an audio unit.
- [class AUAudioUnitViewConfiguration](auaudiounitviewconfiguration.md)
  A configuration object that describes how to present the audio unit’s user interface.
- [class AUGenericView](augenericview.md)
  A view that provides a generic user interface for a Cocoa audio unit.
- [class AUPannerView](aupannerview.md)
  A view that provides a specialized user interface for a Cocoa-based panner audio unit.
- [protocol AUCustomViewPersistentData](aucustomviewpersistentdata.md)
  A protocol that defines the methods an Audio Unit host calls to manage view data.
### Bluetooth Devices
- [class CABTLEMIDIWindowController](cabtlemidiwindowcontroller.md)
  A window controller that displays nearby Bluetooth-based MIDI peripherals.
- [class CABTMIDICentralViewController](cabtmidicentralviewcontroller.md)
  A view controller that displays nearby Bluetooth-based MIDI peripherals.
- [class CABTMIDILocalPeripheralViewController](cabtmidilocalperipheralviewcontroller.md)
  A view controller that advertises an iOS device as a Bluetooth-based MIDI peripheral.
### Network Devices
- [class CANetworkBrowserWindowController](canetworkbrowserwindowcontroller.md)
  A window controller that displays available network audio devices.
### Inter-Device Audio
- [class CAInterDeviceAudioViewController](cainterdeviceaudioviewcontroller.md)
  A view controller object that displays iOS devices that support inter-device audio.
### Inter-App Audio
- [class CAInterAppAudioSwitcherView](cainterappaudioswitcherview.md)
  A view that provides an audio switcher user interface.
- [class CAInterAppAudioTransportView](cainterappaudiotransportview.md)
  A view that provides an audio transport user interface.
### Deprecations
- [class AUGenericViewInternal](augenericviewinternal.md)
- [typealias AUGenericViewInternalBase](augenericviewinternalbase.md)
### Classes
- [class AUAppleCustomViewLoader](auapplecustomviewloader.md)
- [class AUGenericViewController](augenericviewcontroller.md)
### Structures
- [struct AUGenericViewDisplayFlags](augenericviewdisplayflags.md)
  Flags that describe the display of a generic view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreAudioKit)*