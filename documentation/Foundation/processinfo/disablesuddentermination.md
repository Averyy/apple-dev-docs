# disableSuddenTermination()

**Framework**: Foundation  
**Kind**: method

Disables the application for quickly killing using sudden termination.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func disableSuddenTermination()
```

#### Discussion

This method increments the sudden termination counter. When the termination counter reaches `0` the application allows sudden termination.

By default the sudden termination counter is set to 1. This can be overridden in your application Info.plist. See [`Support Sudden Termination`](processinfo#Support-Sudden-Termination.md) for more information and debugging suggestions.

## See Also

- [func enableSuddenTermination()](processinfo/enablesuddentermination.md)
  Enables the application for quick killing using sudden termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/disablesuddentermination())*