# updateTriggerValue(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Changes the trigger value associated with this event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func updateTriggerValue(_ triggerValue: TriggerValueType?) async throws
```

#### Discussion

Set the trigger value to `nil` to trigger the event whenever the value of the characteristic changes.

## Parameters

- `triggerValue`: The value of the characteristic that triggers the event.
- `completion`: The block executed once the trigger value update request has been processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/updatetriggervalue(_:completionhandler:))*