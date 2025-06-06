# templateApplicationScene(_:didDisconnectInterfaceController:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate when CarPlay removes a scene from the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didDisconnectInterfaceController interfaceController: CPInterfaceController)
```

#### Discussion

CarPlay calls this method after it disconnects the scene. You can use it to perform any cleanup.

> ❗ **Important**:  CarPlay doesn’t call this method for navigation apps. You must implement [`templateApplicationScene(_:didDisconnect:from:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnect:from:).md) instead.

 CarPlay doesn’t call this method for navigation apps. You must implement [`templateApplicationScene(_:didDisconnect:from:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnect:from:).md) instead.

## Parameters

- `templateApplicationScene`: The scene disconnecting from the app.
- `interfaceController`: The interface controller for managing the user interface of this scene.

## See Also

- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:).md)
  Tells the delegate about the addition of a CarPlay scene to the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md)
  Tells the delegate about the addition of a CarPlay scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnect:from:).md)
  Tells the delegate when CarPlay removes a scene from your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnectinterfacecontroller:))*