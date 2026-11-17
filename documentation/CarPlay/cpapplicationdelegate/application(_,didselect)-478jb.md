# application(_:didSelect:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

If your application posts a @c CPNavigationAlert while backgrounded, a notification banner may be presented to the user. If the user taps on that banner, your application will launch on the car screen and this method will be called with the alert the user tapped.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate/application(_:didselect:)-478jb)*