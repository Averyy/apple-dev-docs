# player(for:)

**Framework**: TVMLKit  
**Kind**: method

Asks the delegate for a custom player object for a particular player bridge.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
optional func player(for appController: TVApplicationController) -> TVPlayer?
```

#### Return Value

A customizable [`TVPlayer`](tvplayer.md) object.

## Parameters

- `appController`: The   object that contains the player object.

## See Also

- [func appController(TVApplicationController, didFail: any Error)](tvapplicationcontrollerdelegate/appcontroller(_:didfail:).md)
  Tell the delegate the app controller failed due to an error.
- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](tvapplicationcontrollerdelegate/appcontroller(_:didfinishlaunching:).md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, didStop: [String : Any]?)](tvapplicationcontrollerdelegate/appcontroller(_:didstop:).md)
  Tells the delegate the app has stopped for any reason.
- [func appController(TVApplicationController, evaluateAppJavaScriptIn: JSContext)](tvapplicationcontrollerdelegate/appcontroller(_:evaluateappjavascriptin:).md)
  Tells the delegate to add JavaScript classes and objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/player(for:))*