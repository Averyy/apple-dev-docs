# appController(_:didFail:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Tell the delegate the app controller failed due to an error.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func appController(_ appController: TVApplicationController, didFail error: any Error)
```

```objc
- (void) appController:(TVApplicationController *) appController didFailWithError:(NSError *) error;
```

## Parameters

- `appController`: The [`TVApplicationController`](../tvapplicationcontroller.md) object that has failed.
- `error`: An [`NSError`](../../Foundation/nserror.md) object describing why the app controller failed.

## See Also

### Managing the App Controller
- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](./appcontroller%28_,didfinishlaunching%29.md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, didStop: [String : Any]?)](./appcontroller%28_,didstop%29.md)
  Tells the delegate the app has stopped for any reason.
- [func appController(TVApplicationController, evaluateAppJavaScriptIn: JSContext)](./appcontroller%28_,evaluateappjavascriptin%29.md)
  Tells the delegate to add JavaScript classes and objects.
- [func player(for: TVApplicationController) -> TVPlayer?](./player%28for%29.md)
  Asks the delegate for a custom player object for a particular player bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/appcontroller(_:didfail:))*