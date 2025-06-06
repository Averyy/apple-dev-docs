# appController(_:didStop:)

**Framework**: TVMLKit  
**Kind**: method

Tells the delegate the app has stopped for any reason.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func appController(_ appController: TVApplicationController, didStop options: [String : Any]?)
```

## Parameters

- `appController`: The   object that has stopped.
- `options`: The launch options passed to the app controller.

## See Also

- [func appController(TVApplicationController, didFail: any Error)](tvapplicationcontrollerdelegate/appcontroller(_:didfail:).md)
  Tell the delegate the app controller failed due to an error.
- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](tvapplicationcontrollerdelegate/appcontroller(_:didfinishlaunching:).md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, evaluateAppJavaScriptIn: JSContext)](tvapplicationcontrollerdelegate/appcontroller(_:evaluateappjavascriptin:).md)
  Tells the delegate to add JavaScript classes and objects.
- [func player(for: TVApplicationController) -> TVPlayer?](tvapplicationcontrollerdelegate/player(for:).md)
  Asks the delegate for a custom player object for a particular player bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/appcontroller(_:didstop:))*