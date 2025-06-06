# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method

Builds an expression within the builder.

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
static func buildExpression<Content>(_ content: Content) -> Content where Content : Scene
```

## See Also

- [static buildBlock(_:)](scenebuilder/buildblock(_:).md)
  Passes a single scene written as a child scene through unmodified.
- [static buildLimitedAvailability(_:)](scenebuilder/buildlimitedavailability(_:).md)
  Processes scene content for a conditional compiler-control statement that performs an availability check.
- [static func buildOptional((any Scene & _LimitedAvailabilitySceneMarker)?) -> some Scene](scenebuilder/buildoptional(_:).md)
  Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenebuilder/buildexpression(_:))*