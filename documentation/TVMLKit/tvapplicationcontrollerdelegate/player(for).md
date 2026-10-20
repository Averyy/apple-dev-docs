# player(for:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for a custom player object for a particular player bridge.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func player(for appController: TVApplicationController) -> TVPlayer?
```

```objc
- (TVPlayer *) playerForAppController:(TVApplicationController *) appController;
```

#### Return Value

A customizable [`TVPlayer`](../tvplayer.md) object.

## Parameters

- `appController`: The [`TVApplicationController`](../tvapplicationcontroller.md) object that contains the player object.

## See Also

### Managing the App Controller
- [func appController(TVApplicationController, didFail: any Error)](./appcontroller%28_,didfail%29.md)
  Tell the delegate the app controller failed due to an error.
- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](./appcontroller%28_,didfinishlaunching%29.md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, didStop: [String : Any]?)](./appcontroller%28_,didstop%29.md)
  Tells the delegate the app has stopped for any reason.
- [func appController(TVApplicationController, evaluateAppJavaScriptIn: JSContext)](./appcontroller%28_,evaluateappjavascriptin%29.md)
  Tells the delegate to add JavaScript classes and objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/player(for:))*