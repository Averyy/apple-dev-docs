# RPBroadcastActivityViewController

**Framework**: ReplayKit  
**Kind**: class

A view controller that displays a user interface where users choose a broadcast service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class RPBroadcastActivityViewController
```

#### Overview

The view controller displays the broadcast services currently installed on the device. On iPad, you must present the broadcast activity view controller as a popover.

## Topics

### Presenting the Broadcast Activity UI
- [class func load(handler: (RPBroadcastActivityViewController?, (any Error)?) -> Void)](rpbroadcastactivityviewcontroller/load(handler:).md)
  Loads a broadcast activity view controller.
- [class func load(withPreferredExtension: String?, handler: (RPBroadcastActivityViewController?, (any Error)?) -> Void)](rpbroadcastactivityviewcontroller/load(withpreferredextension:handler:).md)
  Loads a broadcast activity view controller with a preferred extension.
### Getting the Delegate
- [var delegate: (any RPBroadcastActivityViewControllerDelegate)?](rpbroadcastactivityviewcontroller/delegate.md)
  The delegate for the broadcast activity view controller.
- [protocol RPBroadcastActivityViewControllerDelegate](rpbroadcastactivityviewcontrollerdelegate.md)
  The protocol you implement to respond to changes to a broadcast activity user interface.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
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
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class RPSystemBroadcastPickerView](rpsystembroadcastpickerview.md)
  A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- [class RPBroadcastActivityController](rpbroadcastactivitycontroller.md)
  A controller object that presents the macOS broadcast picker.
- [protocol RPBroadcastActivityControllerDelegate](rpbroadcastactivitycontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.
- [class RPBroadcastConfiguration](rpbroadcastconfiguration.md)
  An object used to configure the movie clips produced during a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller)*