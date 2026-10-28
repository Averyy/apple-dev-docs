# application(_:didSelect:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the app delegate that the user selected an action from a navigation alert.

**Availability**:
- iOS 12.0+ - Deprecated in 13.0
- iPadOS 12.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
optional func application(_ application: UIApplication, didSelect navigationAlert: CPNavigationAlert)
```

```objc
- (void) application:(UIApplication *) application didSelectNavigationAlert:(CPNavigationAlert *) navigationAlert;
```

## Discussion

When your app posts a navigation alert while running in the background, CarPlay may display a notification banner. If the user taps the banner, the system displays your app on the CarPlay screen, then calls this method.

## Parameters

- `application`: Your singleton app object.
- `navigationAlert`: The alert tapped by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate/application(_:didselect:)-478jb)*