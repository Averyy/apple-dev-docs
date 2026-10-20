# templateApplicationDashboardScene(_:didDisconnect:from:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when CarPlay removes the dashboard scene from your navigation app.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
optional func templateApplicationDashboardScene(_ templateApplicationDashboardScene: CPTemplateApplicationDashboardScene, didDisconnect dashboardController: CPDashboardController, from window: UIWindow)
```

```objc
- (void) templateApplicationDashboardScene:(CPTemplateApplicationDashboardScene *) templateApplicationDashboardScene didDisconnectDashboardController:(CPDashboardController *) dashboardController fromWindow:(UIWindow *) window;
```

#### Discussion

CarPlay calls this method after it disconnects your dashboard scene. You can use it to perform any cleanup.

## Parameters

- `templateApplicationDashboardScene`: The scene disconnecting from the app.
- `dashboardController`: The controller that was managing this scene’s dashboard shortcut buttons.
- `window`: The window where your app was drawing its map content.

## See Also

### Responding to the Scene Life Cycle
- [func templateApplicationDashboardScene(CPTemplateApplicationDashboardScene, didConnect: CPDashboardController, to: UIWindow)](./templateapplicationdashboardscene%28_,didconnect,to%29.md)
  Tells the delegate about the addition of a CarPlay Dashboard scene to your navigation app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscenedelegate/templateapplicationdashboardscene(_:diddisconnect:from:))*