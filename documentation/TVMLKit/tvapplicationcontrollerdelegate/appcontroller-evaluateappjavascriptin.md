# appController(_:evaluateAppJavaScriptIn:)

**Framework**: TVMLKit  
**Kind**: method

Tells the delegate to add JavaScript classes and objects.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func appController(_ appController: TVApplicationController, evaluateAppJavaScriptIn jsContext: JSContext)
```

#### Discussion

This method serves as a callback function, giving the delegate the ability to add JavaScript classes and objects through the  [`setObject:forKeyedSubscript:`](https://developer.apple.com/documentation/Foundation/NSMutableDictionary/setObject:forKeyedSubscript:) method using the `jsContext` parameter. This method is called before the JavaScript is parsed into the execution context and is called on the JavaScript execution thread, not the main thread. Any object exposed to [`JSContext`](https://developer.apple.com/documentation/JavaScriptCore/JSContext) must not be retained on any other thread.

## Parameters

- `appController`: The   object that is evaluating the JavaScript context.
- `jsContext`: The   object being evaluated.

## See Also

- [func appController(TVApplicationController, didFail: any Error)](tvapplicationcontrollerdelegate/appcontroller(_:didfail:).md)
  Tell the delegate the app controller failed due to an error.
- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](tvapplicationcontrollerdelegate/appcontroller(_:didfinishlaunching:).md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, didStop: [String : Any]?)](tvapplicationcontrollerdelegate/appcontroller(_:didstop:).md)
  Tells the delegate the app has stopped for any reason.
- [func player(for: TVApplicationController) -> TVPlayer?](tvapplicationcontrollerdelegate/player(for:).md)
  Asks the delegate for a custom player object for a particular player bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/appcontroller(_:evaluateappjavascriptin:))*