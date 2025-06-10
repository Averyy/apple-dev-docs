# templateApplicationScene(_:didConnect:to:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate about the addition of a CarPlay scene to your navigation app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didConnect interfaceController: CPInterfaceController, to window: CPWindow)
```

## Mentions

- [Displaying Content in CarPlay](displaying-content-in-carplay.md)

#### Discussion

CarPlay calls this method when it launches your navigation app and connects the scene. Create an instance of your map-drawing view controller and assign it to the window’s root view controller. Use the interface controller to present your user interface templates. You must set both the window’s root view controller and the scene’s root template before returning from this method.

> ❗ **Important**:  CarPlay calls this method exclusively for navigation apps. All other categories of apps must implement [`templateApplicationScene(_:didConnect:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:).md) instead.

## Parameters

- `templateApplicationScene`: The scene connecting to the app.
- `interfaceController`: The interface controller for managing the user interface of this scene.
- `window`: The window where the app draws the map content.

## See Also

- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:).md)
  Tells the delegate about the addition of a CarPlay scene to the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnectinterfacecontroller:).md)
  Tells the delegate when CarPlay removes a scene from the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnect:from:).md)
  Tells the delegate when CarPlay removes a scene from your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:))*