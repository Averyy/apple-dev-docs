# NSUserUnixTask.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias

Implement this block to retrieve an error from the Unix scripted executed by [`execute(withArguments:completionHandler:)`](nsuserunixtask/execute(witharguments:completionhandler:).md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CompletionHandler = ((any Error)?) -> Void
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask/completionhandler)*