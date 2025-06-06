# appController(_:didFail:)

**Framework**: TVMLKit  
**Kind**: method

Tell the delegate the app controller failed due to an error.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func appController(_ appController: TVApplicationController, didFail error: any Error)
```

## Parameters

- `appController`: The   object that has failed.
- `error`: An   object describing why the app controller failed.

## See Also

- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](tvapplicationcontrollerdelegate/appcontroller(_:didfinishlaunching:).md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, didStop: [String : Any]?)](tvapplicationcontrollerdelegate/appcontroller(_:didstop:).md)
  Tells the delegate the app has stopped for any reason.
- [func appController(TVApplicationController, evaluateAppJavaScriptIn: JSContext)](tvapplicationcontrollerdelegate/appcontroller(_:evaluateappjavascriptin:).md)
  Tells the delegate to add JavaScript classes and objects.
- [func player(for: TVApplicationController) -> TVPlayer?](tvapplicationcontrollerdelegate/player(for:).md)
  Asks the delegate for a custom player object for a particular player bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/appcontroller(_:didfail:))*