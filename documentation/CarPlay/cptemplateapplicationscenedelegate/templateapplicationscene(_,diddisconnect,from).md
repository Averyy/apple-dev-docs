# templateApplicationScene(_:didDisconnect:from:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when CarPlay removes a scene from your navigation app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didDisconnect interfaceController: CPInterfaceController, from window: CPWindow)
```

```objc
- (void) templateApplicationScene:(CPTemplateApplicationScene *) templateApplicationScene didDisconnectInterfaceController:(CPInterfaceController *) interfaceController fromWindow:(CPWindow *) window;
```

#### Discussion

CarPlay calls this method after it disconnects the scene. You can use it to perform any cleanup.

> ❗ **Important**:  CarPlay calls this method exclusively for navigation apps. All other categories of apps must implement [`templateApplicationScene(_:didDisconnectInterfaceController:)`](./templateapplicationscene%28_,diddisconnectinterfacecontroller%29.md) instead.

## Parameters

- `templateApplicationScene`: The scene disconnecting from the app.
- `interfaceController`: The interface controller for managing the user interface of this scene.
- `window`: The window where the app draws the map content.

## See Also

### Responding to the Scene Life Cycle
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](./templateapplicationscene%28_,didconnect%29.md)
  Tells the delegate about the addition of a CarPlay scene to the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](./templateapplicationscene%28_,didconnect,to%29.md)
  Tells the delegate about the addition of a CarPlay scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](./templateapplicationscene%28_,diddisconnectinterfacecontroller%29.md)
  Tells the delegate when CarPlay removes a scene from the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnect:from:))*