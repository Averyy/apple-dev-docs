# updateRecurrence(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the recurrence interval.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateRecurrence(_ recurrence: DateComponents?, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateRecurrence(_ recurrence: DateComponents?) async throws
```

```objc
- (void) updateRecurrence:(NSDateComponents *) recurrence completionHandler:(void (^)(NSError *error)) completion;
```

## Discussion

See [`recurrence`](./recurrence.md) for a discussion of how the recurrence value is used.

## Parameters

- `recurrence`: The new recurrence interval.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Using recurrence
- [var recurrence: DateComponents?](./recurrence.md)
  The interval on which to repeat firing the trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/updaterecurrence(_:completionhandler:))*