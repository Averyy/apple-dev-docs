# application(_:didSelect:)

**Framework**: CarPlay  
**Kind**: method

Tells the app delegate that the user selected a maneuver.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func application(_ application: UIApplication, didSelect maneuver: CPManeuver)
```

#### Discussion

When your app posts a maneuver while running in the background, CarPlay may display a notification banner. If the user taps the banner, the system displays your app on the CarPlay screen, then calls this method.

## Parameters

- `application`: Your singleton app object.
- `maneuver`: The maneuver selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate/application(_:didselect:)-6ybyy)*