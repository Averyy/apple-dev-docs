# TVApplicationControllerDelegate

**Framework**: TVMLKit  
**Kind**: protocol

A protocol used to observe and manage the different states of an application controller.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
protocol TVApplicationControllerDelegate : NSObjectProtocol
```

## Topics

### Managing the App Controller
- [func appController(TVApplicationController, didFail: any Error)](tvapplicationcontrollerdelegate/appcontroller(_:didfail:).md)
  Tell the delegate the app controller failed due to an error.
- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](tvapplicationcontrollerdelegate/appcontroller(_:didfinishlaunching:).md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, didStop: [String : Any]?)](tvapplicationcontrollerdelegate/appcontroller(_:didstop:).md)
  Tells the delegate the app has stopped for any reason.
- [func appController(TVApplicationController, evaluateAppJavaScriptIn: JSContext)](tvapplicationcontrollerdelegate/appcontroller(_:evaluateappjavascriptin:).md)
  Tells the delegate to add JavaScript classes and objects.
- [func player(for: TVApplicationController) -> TVPlayer?](tvapplicationcontrollerdelegate/player(for:).md)
  Asks the delegate for a custom player object for a particular player bridge.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any TVApplicationControllerDelegate)?](tvapplicationcontroller/delegate.md)
  The delegate of the app controller object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate)*