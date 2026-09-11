# subscribe(to:_:)

**Framework**: RealityKit  
**Kind**: method

Subscribes to a serializable action event and returns a `ActionResult`.

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
@preconcurrency static func subscribe(to eventType: ActionEventType, _ handler: @escaping @MainActor (ActionEvent<Self>) -> ActionResult)
```

#### Discussion

For example, you can call this method to subscribe to the update event, which the system calls each frame it evaluates the action:

```swift
struct MyAction: BehaviorTreeAction, Codable {
    // ...
}
MyAction.subscribe(to: .updated) { event in
    // Return value is the action result.
    return .success
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeaction/subscribe(to:_:))*