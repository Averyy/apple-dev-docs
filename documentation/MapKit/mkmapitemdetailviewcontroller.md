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
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

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