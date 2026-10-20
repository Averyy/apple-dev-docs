# templateApplicationScene(_:didConnect:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate about the addition of a CarPlay scene to the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didConnect interfaceController: CPInterfaceController)
```

```objc
- (void) templateApplicationScene:(CPTemplateApplicationScene *) templateApplicationScene didConnectInterfaceController:(CPInterfaceController *) interfaceController;
```

## Mentions

- [Displaying Content in CarPlay](../displaying-content-in-carplay.md)

#### Discussion

CarPlay calls this method when it launches your app and connects the scene. Use the interface controller to present your user interface templates. You must set the scene’s root template before returning from this method.

> ❗ **Important**:  Navigation apps must implement [`templateApplicationScene(_:didConnect:to:)`](./templateapplicationscene%28_,didconnect,to%29.md) instead so they can access the window where they draw their map content.

## Parameters

- `templateApplicationScene`: The scene connecting to the app.
- `interfaceController`: The interface controller for managing the user interface of this scene.

## See Also

### Responding to the Scene Life Cycle
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](./templateapplicationscene%28_,didconnect,to%29.md)
  Tells the delegate about the addition of a CarPlay scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](./templateapplicationscene%28_,diddisconnectinterfacecontroller%29.md)
  Tells the delegate when CarPlay removes a scene from the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](./templateapplicationscene%28_,diddisconnect,from%29.md)
  Tells the delegate when CarPlay removes a scene from your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:))*