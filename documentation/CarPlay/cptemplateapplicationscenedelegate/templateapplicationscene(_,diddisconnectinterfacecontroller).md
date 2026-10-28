# templateApplicationScene(_:didDisconnectInterfaceController:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when CarPlay removes a scene from the app.

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

CarPlay calls this method after it disconnects the scene. You can use it to perform any cleanup.

> ❗ **Important**:  CarPlay doesn’t call this method for navigation apps. You must implement [`templateApplicationScene(_:didDisconnect:from:)`](./templateapplicationscene%28_,diddisconnect,from%29.md) instead.

## Parameters

- `templateApplicationScene`: The scene disconnecting from the app.
- `interfaceController`: The interface controller for managing the user interface of this scene.

## See Also

### Responding to the Scene Life Cycle
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](./templateapplicationscene%28_,didconnect%29.md)
  Tells the delegate about the addition of a CarPlay scene to the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](./templateapplicationscene%28_,didconnect,to%29.md)
  Tells the delegate about the addition of a CarPlay scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](./templateapplicationscene%28_,diddisconnect,from%29.md)
  Tells the delegate when CarPlay removes a scene from your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnectinterfacecontroller:))*