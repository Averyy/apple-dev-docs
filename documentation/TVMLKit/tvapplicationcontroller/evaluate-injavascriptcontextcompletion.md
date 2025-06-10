# evaluate(inJavaScriptContext:completion:)

**Framework**: TVMLKit  
**Kind**: method

Evaluates a block in the JavaScript execution queue.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
func evaluate(inJavaScriptContext evaluation: @escaping (JSContext) -> Void) async -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func evaluate(inJavaScriptContext evaluation: @escaping (JSContext) -> Void) async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method adds a block to the JavaScript execution queue and invokes the completion block after the evaluation block has finished execution. The `context` block parameter is valid within the scope of the evaluation block and should not be referenced by the app outside the block.

## Parameters

- `evaluation`: The block to be evaluated in the JavaScript execution queue.
- `completion`: The callback after the block has been executed.   if the block was evaluated;   otherwise.

## See Also

- [func stop()](tvapplicationcontroller/stop.md)
  Ends the app life cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/evaluate(injavascriptcontext:completion:))*