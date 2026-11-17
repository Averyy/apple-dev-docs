# CPInstrumentClusterControllerDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The methods for responding to changes to instrument cluster settings.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
protocol CPInstrumentClusterControllerDelegate : NSObjectProtocol
```

```objc
@protocol CPInstrumentClusterControllerDelegate <NSObject>
```

## Overview

When the instrument cluster settings change, a [`CPInstrumentClusterController`](./cpinstrumentclustercontroller.md) object notifies its associated delegate object. The `CPInstrumentClusterControllerDelegate` protocol defines the methods you implement in that delegate object to receive and handle the changes. The system notifies your delegate object when the window you use to display your interface changes, when speed limit and compass settings change, or when there’s a request to change the zoom level of the map content you’re displaying.

Adopt this protocol in a custom type you define. When CarPlay creates your app’s instrument cluster scene, instantiate your custom type and assign it to the [`delegate`](./cpinstrumentclustercontroller/delegate.md) property of the controller object you use to configure your UI.

## Topics

### Responding to life-cycle events
- [func instrumentClusterControllerDidConnect(UIWindow)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdidconnect%28_%29.md)
  Tells the delegate that there’s a new window for displaying your content.
- [func instrumentClusterControllerDidDisconnectWindow(UIWindow)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdiddisconnectwindow%28_%29.md)
  Tells the delegate that the system removed the window you use to draw your content.
### Responding to setting changes
- [func instrumentClusterController(CPInstrumentClusterController, didChangeSpeedLimitSetting: CPInstrumentClusterSetting)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontroller%28_,didchangespeedlimitsetting%29.md)
  Tells the delegate to adjust how your app displays speed limit information.
- [func instrumentClusterController(CPInstrumentClusterController, didChangeCompassSetting: CPInstrumentClusterSetting)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontroller%28_,didchangecompasssetting%29.md)
  Tells the delegate to adjust how your app displays compass information.
### Handling zoom events
- [func instrumentClusterControllerDidZoom(in: CPInstrumentClusterController)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdidzoom%28in%29.md)
  Tells the delegate to increase map magnification by one level.
- [func instrumentClusterControllerDidZoomOut(CPInstrumentClusterController)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdidzoomout%28_%29.md)
  Tells the delegate to decrease map magnification by one level.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Instrument cluster display
- [class CPTemplateApplicationInstrumentClusterScene](./cptemplateapplicationinstrumentclusterscene.md)
  A CarPlay scene that presents navigation-related instructions in the vehicle’s instrument display.
- [protocol CPTemplateApplicationInstrumentClusterSceneDelegate](./cptemplateapplicationinstrumentclusterscenedelegate.md)
  The methods for responding to the life cycle events in your app’s instrument cluster scene.
- [class CPInstrumentClusterController](./cpinstrumentclustercontroller.md)
  The controller you use to configure and manage your instrument cluster interface.
- [enum CPInstrumentClusterSetting](./cpinstrumentclustersetting.md)
  Constants that indicate when to include or exclude vehicle-related data in your custom content.
- [CPSupportsInstrumentClusterNavigationScene](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontrollerdelegate)*