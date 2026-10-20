# execute(completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Executes the script with no input and ignoring any result.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func execute(completionHandler handler: NSUserScriptTask.CompletionHandler? = nil)
```

```swift
func execute() async throws
```

```objc
- (void) executeWithCompletionHandler:(NSUserScriptTaskCompletionHandler) handler;
```

#### Discussion

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## Parameters

- `handler`: The completion handler Block that returns the result or an error. See [`NSUserScriptTask.CompletionHandler`](./completionhandler.md).

## See Also

### Related Documentation
- [init(url: URL) throws](./init%28url%29-2qgls.md)
  Return a user script task instance given a URL for a script file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserscripttask/execute(completionhandler:))*