# NSUserAutomatorTask.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

Implement this block to retrieve the output of the Automator workflow executed by [`execute(withInput:completionHandler:)`](./execute%28withinput,completionhandler%29.md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CompletionHandler = @Sendable (Any?, (any Error)?) -> Void
```

```c
typedef void (^)(id, NSError *) NSUserAutomatorTaskCompletionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserautomatortask/completionhandler)*