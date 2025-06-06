# execute(withAppleEvent:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Execute the AppleScript script by sending it the specified Apple event.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func execute(withAppleEvent event: NSAppleEventDescriptor?) async throws -> NSAppleEventDescriptor
```

#### Discussion

Pass `nil` as `event` to execute the script’s default “run” handler.

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## Parameters

- `event`: The Apple event.
- `handler`: The completion handler Block that returns the result or an error. See  .

## See Also

- [init(url: URL) throws](nsuserscripttask/init(url:).md)
  Return a user script task instance given a URL for a script file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserapplescripttask/execute(withappleevent:completionhandler:))*