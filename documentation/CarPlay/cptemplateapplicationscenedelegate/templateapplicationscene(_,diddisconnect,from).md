# templateApplicationScene(_:didDisconnect:from:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate about the removal of a CarPlay scene from your navigation app.

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

## Discussion

When CarPlay disconnects a scene from your navigation app, it calls this method so you can perform any app-specific cleanup.

> ❗ **Important**: CarPlay calls this method exclusively for navigation apps. If you create a different type of app, implement the [`templateApplicationScene(_:didDisconnectInterfaceController:)`](./templateapplicationscene%28_,diddisconnectinterfacecontroller%29.md) method instead of this one.

## Parameters

- `templateApplicationScene`: The scene that CarPlay disconnects from your app.
- `interfaceController`: The controller you use to manage the interface for the scene.
- `window`: The window you use to draw your app’s map content.

## See Also

### Responding to scene life-cycle events
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](./templateapplicationscene%28_,didconnect%29.md)
  Tells the delegate that CarPlay added a main scene to your app.
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](./templateapplicationscene%28_,didconnect,to%29.md)
  Tells the delegate that CarPlay added a main scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](./templateapplicationscene%28_,diddisconnectinterfacecontroller%29.md)
  Tells the delegate about the removal of a CarPlay scene from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnect:from:))*