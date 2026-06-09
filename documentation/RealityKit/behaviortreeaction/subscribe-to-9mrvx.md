# subscribe(to:_:)

**Framework**: RealityKit  
**Kind**: method

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

## See Also

- [static func subscribe(to: ActionEventType, (ActionEvent<Self>) -> Void)](behaviortreeaction/subscribe(to:_:)-3p0pj.md)
  Shadows the `EntityAction.subscribe(to:_:)` overload that takes a `-> Void` closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeaction/subscribe(to:_:)-9mrvx)*