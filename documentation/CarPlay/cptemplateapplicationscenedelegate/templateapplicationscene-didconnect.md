# templateApplicationScene(_:didConnect:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate about the addition of a CarPlay scene to the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didConnect interfaceController: CPInterfaceController)
```

## Mentions

- [Displaying Content in CarPlay](displaying-content-in-carplay.md)

#### Discussion

CarPlay calls this method when it launches your app and connects the scene. Use the interface controller to present your user interface templates. You must set the scene’s root template before returning from this method.

> ❗ **Important**:  Navigation apps must implement [`templateApplicationScene(_:didConnect:to:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md) instead so they can access the window where they draw their map content.

## Parameters

- `templateApplicationScene`: The scene connecting to the app.
- `interfaceController`: The interface controller for managing the user interface of this scene.

## See Also

- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md)
  Tells the delegate about the addition of a CarPlay scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnectinterfacecontroller:).md)
  Tells the delegate when CarPlay removes a scene from the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnect:from:).md)
  Tells the delegate when CarPlay removes a scene from your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:))*