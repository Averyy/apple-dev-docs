# NSBackgroundActivityScheduler.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS 10.10+

## Declaration

```swift
typealias CompletionHandler = @Sendable (NSBackgroundActivityScheduler.Result) -> Void
```

```c
typedef void (^)(enum NSBackgroundActivityResult) NSBackgroundActivityCompletionHandler;
```

## See Also

### Scheduling Activity
- [func schedule((NSBackgroundActivityScheduler.CompletionHandler) -> Void)](./schedule%28_%29.md)
  Begins scheduling the background activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/completionhandler)*