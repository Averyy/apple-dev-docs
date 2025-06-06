# application(_:didDisconnectCarInterfaceController:from:)

**Framework**: CarPlay  
**Kind**: method  
**Required**: Yes

Tells the app delegate that the app disconnected from the CarPlay interface.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func application(_ application: UIApplication, didDisconnectCarInterfaceController interfaceController: CPInterfaceController, from window: CPWindow)
```

## Parameters

- `application`: Your singleton app object.
- `interfaceController`: The interface controller provided by CarPlay. Your app should release its reference to this controller.
- `window`: The CarPlay window.

## See Also

- [func application(UIApplication, didConnectCarInterfaceController: CPInterfaceController, to: CPWindow)](cpapplicationdelegate/application(_:didconnectcarinterfacecontroller:to:).md)
  Tells the app delegate that the app connected to the CarPlay interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate/application(_:diddisconnectcarinterfacecontroller:from:))*