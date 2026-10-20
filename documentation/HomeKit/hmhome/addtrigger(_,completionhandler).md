# addTrigger(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Adds a trigger to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addTrigger(_ trigger: HMTrigger, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func addTrigger(_ trigger: HMTrigger) async throws
```

```objc
- (void) addTrigger:(HMTrigger *) trigger completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `trigger`: The name of the new trigger. Must not be `nil`, and must not be the name of a trigger already in the home.
- `completion`: The block executed after the request is processed.

  - **trigger**: The newly created trigger.
  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Triggering an action set
- [var triggers: [HMTrigger]](./triggers.md)
  An array of triggers defined in the home.
- [func removeTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](./removetrigger%28_,completionhandler%29.md)
  Removes a trigger from the home.
- [class HMTimerTrigger](../hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.
- [class HMEventTrigger](../hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.
- [class HMTrigger](../hmtrigger.md)
  An abstract base class for triggering actions based on a set of conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addtrigger(_:completionhandler:))*