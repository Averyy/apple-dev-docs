# application(_:didConnectCarInterfaceController:to:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The CarPlay screen has connected and is ready to present content.

**Availability**:
- iOS 12.0+ - Deprecated in 13.0
- iPadOS 12.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func application(_ application: UIApplication, didConnectCarInterfaceController interfaceController: CPInterfaceController, to window: CPWindow)
```

```objc
- (void) application:(UIApplication *) application didConnectCarInterfaceController:(CPInterfaceController *) interfaceController toWindow:(CPWindow *) window;
```

## Discussion

Your app should create its view controller and assign it to the @c rootViewController property of this window.

> **Note**: It is the responsibility of the delegate to maintain a reference to the interface controller beyond the scope of this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate/application(_:didconnectcarinterfacecontroller:to:))*