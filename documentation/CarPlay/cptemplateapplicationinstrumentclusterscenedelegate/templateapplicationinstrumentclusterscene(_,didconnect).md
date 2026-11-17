# templateApplicationInstrumentClusterScene(_:didConnect:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that CarPlay added an instrument cluster scene to your app.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
optional func templateApplicationInstrumentClusterScene(_ templateApplicationInstrumentClusterScene: CPTemplateApplicationInstrumentClusterScene, didConnect instrumentClusterController: CPInstrumentClusterController)
```

```objc
- (void) templateApplicationInstrumentClusterScene:(CPTemplateApplicationInstrumentClusterScene *) templateApplicationInstrumentClusterScene didConnectInstrumentClusterController:(CPInstrumentClusterController *) instrumentClusterController;
```

## Discussion

CarPlay calls this method when it adds an instrument cluster scene to your app. The object in the `instrumentClusterController` parameter provides a window you can use to install your custom content and details about additional content to show. Set the [`rootViewController`](../../UIKit/uiwindow/rootviewcontroller.md) property of this window to the view controller you use to manage the content. Present your content using the scene’s suggested interface style, which can get from the scene’s [`contentStyle`](../cptemplateapplicationinstrumentclusterscene/contentstyle.md) property.

## Parameters

- `templateApplicationInstrumentClusterScene`: The instrument cluster scene that CarPlay added.
- `instrumentClusterController`: The object you use to manage the scene’s interface. This type contains the scene’s window in its [`instrumentClusterWindow`](../cpinstrumentclustercontroller/instrumentclusterwindow.md) property.

## See Also

### Responding to the scene life-cycle changes
- [func templateApplicationInstrumentClusterScene(CPTemplateApplicationInstrumentClusterScene, didDisconnectInstrumentClusterController: CPInstrumentClusterController)](./templateapplicationinstrumentclusterscene%28_,diddisconnectinstrumentclustercontroller%29.md)
  Tells the delegate about the removal of an instrument cluster scene from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscenedelegate/templateapplicationinstrumentclusterscene(_:didconnect:))*