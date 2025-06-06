# templateApplicationScene(_:didDisconnect:from:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate when CarPlay removes a scene from your navigation app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didDisconnect interfaceController: CPInterfaceController, from window: CPWindow)
```

#### Discussion

CarPlay calls this method after it disconnects the scene. You can use it to perform any cleanup.

> ❗ **Important**:  CarPlay calls this method exclusively for navigation apps. All other categories of apps must implement [`templateApplicationScene(_:didDisconnectInterfaceController:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnectinterfacecontroller:).md) instead.

 CarPlay calls this method exclusively for navigation apps. All other categories of apps must implement [`templateApplicationScene(_:didDisconnectInterfaceController:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnectinterfacecontroller:).md) instead.

## Parameters

- `templateApplicationScene`: The scene disconnecting from the app.
- `interfaceController`: The interface controller for managing the user interface of this scene.
- `window`: The window where the app draws the map content.

## See Also

- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:).md)
  Tells the delegate about the addition of a CarPlay scene to the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md)
  Tells the delegate about the addition of a CarPlay scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnectinterfacecontroller:).md)
  Tells the delegate when CarPlay removes a scene from the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnect:from:))*