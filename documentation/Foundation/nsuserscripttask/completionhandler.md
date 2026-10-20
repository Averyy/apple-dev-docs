# NSUserScriptTask.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

Implement this block to retrieve the error of the script executed by [`execute(completionHandler:)`](./execute%28completionhandler%29.md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CompletionHandler = @Sendable ((any Error)?) -> Void
```

```c
typedef void (^)(NSError *) NSUserScriptTaskCompletionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserscripttask/completionhandler)*