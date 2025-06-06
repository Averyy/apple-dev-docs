# NSUserAppleScriptTask.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias

Implement this block to retrieve the result of the AppleScript executed by [`execute(withAppleEvent:completionHandler:)`](nsuserapplescripttask/execute(withappleevent:completionhandler:).md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CompletionHandler = (NSAppleEventDescriptor?, (any Error)?) -> Void
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserapplescripttask/completionhandler)*