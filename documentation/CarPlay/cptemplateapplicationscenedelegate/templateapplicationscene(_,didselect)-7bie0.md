# templateApplicationScene(_:didSelect:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user selects a navigation alert while the app is in the background.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didSelect navigationAlert: CPNavigationAlert)
```

```objc
- (void) templateApplicationScene:(CPTemplateApplicationScene *) templateApplicationScene didSelectNavigationAlert:(CPNavigationAlert *) navigationAlert;
```

## Discussion

If your navigation app posts a navigation alert while in the background, CarPlay displays a notification banner to the user. If the user taps the banner, CarPlay brings your navigation app to the foreground and calls this method.

## Parameters

- `templateApplicationScene`: The active scene.
- `navigationAlert`: The selected navigation alert.

## See Also

### Responding to User Actions
- [func templateApplicationScene(CPTemplateApplicationScene, didSelect: CPManeuver)](./templateapplicationscene%28_,didselect%29-5rf2h.md)
  Tells the delegate when the user selects a maneuver while the app is in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:didselect:)-7bie0)*