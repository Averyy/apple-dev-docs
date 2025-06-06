# updateRecurrence(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the recurrence interval.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateRecurrence(_ recurrence: DateComponents?) async throws
```

#### Discussion

See [`recurrence`](hmtimertrigger/recurrence.md) for a discussion of how the recurrence value is used.

## Parameters

- `recurrence`: The new recurrence interval.
- `completion`: The block executed after the request is processed.

## See Also

- [var recurrence: DateComponents?](hmtimertrigger/recurrence.md)
  The interval on which to repeat firing the trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/updaterecurrence(_:completionhandler:))*