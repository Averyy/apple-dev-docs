# AudioAccessoryKit

**Framework**: AudioAccessoryKit  
**Kind**: module

Support audio features like automatic audio switching.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

#### Overview

AudioAccessoryKit makes it possible for third-party audio accessory manufacturers to provide headphone information to the system to support automatic audio switching. For example, when someone takes off their earbuds, their iPhone can route audio to its speakers.  The accessory’s companion app updates the earbuds’ placement from [`AccessoryControlDevice.Placement.inEar`](accessorycontroldevice/placement/inear.md) to [`AccessoryControlDevice.Placement.offHead`](accessorycontroldevice/placement/offhead.md). iOS reroutes the audio intelligently, rather than continuing to play audio on the distant accessory.

Your companion app pairs the accessory using [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit), then uses AudioAccessoryKit to register the accessory’s capabilities, such as [`placement`](accessorycontroldevice/capabilities/placement.md).  In addition to placement information, your accessory communicates connected audio sources. To participate in automatic audio switching, keep the system up-to-date about your accessory’s state changes.

> ❗ **Important**:  This framework supports iPhone and iPad only. You can develop and test an app that uses this framework on devices in any region. Customer installations of your app can use the framework only on devices located in the EU that are signed in with an Apple Account with an EU country or region.

## Topics

### Essentials
- [Supporting automatic audio switching for third-party accessories](supporting-automatic-audio-switching.md)
  Configure your audio accessory to support seamless audio routing between connected devices.
### Audio configuration
- [class AccessoryControlDevice](accessorycontroldevice.md)
  A configuration object that manages audio accessory capabilities and state.
### Device characteristics
- [AccessoryControlDevice.Placement](accessorycontroldevice/placement.md)
  The physical placement of an audio accessory.
- [AccessoryControlDevice.Capabilities](accessorycontroldevice/capabilities.md)
  A set of capabilities that an audio accessory supports.
- [AccessoryControlDevice.Configuration](accessorycontroldevice/configuration-swift.struct.md)
  The configuration for an accessory.
### Errors
- [AccessoryControlDevice.Error](accessorycontroldevice/error.md)
  An error that occurs during audio accessory configuration operations.
### Classes
- [class AudioAccessoryHeadTracking](audioaccessoryheadtracking.md)
### Structures
- [struct AccessorySensorUpdates](accessorysensorupdates.md)
  Subscribes to a stream of raw sensor data packets from a connected accessory.
### Enumerations
- [enum AudioAccessoryError](audioaccessoryerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AudioAccessoryKit)*