# CABTMIDILocalPeripheralViewController

**Framework**: CoreAudioKit  
**Kind**: class  
**Role**: Class

A view controller that advertises an iOS device as a Bluetooth-based MIDI peripheral.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class CABTMIDILocalPeripheralViewController
```

```objc
@interface CABTMIDILocalPeripheralViewController : UIViewController
```

## Overview

To advertise the iOS device as a Bluetooth MIDI peripheral, create a new [`CABTMIDILocalPeripheralViewController`](./cabtmidilocalperipheralviewcontroller.md) object and then either present it modally or push it onto a[`UINavigationController`](../UIKit/uinavigationcontroller.md) view controller. No other configuration of the object is necessary. Once the user interface is displayed, the iOS device is discoverable by another device looking for Bluetooth MIDI peripherals, such as an iOS device displaying a [`CABTMIDICentralViewController`](./cabtmidicentralviewcontroller.md) object. The [`CABTMIDILocalPeripheralViewController`](./cabtmidilocalperipheralviewcontroller.md) object manages its own user interface and is dismissed automatically.

Once connected, the peripheral appears as a MIDI device, just like any other connected MIDI device. MIDI commands sent to the peripheral are automatically played. For more information, see [Core MIDI](../CoreMIDI/CoreMIDI.md).

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Bluetooth Devices
- [class CABTLEMIDIWindowController](./cabtlemidiwindowcontroller.md)
  A window controller that displays nearby Bluetooth-based MIDI peripherals.
- [class CABTMIDICentralViewController](./cabtmidicentralviewcontroller.md)
  A view controller that displays nearby Bluetooth-based MIDI peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/cabtmidilocalperipheralviewcontroller)*