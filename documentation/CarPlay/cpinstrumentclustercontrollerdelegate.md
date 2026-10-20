# CPInstrumentClusterControllerDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

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

## Topics

### Instance Methods
- [func instrumentClusterController(CPInstrumentClusterController, didChangeCompassSetting: CPInstrumentClusterSetting)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontroller%28_,didchangecompasssetting%29.md)
- [func instrumentClusterController(CPInstrumentClusterController, didChangeSpeedLimitSetting: CPInstrumentClusterSetting)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontroller%28_,didchangespeedlimitsetting%29.md)
- [func instrumentClusterControllerDidConnect(UIWindow)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdidconnect%28_%29.md)
- [func instrumentClusterControllerDidDisconnectWindow(UIWindow)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdiddisconnectwindow%28_%29.md)
- [func instrumentClusterControllerDidZoom(in: CPInstrumentClusterController)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdidzoom%28in%29.md)
- [func instrumentClusterControllerDidZoomOut(CPInstrumentClusterController)](./cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdidzoomout%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Instrument cluster
- [class CPInstrumentClusterController](./cpinstrumentclustercontroller.md)
- [class CPTemplateApplicationInstrumentClusterScene](./cptemplateapplicationinstrumentclusterscene.md)
- [protocol CPTemplateApplicationInstrumentClusterSceneDelegate](./cptemplateapplicationinstrumentclusterscenedelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontrollerdelegate)*