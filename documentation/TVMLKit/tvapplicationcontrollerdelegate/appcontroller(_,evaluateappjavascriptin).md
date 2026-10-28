# appController(_:evaluateAppJavaScriptIn:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to add JavaScript classes and objects.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func appController(_ appController: TVApplicationController, evaluateAppJavaScriptIn jsContext: JSContext)
```

```objc
- (void) appController:(TVApplicationController *) appController evaluateAppJavaScriptInContext:(JSContext *) jsContext;
```

## Discussion

This method serves as a callback function, giving the delegate the ability to add JavaScript classes and objects through the [`setObject(_:forKey:)`](../../Foundation/nsmutabledictionary/setobject%28_,forkey%29.md) method using the `jsContext` parameter. This method is called before the JavaScript is parsed into the execution context and is called on the JavaScript execution thread, not the main thread. Any object exposed to [`JSContext`](../../JavaScriptCore/jscontext.md) must not be retained on any other thread.

## Parameters

- `appController`: The [`TVApplicationController`](../tvapplicationcontroller.md) object that is evaluating the JavaScript context.
- `jsContext`: The [`JSContext`](../../JavaScriptCore/jscontext.md) object being evaluated.

## See Also

### Managing the App Controller
- [func appController(TVApplicationController, didFail: any Error)](./appcontroller%28_,didfail%29.md)
  Tell the delegate the app controller failed due to an error.
- [func appController(TVApplicationController, didFinishLaunching: [String : Any]?)](./appcontroller%28_,didfinishlaunching%29.md)
  Tells the delegate the app controller has finished launching.
- [func appController(TVApplicationController, didStop: [String : Any]?)](./appcontroller%28_,didstop%29.md)
  Tells the delegate the app has stopped for any reason.
- [func player(for: TVApplicationController) -> TVPlayer?](./player%28for%29.md)
  Asks the delegate for a custom player object for a particular player bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/appcontroller(_:evaluateappjavascriptin:))*