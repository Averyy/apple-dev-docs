# invalidate()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Prevents the background activity from being scheduled again.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func invalidate()
```

```objc
- (void) invalidate;
```

## Discussion

When `invalidate` is used to stop an activity that is currently executing, the activity will still finish executing.

See [Stop Activity](../nsbackgroundactivityscheduler.md#Stop-Activity).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/invalidate())*