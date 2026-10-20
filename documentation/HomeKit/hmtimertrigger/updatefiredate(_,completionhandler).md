# updateFireDate(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the next fire date for the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateFireDate(_ fireDate: Date, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateFireDate(_ fireDate: Date) async throws
```

```objc
- (void) updateFireDate:(NSDate *) fireDate completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `fireDate`: The new fire date.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Choosing the fire date
- [var fireDate: Date](./firedate.md)
  The time at which the trigger will next fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/updatefiredate(_:completionhandler:))*