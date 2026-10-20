# application(_:didDisconnectCarInterfaceController:from:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the app delegate that the app disconnected from the CarPlay interface.

**Availability**:
- iOS 12.0+ - Deprecated in 13.0
- iPadOS 12.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func application(_ application: UIApplication, didDisconnectCarInterfaceController interfaceController: CPInterfaceController, from window: CPWindow)
```

```objc
- (void) application:(UIApplication *) application didDisconnectCarInterfaceController:(CPInterfaceController *) interfaceController fromWindow:(CPWindow *) window;
```

## Parameters

- `application`: Your singleton app object.
- `interfaceController`: The interface controller provided by CarPlay. Your app should release its reference to this controller.
- `window`: The CarPlay window.

## See Also

### Connecting to the CarPlay Interface
- [func application(UIApplication, didConnectCarInterfaceController: CPInterfaceController, to: CPWindow)](./application%28_,didconnectcarinterfacecontroller,to%29.md)
  Tells the app delegate that the app connected to the CarPlay interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate/application(_:diddisconnectcarinterfacecontroller:from:))*