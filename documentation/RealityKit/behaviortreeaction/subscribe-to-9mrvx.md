# subscribe(to:_:)

**Framework**: RealityKit  
**Kind**: method

Subscribes to a serializable action event and returns a `ActionResult`.

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
@preconcurrency static func subscribe(to eventType: ActionEventType, _ handler: @escaping @MainActor (ActionEvent<Self>) -> ActionResult)
```

#### Discussion

For example, you can call this method to subscribe to the update event, which the system calls each frame it evaluates the action:

```swift
struct MyAction: BehaviorTreeAction, Codable {
    ...
}
MyAction.subscribe(to: .updated) { event in
    // Return value is the action result.
    return .success
}
```

## See Also

- [static func subscribe(to: ActionEventType, (ActionEvent<Self>) -> Void)](behaviortreeaction/subscribe(to:_:)-3p0pj.md)
  Shadows the `EntityAction.subscribe(to:_:)` overload that takes a `-> Void` closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeaction/subscribe(to:_:)-9mrvx)*