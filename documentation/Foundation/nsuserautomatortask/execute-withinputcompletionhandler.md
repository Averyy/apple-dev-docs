# execute(withInput:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Execute the Automator workflow by providing it as securely coded input.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func execute(withInput input: (any NSSecureCoding)?) async throws -> Any
```

#### Discussion

The Automator workflow will execute using the [`variables`](nsuserautomatortask/variables.md) property values.

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## Parameters

- `input`: The automator task.
- `handler`: The completion handler Block that returns the result or an error. See  .

## See Also

- [init(url: URL) throws](nsuserscripttask/init(url:).md)
  Return a user script task instance given a URL for a script file.
- [var variables: [String : Any]?](nsuserautomatortask/variables.md)
  The variables required by the Automator workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserautomatortask/execute(withinput:completionhandler:))*