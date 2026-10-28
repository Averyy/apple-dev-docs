# updateTriggerValue(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Changes the trigger value associated with this event.

**Availability**:
- iOS 9.0+ - Deprecated in 11.0
- iPadOS 9.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the mutable region property on the [`HMMutableLocationEvent`](../hmmutablelocationevent.md) subclass of [`HMLocationEvent`](../hmlocationevent.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func updateTriggerValue(_ triggerValue: TriggerValueType?, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

*Mac Catalyst, visionOS*

```swift
func updateTriggerValue(_ triggerValue: TriggerValueType?) async throws
```

```objc
- (void) updateTriggerValue:(TriggerValueType) triggerValue completionHandler:(void (^)(NSError *error)) completion;
```

## Discussion

Set the trigger value to `nil` to trigger the event whenever the value of the characteristic changes.

## Parameters

- `triggerValue`: The value of the characteristic that triggers the event.
- `completion`: The block executed once the trigger value update request has been processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/updatetriggervalue(_:completionhandler:))*