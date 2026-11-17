# templateApplicationScene(_:didConnect:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that CarPlay added a main scene to your app.

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

- [Building your app’s initial CarPlay interface](../building-your-apps-initial-carplay-interface.md)

## Discussion

CarPlay calls this method when it connects a new scene to a non-navigation app. This method is an entry point for your app, and you use it to prepare your app’s interface and any other content you need. In your implementation of this method, prepare the root template for your interface and install it using the object in the `interfaceController` parameter. CarPlay requires you to install a root template before this method returns.

> ❗ **Important**: CarPlay calls this method for all app types except navigation apps. If you create a navigation app, implement the [`templateApplicationScene(_:didConnect:to:)`](./templateapplicationscene%28_,didconnect,to%29.md) method instead of this one.

## Parameters

- `templateApplicationScene`: The new scene that CarPlay creates.
- `interfaceController`: The object you use to manage the interface for the scene.

## See Also

### Responding to scene life-cycle events
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](./templateapplicationscene%28_,didconnect,to%29.md)
  Tells the delegate that CarPlay added a main scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](./templateapplicationscene%28_,diddisconnectinterfacecontroller%29.md)
  Tells the delegate about the removal of a CarPlay scene from your app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](./templateapplicationscene%28_,diddisconnect,from%29.md)
  Tells the delegate about the removal of a CarPlay scene from your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:))*