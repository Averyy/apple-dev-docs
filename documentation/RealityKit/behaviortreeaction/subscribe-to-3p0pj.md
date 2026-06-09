# subscribe(to:_:)

**Framework**: RealityKit  
**Kind**: method

Shadows the `EntityAction.subscribe(to:_:)` overload that takes a `-> Void` closure.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency static func subscribe(to eventType: ActionEventType, _ handler: @escaping @MainActor (ActionEvent<Self>) -> Void)
```

#### Discussion

When the handler doesn’t return a value, the action status is preserved: the value already in `actionStatusPointer` at the time the handler is called is read and written back, leaving the behavior tree’s status unchanged.

## See Also

- [static func subscribe(to: ActionEventType, (ActionEvent<Self>) -> ActionResult)](behaviortreeaction/subscribe(to:_:)-9mrvx.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeaction/subscribe(to:_:)-3p0pj)*