# templateApplicationScene(_:didDisconnectInterfaceController:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate about the removal of a CarPlay scene from your app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didDisconnectInterfaceController interfaceController: CPInterfaceController)
```

```objc
- (void) templateApplicationScene:(CPTemplateApplicationScene *) templateApplicationScene didDisconnectInterfaceController:(CPInterfaceController *) interfaceController;
```

## Discussion

When CarPlay disconnects a scene from your app, it calls this method so you can perform any app-specific cleanup.

> ❗ **Important**: CarPlay calls this method for all app types except navigation apps. If you create a navigation app, implement the [`templateApplicationScene(_:didDisconnect:from:)`](./templateapplicationscene%28_,diddisconnect,from%29.md) method instead of this one.

## Parameters

- `templateApplicationScene`: The scene that CarPlay disconnects from your app.
- `interfaceController`: The controller you use to manage the interface for the scene.

## See Also

### Responding to scene life-cycle events
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](./templateapplicationscene%28_,didconnect%29.md)
  Tells the delegate that CarPlay added a main scene to your app.
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](./templateapplicationscene%28_,didconnect,to%29.md)
  Tells the delegate that CarPlay added a main scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](./templateapplicationscene%28_,diddisconnect,from%29.md)
  Tells the delegate about the removal of a CarPlay scene from your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnectinterfacecontroller:))*