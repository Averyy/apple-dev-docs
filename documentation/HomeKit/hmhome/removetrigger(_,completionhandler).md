# removeTrigger(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes a trigger from the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeTrigger(_ trigger: HMTrigger, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeTrigger(_ trigger: HMTrigger) async throws
```

```objc
- (void) removeTrigger:(HMTrigger *) trigger completionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

If `trigger` is enabled, removing it from the home disables it.

## Parameters

- `trigger`: The trigger to remove.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Triggering an action set
- [var triggers: [HMTrigger]](./triggers.md)
  An array of triggers defined in the home.
- [func addTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](./addtrigger%28_,completionhandler%29.md)
  Adds a trigger to the home.
- [class HMTimerTrigger](../hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.
- [class HMEventTrigger](../hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.
- [class HMTrigger](../hmtrigger.md)
  An abstract base class for triggering actions based on a set of conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removetrigger(_:completionhandler:))*