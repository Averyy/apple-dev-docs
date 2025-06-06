# updatePredicate(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Replaces the predicate used to evaluate execution of the scene associated with the event trigger.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+

## Declaration

```swift
func updatePredicate(_ predicate: NSPredicate?) async throws
```

## Parameters

- `predicate`: The new predicate to use with the event trigger.
- `completion`: The block takes the following parameter:

## See Also

- [var predicate: NSPredicate?](hmeventtrigger/predicate.md)
  The predicate to evaluate before executing the scene associated with the event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/updatepredicate(_:completionhandler:))*