# execute(withInput:completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Execute the Automator workflow by providing it as securely coded input.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func execute(withInput input: (any NSSecureCoding)?, completionHandler handler: NSUserAutomatorTask.CompletionHandler? = nil)
```

```swift
func execute(withInput input: (any NSSecureCoding)?) async throws -> Any
```

```objc
- (void) executeWithInput:(id<NSSecureCoding>) input completionHandler:(NSUserAutomatorTaskCompletionHandler) handler;
```

#### Discussion

The Automator workflow will execute using the [`variables`](./variables.md) property values.

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## Parameters

- `input`: The automator task.
- `handler`: The completion handler Block that returns the result or an error. See [`NSUserAutomatorTask.CompletionHandler`](./completionhandler.md).

## See Also

### Related Documentation
- [init(url: URL) throws](../nsuserscripttask/init%28url%29-2qgls.md)
  Return a user script task instance given a URL for a script file.
### Executing Automator Tasks
- [var variables: [String : Any]?](./variables.md)
  The variables required by the Automator workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserautomatortask/execute(withinput:completionhandler:))*