# wait()

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Waits synchronously for the previously submitted work to finish.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func wait()
```

## See Also

### Waiting for Tasks to Finish Executing
- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](./wait%28timeout%29.md)
  Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](./wait%28walltimeout%29.md)
  Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup/wait())*