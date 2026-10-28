# disableSuddenTermination()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Disables the application for quickly killing using sudden termination.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func disableSuddenTermination()
```

```objc
- (void) disableSuddenTermination;
```

## Discussion

This method increments the sudden termination counter. When the termination counter reaches `0` the application allows sudden termination.

By default the sudden termination counter is set to 1. This can be overridden in your application Info.plist. See [Support Sudden Termination](../processinfo.md#Support-Sudden-Termination) for more information and debugging suggestions.

## See Also

### Working with sudden application termination
- [func enableSuddenTermination()](./enablesuddentermination%28%29.md)
  Enables the application for quick killing using sudden termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/disablesuddentermination())*