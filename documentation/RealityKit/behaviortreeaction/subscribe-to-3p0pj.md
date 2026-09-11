# subscribe(to:_:)

**Framework**: RealityKit  
**Kind**: method

Shadows the `EntityAction.subscribe(to:_:)` overload that takes a `-> Void` closure.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency static func subscribe(to eventType: ActionEventType, _ handler: @escaping @MainActor (ActionEvent<Self>) -> Void)
```

#### Discussion

When the handler doesn’t return a value, the action status is preserved: the value already in `actionStatusPointer` at the time the handler is called is read and written back, leaving the behavior tree’s status unchanged.

## See Also

- [static func subscribe(to: ActionEventType, (ActionEvent<Self>) -> ActionResult)](behaviortreeaction/subscribe(to:_:)-9mrvx.md)
  Subscribes to a serializable action event and returns a `ActionResult`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeaction/subscribe(to:_:)-3p0pj)*