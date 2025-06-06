# stop()

**Framework**: TVMLKit  
**Kind**: method

Ends the app life cycle.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
func stop()
```

#### Discussion

After the JavaScript context has ended and all resources have been released, [`appController(_:didStop:)`](tvapplicationcontrollerdelegate/appcontroller(_:didstop:).md) is called. The app controller cannot be reused after the `stop` method has been called.

## See Also

- [func evaluate(inJavaScriptContext: (JSContext) -> Void, completion: ((Bool) -> Void)?)](tvapplicationcontroller/evaluate(injavascriptcontext:completion:).md)
  Evaluates a block in the JavaScript execution queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/stop())*