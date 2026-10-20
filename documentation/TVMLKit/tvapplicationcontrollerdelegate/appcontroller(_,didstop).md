# appController(_:didStop:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the app has stopped for any reason.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func appController(_ appController: TVApplicationController, didStop options: [String : Any]?)
```

```objc
- (void) appController:(TVApplicationController *) appController didStopWithOptions:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `appController`: The [`TVApplicationController`](../tvapplicationcontroller.md) object that has stopped.
- `options`: The launch options passed to the app controller.

## See Also

### Managing the App Controller
- [func appController(TVApplicationController, didFail: any Error)](./appcontroller%28_,didfail%29.md)
  Tell the delegate the app controller failed due to an error.
- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](./appcontroller%28_,didfinishlaunching%29.md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, evaluateAppJavaScriptIn: JSContext)](./appcontroller%28_,evaluateappjavascriptin%29.md)
  Tells the delegate to add JavaScript classes and objects.
- [func player(for: TVApplicationController) -> TVPlayer?](./player%28for%29.md)
  Asks the delegate for a custom player object for a particular player bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/appcontroller(_:didstop:))*