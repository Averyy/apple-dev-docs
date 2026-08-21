# CABTMIDICentralViewController

**Framework**: CoreAudioKit  
**Kind**: class

A view controller that displays nearby Bluetooth-based MIDI peripherals.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class CABTMIDICentralViewController
```

#### Overview

To let the user search for nearby MIDI peripherals, create a new [`CABTMIDICentralViewController`](cabtmidicentralviewcontroller.md) object and then either present it modally or push it onto a [`UINavigationController`](https://developer.apple.com/documentation/uikit/uinavigationcontroller) view controller. No other configuration of the object is necessary. Once the user interface is visible, the iOS device finds nearby peripherals and displays them to the user. If the user selects a peripheral, it’s automatically paired with this iOS device. The [`CABTMIDICentralViewController`](cabtmidicentralviewcontroller.md) object manages its own user interface and is dismissed automatically.

Once connected, the peripheral appears as a MIDI device, just like any other connected MIDI device. MIDI commands sent to the peripheral are automatically played. For more information, see [`Core MIDI`](https://developer.apple.com/documentation/coremidi).

## Relationships

### Inherits From
- [UITableViewController](../uikit/uitableviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIScrollViewDelegate](../uikit/uiscrollviewdelegate.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITableViewDataSource](../uikit/uitableviewdatasource.md)
- [UITableViewDelegate](../uikit/uitableviewdelegate.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class CABTLEMIDIWindowController](cabtlemidiwindowcontroller.md)
  A window controller that displays nearby Bluetooth-based MIDI peripherals.
- [class CABTMIDILocalPeripheralViewController](cabtmidilocalperipheralviewcontroller.md)
  A view controller that advertises an iOS device as a Bluetooth-based MIDI peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/cabtmidicentralviewcontroller)*