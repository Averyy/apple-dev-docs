# TVApplicationControllerDelegate

**Framework**: TVMLKit  
**Kind**: protocol  
**Role**: Protocol

A protocol used to observe and manage the different states of an application controller.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
protocol TVApplicationControllerDelegate : NSObjectProtocol
```

```objc
@protocol TVApplicationControllerDelegate <NSObject>
```

## Topics

### Managing the App Controller
- [func appController(TVApplicationController, didFail: any Error)](./tvapplicationcontrollerdelegate/appcontroller%28_,didfail%29.md)
  Tell the delegate the app controller failed due to an error.
- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](./tvapplicationcontrollerdelegate/appcontroller%28_,didfinishlaunching%29.md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, didStop: [String : Any]?)](./tvapplicationcontrollerdelegate/appcontroller%28_,didstop%29.md)
  Tells the delegate the app has stopped for any reason.
- [func appController(TVApplicationController, evaluateAppJavaScriptIn: JSContext)](./tvapplicationcontrollerdelegate/appcontroller%28_,evaluateappjavascriptin%29.md)
  Tells the delegate to add JavaScript classes and objects.
- [func player(for: TVApplicationController) -> TVPlayer?](./tvapplicationcontrollerdelegate/player%28for%29.md)
  Asks the delegate for a custom player object for a particular player bridge.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Getting the Delegate
- [var delegate: (any TVApplicationControllerDelegate)?](./tvapplicationcontroller/delegate.md)
  The delegate of the app controller object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate)*