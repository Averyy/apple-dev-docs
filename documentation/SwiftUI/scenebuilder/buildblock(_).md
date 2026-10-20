# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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

**Other overloads**:

```swift
static func buildBlock<Content>(_ content: Content) -> Content where Content : Scene
```

## See Also

### Building content
- [static func buildExpression<Content>(Content) -> Content](./buildexpression%28_%29.md)
  Builds an expression within the builder.
- [static func buildLimitedAvailability(some Scene) -> any Scene & _LimitedAvailabilitySceneMarker](./buildlimitedavailability%28_%29.md)
  Processes scene content for a conditional compiler-control statement that performs an availability check.
- [static func buildOptional((any Scene & _LimitedAvailabilitySceneMarker)?) -> some Scene](./buildoptional%28_%29.md)
  Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenebuilder/buildblock(_:))*