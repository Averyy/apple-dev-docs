# templateApplicationScene(_:didConnect:to:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that CarPlay added a main scene to your navigation app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didConnect interfaceController: CPInterfaceController, to window: CPWindow)
```

```objc
- (void) templateApplicationScene:(CPTemplateApplicationScene *) templateApplicationScene didConnectInterfaceController:(CPInterfaceController *) interfaceController toWindow:(CPWindow *) window;
```

## Mentions

- [Building your app’s initial CarPlay interface](../building-your-apps-initial-carplay-interface.md)

## Discussion

CarPlay calls this method when it launches your navigation app and connects a scene. This method is the entry point for your app, and you use it to prepare your app and configure its interface. In your implementation, set the root view controller of the provided `window` object to the view controller object you use to display your custom map content. In addition, set the root template of the provided `interfaceController` object to an instance of the [`CPMapTemplate`](../cpmaptemplate.md) type. CarPlay requires you to install the root template and set the window’s view controller before this method returns.

> ❗ **Important**: CarPlay calls this method exclusively for navigation apps. If you create a different type of app, implement the [`templateApplicationScene(_:didDisconnect:from:)`](./templateapplicationscene%28_,diddisconnect,from%29.md) method instead of this one.

## Parameters

- `templateApplicationScene`: The new scene that CarPlay creates.
- `interfaceController`: The object you use to manage the interface for the scene.
- `window`: The window you use to draw your app’s map content.

## See Also

### Responding to scene life-cycle events
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](./templateapplicationscene%28_,didconnect%29.md)
  Tells the delegate that CarPlay added a main scene to your app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](./templateapplicationscene%28_,diddisconnectinterfacecontroller%29.md)
  Tells the delegate about the removal of a CarPlay scene from your app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](./templateapplicationscene%28_,diddisconnect,from%29.md)
  Tells the delegate about the removal of a CarPlay scene from your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:))*