# execute(completionHandler:)

**Framework**: Foundation  
**Kind**: method

Executes the script with no input and ignoring any result.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func execute() async throws
```

#### Discussion

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## Parameters

- `handler`: The completion handler Block that returns the result or an error. See  .

## See Also

- [init(url: URL) throws](nsuserscripttask/init(url:).md)
  Return a user script task instance given a URL for a script file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserscripttask/execute(completionhandler:))*