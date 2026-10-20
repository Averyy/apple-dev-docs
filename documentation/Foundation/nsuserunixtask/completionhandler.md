# NSUserUnixTask.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

Implement this block to retrieve an error from the Unix scripted executed by [`execute(withArguments:completionHandler:)`](./execute%28witharguments,completionhandler%29.md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CompletionHandler = @Sendable ((any Error)?) -> Void
```

```c
typedef void (^)(NSError *) NSUserUnixTaskCompletionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask/completionhandler)*