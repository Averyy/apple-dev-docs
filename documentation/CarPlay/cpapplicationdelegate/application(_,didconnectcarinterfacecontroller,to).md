# application(_:didConnectCarInterfaceController:to:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the app delegate that the app connected to the CarPlay interface.

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

## Parameters

- `application`: Your singleton app object.
- `interfaceController`: The interface controller provided by CarPlay. Your app should maintain a reference to this controller.
- `window`: The CarPlay window. Your app should create its view controller and assign the controller to the [`rootViewController`](../../UIKit/uiwindow/rootviewcontroller.md) property of this window.

## See Also

### Connecting to the CarPlay Interface
- [func application(UIApplication, didDisconnectCarInterfaceController: CPInterfaceController, from: CPWindow)](./application%28_,diddisconnectcarinterfacecontroller,from%29.md)
  Tells the app delegate that the app disconnected from the CarPlay interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate/application(_:didconnectcarinterfacecontroller:to:))*