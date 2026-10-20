# stop()

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Ends the app life cycle.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
func stop()
```

```objc
- (void) stop;
```

#### Discussion

After the JavaScript context has ended and all resources have been released, [`appController(_:didStop:)`](../tvapplicationcontrollerdelegate/appcontroller%28_,didstop%29.md) is called. The app controller cannot be reused after the `stop` method has been called.

## See Also

### Controlling and Handling Events
- [func evaluate(inJavaScriptContext: (JSContext) -> Void, completion: ((Bool) -> Void)?)](./evaluate%28injavascriptcontext,completion%29.md)
  Evaluates a block in the JavaScript execution queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/stop())*