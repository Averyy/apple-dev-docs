# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> some Scene where repeat each Content : Scene
```

## See Also

- [static func buildExpression<Content>(Content) -> Content](scenebuilder/buildexpression(_:).md)
  Builds an expression within the builder.
- [static func buildLimitedAvailability(some Scene) -> any Scene & _LimitedAvailabilitySceneMarker](scenebuilder/buildlimitedavailability(_:).md)
  Processes scene content for a conditional compiler-control statement that performs an availability check.
- [static func buildOptional((any Scene & _LimitedAvailabilitySceneMarker)?) -> some Scene](scenebuilder/buildoptional(_:).md)
  Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenebuilder/buildblock(_:))*