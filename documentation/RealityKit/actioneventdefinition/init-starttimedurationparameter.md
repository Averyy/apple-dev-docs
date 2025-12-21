# init(startTime:duration:parameter:)

**Framework**: RealityKit  
**Kind**: init

Constructs an event definition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(startTime: TimeInterval, duration: TimeInterval, parameter: ActionEventDefinition<ActionType>.EventParameterType? = nil)
```

## Parameters

- `startTime`: The time when the event becomes active.
- `duration`: The duration of the event.
- `parameter`: The event parameter to return to the event handler when the event occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actioneventdefinition/init(starttime:duration:parameter:))*