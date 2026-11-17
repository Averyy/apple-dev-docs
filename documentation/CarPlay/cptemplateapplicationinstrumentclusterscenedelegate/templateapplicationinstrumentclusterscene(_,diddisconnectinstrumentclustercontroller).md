# templateApplicationInstrumentClusterScene(_:didDisconnectInstrumentClusterController:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate about the removal of an instrument cluster scene from your app.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
optional func templateApplicationInstrumentClusterScene(_ templateApplicationInstrumentClusterScene: CPTemplateApplicationInstrumentClusterScene, didDisconnectInstrumentClusterController instrumentClusterController: CPInstrumentClusterController)
```

```objc
- (void) templateApplicationInstrumentClusterScene:(CPTemplateApplicationInstrumentClusterScene *) templateApplicationInstrumentClusterScene didDisconnectInstrumentClusterController:(CPInstrumentClusterController *) instrumentClusterController;
```

## Discussion

When CarPlay disconnects an instrument cluster scene from your app, it calls this method so you can perform any app-specific cleanup.

## Parameters

- `templateApplicationInstrumentClusterScene`: The scene that CarPlay disconnected from your app.

## See Also

### Responding to the scene life-cycle changes
- [func templateApplicationInstrumentClusterScene(CPTemplateApplicationInstrumentClusterScene, didConnect: CPInstrumentClusterController)](./templateapplicationinstrumentclusterscene%28_,didconnect%29.md)
  Tells the delegate that CarPlay added an instrument cluster scene to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscenedelegate/templateapplicationinstrumentclusterscene(_:diddisconnectinstrumentclustercontroller:))*