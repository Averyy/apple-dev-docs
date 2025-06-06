# NSUserAutomatorTask.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias

Implement this block to retrieve the output of the Automator workflow executed by [`execute(withInput:completionHandler:)`](nsuserautomatortask/execute(withinput:completionhandler:).md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CompletionHandler = (Any?, (any Error)?) -> Void
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserautomatortask/completionhandler)*