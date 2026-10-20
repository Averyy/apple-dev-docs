# removeEvent(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified event from the event trigger.

**Availability**:
- iOS 9.0+ - Deprecated in 11.0
- iPadOS 9.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`updateEvents(_:completionHandler:)`](./updateevents%28_,completionhandler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func removeEvent(_ event: HMEvent, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

*Mac Catalyst, visionOS*

```swift
func removeEvent(_ event: HMEvent) async throws
```

```objc
- (void) removeEvent:(HMEvent *) event completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `event`: The event to remove from the event trigger.
- `completion`: A block that executes after processing the request.

  The block takes the following parameter:

  - **error**: If the request was successful, the value of `error` is `nil`; otherwise, the value provides more information about the request status.

## See Also

### Deprecated symbols
- [func addEvent(HMEvent, completionHandler: ((any Error)?) -> Void)](./addevent%28_,completionhandler%29.md)
  Adds a new event to the event trigger.
- [class func predicateForEvaluatingTrigger(occurringBefore: String, applyingOffset: DateComponents?) -> NSPredicate](./predicateforevaluatingtrigger%28occurringbefore,applyingoffset%29.md)
  Creates a predicate that evaluates whether the event occurred before a significant event.
- [class func predicateForEvaluatingTrigger(occurringAfter: String, applyingOffset: DateComponents?) -> NSPredicate](./predicateforevaluatingtrigger%28occurringafter,applyingoffset%29.md)
  Creates a predicate that evaluates whether the event occurred before a significant event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/removeevent(_:completionhandler:))*