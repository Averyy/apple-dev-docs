# CPInstrumentClusterController

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

The controller you use to configure and manage your instrument cluster interface.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
class CPInstrumentClusterController
```

```objc
@interface CPInstrumentClusterController : NSObject
```

## Overview

During the creation of an instrument cluster scene, CarPlay creates a `CPInstrumentClusterController` object to manage the scene’s content. Use this object to configure the UI you want to display in the instrument cluster. To build your instrument cluster UI, create a [`UIViewController`](../UIKit/uiviewcontroller.md), fill it with your app-specific content, and attach it to the window provided by this controller object.

Don’t instantiate this type directly. If your app and the vehicle support content in the instrument cluster, CarPlay creates a [`CPTemplateApplicationInstrumentClusterScene`](./cptemplateapplicationinstrumentclusterscene.md), the scene’s delegate object, and an instance of this type automatically. The system passes the newly created `CPInstrumentClusterController` object to the delegate object at startup. You can also access the object from the scene’s [`instrumentClusterController`](./cptemplateapplicationinstrumentclusterscene/instrumentclustercontroller.md) property.

When the instrument cluster settings change, the `CPInstrumentClusterController` object notifies its associated delegate object. To receive the notifications, implement the [`CPInstrumentClusterControllerDelegate`](./cpinstrumentclustercontrollerdelegate.md) protocol in a custom type and assign an instance of that type to the [`delegate`](./cpinstrumentclustercontroller/delegate.md) property of the controller. Assign your delegate object to the controller at the same time you set up the interface for your instrument cluster scene.

## Topics

### Configuring your instrument cluster interface
- [var instrumentClusterWindow: UIWindow?](./cpinstrumentclustercontroller/instrumentclusterwindow.md)
  The window you use to display your instrument cluster interface.
- [var inactiveDescriptionVariants: [String]](./cpinstrumentclustercontroller/inactivedescriptionvariants.md)
  Strings for the vehicle to display in the instrument cluster when navigation isn’t active for your app.
- [var attributedInactiveDescriptionVariants: [NSAttributedString]](./cpinstrumentclustercontroller/attributedinactivedescriptionvariants.md)
  Attributed strings for the vehicle to display in the instrument cluster when navigation isn’t active for your app.
- [var speedLimitSetting: CPInstrumentClusterSetting](./cpinstrumentclustercontroller/speedlimitsetting.md)
  A value that indicates whether to show speed limit information as part of your content.
- [var compassSetting: CPInstrumentClusterSetting](./cpinstrumentclustercontroller/compasssetting.md)
  A value that indicates whether to show compass information as part of your content.
### Managing the instrument cluster content
- [var delegate: (any CPInstrumentClusterControllerDelegate)?](./cpinstrumentclustercontroller/delegate.md)
  The custom object you provide to handle controller-related events.
- [protocol CPInstrumentClusterControllerDelegate](./cpinstrumentclustercontrollerdelegate.md)
  The methods for responding to changes to instrument cluster settings.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Instrument cluster display
- [class CPTemplateApplicationInstrumentClusterScene](./cptemplateapplicationinstrumentclusterscene.md)
  A CarPlay scene that presents navigation-related instructions in the vehicle’s instrument display.
- [protocol CPTemplateApplicationInstrumentClusterSceneDelegate](./cptemplateapplicationinstrumentclusterscenedelegate.md)
  The methods for responding to the life cycle events in your app’s instrument cluster scene.
- [protocol CPInstrumentClusterControllerDelegate](./cpinstrumentclustercontrollerdelegate.md)
  The methods for responding to changes to instrument cluster settings.
- [enum CPInstrumentClusterSetting](./cpinstrumentclustersetting.md)
  Constants that indicate when to include or exclude vehicle-related data in your custom content.
- [CPSupportsInstrumentClusterNavigationScene](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontroller)*