# application(_:didConnectCarInterfaceController:to:)

**Framework**: CarPlay  
**Kind**: method  
**Required**: Yes

Tells the app delegate that the app connected to the CarPlay interface.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func application(_ application: UIApplication, didConnectCarInterfaceController interfaceController: CPInterfaceController, to window: CPWindow)
```

## Parameters

- `application`: Your singleton app object.
- `interfaceController`: The interface controller provided by CarPlay. Your app should maintain a reference to this controller.
- `window`: The CarPlay window. Your app should create its view controller and assign the controller to the   property of this window.

## See Also

- [func application(UIApplication, didDisconnectCarInterfaceController: CPInterfaceController, from: CPWindow)](cpapplicationdelegate/application(_:diddisconnectcarinterfacecontroller:from:).md)
  Tells the app delegate that the app disconnected from the CarPlay interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate/application(_:didconnectcarinterfacecontroller:to:))*