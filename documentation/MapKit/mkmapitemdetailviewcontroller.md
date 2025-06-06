# MKMapItemDetailViewController

**Framework**: MapKit  
**Kind**: class

An object that displays detailed information about a map item.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class MKMapItemDetailViewController
```

#### Overview

The view controller presents modally and displays place information such as addresses and phone numbers.

This class doesn’t support subclassing. The view hierarchy for this class is private and must not be modified.

## Topics

### Creating a map item detail view controller
- [init(mapItem: MKMapItem?)](mkmapitemdetailviewcontroller/init(mapitem:).md)
  Create a map item detail view controller.
- [init(mapItem: MKMapItem?, displaysMap: Bool)](mkmapitemdetailviewcontroller/init(mapitem:displaysmap:).md)
  Create a map item detail view controller
### Dismissing the map item detail interface
- [var delegate: (any MKMapItemDetailViewControllerDelegate)?](mkmapitemdetailviewcontroller/delegate.md)
  The map item detail view controller’s delegate.
### Getting and setting the map item
- [var mapItem: MKMapItem?](mkmapitemdetailviewcontroller/mapitem.md)
  The map item to display.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
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

- [protocol MKMapItemDetailViewControllerDelegate](mkmapitemdetailviewcontrollerdelegate.md)
  The methods that you use to receive events from an associated map view controller.
- [MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle.md)
  The type of map item detail accessory presentation to use.
- [class MKSelectionAccessory](mkselectionaccessory.md)
  The type of accessory to display for a selected annotation.
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle.md)
  The style to use for a map item detail callout presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemdetailviewcontroller)*