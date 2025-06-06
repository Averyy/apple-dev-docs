# NSUserScriptTask.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias

Implement this block to retrieve the error of the script executed by [`execute(completionHandler:)`](nsuserscripttask/execute(completionhandler:).md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CompletionHandler = ((any Error)?) -> Void
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserscripttask/completionhandler)*