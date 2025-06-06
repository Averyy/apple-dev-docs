# templateApplicationDashboardScene(_:didConnect:to:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate about the addition of a CarPlay Dashboard scene to your navigation app.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
optional func templateApplicationDashboardScene(_ templateApplicationDashboardScene: CPTemplateApplicationDashboardScene, didConnect dashboardController: CPDashboardController, to window: UIWindow)
```

## Mentions

- [Displaying Content in CarPlay](displaying-content-in-carplay.md)

#### Discussion

CarPlay calls this method when it connects a dashboard scene to your navigation app. Create an instance of your map-drawing view controller and assign it as the window’s root view controller. Use the dashboard controller to provide up to two shortcut buttons to display instead of your map content when there’s no active navigation session.

## Parameters

- `templateApplicationDashboardScene`: The scene connecting to the app.
- `dashboardController`: The controller that manages the scene’s dashboard shortcut buttons.
- `window`: The window where your app draws its map content.

## See Also

- [func templateApplicationDashboardScene(CPTemplateApplicationDashboardScene, didDisconnect: CPDashboardController, from: UIWindow)](cptemplateapplicationdashboardscenedelegate/templateapplicationdashboardscene(_:diddisconnect:from:).md)
  Tells the delegate when CarPlay removes the dashboard scene from your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscenedelegate/templateapplicationdashboardscene(_:didconnect:to:))*