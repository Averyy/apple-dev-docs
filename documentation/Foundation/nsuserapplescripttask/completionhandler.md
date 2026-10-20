# NSUserAppleScriptTask.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

Implement this block to retrieve the result of the AppleScript executed by [`execute(withAppleEvent:completionHandler:)`](./execute%28withappleevent,completionhandler%29.md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CompletionHandler = @Sendable (NSAppleEventDescriptor?, (any Error)?) -> Void
```

```c
typedef void (^)(NSAppleEventDescriptor *, NSError *) NSUserAppleScriptTaskCompletionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserapplescripttask/completionhandler)*