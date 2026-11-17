# templateApplicationScene(_:didSelect:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells your navigation app when someone selects a maneuver while your app is in the background.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, didSelect maneuver: CPManeuver)
```

```objc
- (void) templateApplicationScene:(CPTemplateApplicationScene *) templateApplicationScene didSelectManeuver:(CPManeuver *) maneuver;
```

## Discussion

If your navigation app posts a maneuver while in the background, CarPlay displays a notification banner on the vehicle display. If the person taps the banner, CarPlay brings your app to the foreground and calls this method.

## Parameters

- `templateApplicationScene`: The active scene.
- `maneuver`: The selected maneuver.

## See Also

### Responding to interactions
- [func templateApplicationScene(CPTemplateApplicationScene, didSelect: CPNavigationAlert)](./templateapplicationscene%28_,didselect%29-7bie0.md)
  Tells your navigation app that someone selected a navigation alert while your app was in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/templateapplicationscene(_:didselect:)-5rf2h)*