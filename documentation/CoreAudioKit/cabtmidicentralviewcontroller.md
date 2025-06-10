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
@MainActor
class CABTMIDICentralViewController
```

#### Overview

To let the user search for nearby MIDI peripherals, create a new [`CABTMIDICentralViewController`](cabtmidicentralviewcontroller.md) object and then either present it modally or push it onto a [`UINavigationController`](https://developer.apple.com/documentation/UIKit/UINavigationController) view controller. No other configuration of the object is necessary. Once the user interface is visible, the iOS device finds nearby peripherals and displays them to the user. If the user selects a peripheral, it’s automatically paired with this iOS device. The [`CABTMIDICentralViewController`](cabtmidicentralviewcontroller.md) object manages its own user interface and is dismissed automatically.

Once connected, the peripheral appears as a MIDI device, just like any other connected MIDI device. MIDI commands sent to the peripheral are automatically played. For more information, see [`Core MIDI`](https://developer.apple.com/documentation/CoreMIDI).

## Relationships

### Inherits From
- [UITableViewController](../UIKit/UITableViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIScrollViewDelegate](../UIKit/UIScrollViewDelegate.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITableViewDataSource](../UIKit/UITableViewDataSource.md)
- [UITableViewDelegate](../UIKit/UITableViewDelegate.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class CABTLEMIDIWindowController](cabtlemidiwindowcontroller.md)
  A window controller that displays nearby Bluetooth-based MIDI peripherals.
- [class CABTMIDILocalPeripheralViewController](cabtmidilocalperipheralviewcontroller.md)
  A view controller that advertises an iOS device as a Bluetooth-based MIDI peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/cabtmidicentralviewcontroller)*