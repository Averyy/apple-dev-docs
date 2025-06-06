# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method

Processes scene content for a conditional compiler-control statement that performs an availability check.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
static func buildLimitedAvailability(_ scene: some Scene) -> any Scene & _LimitedAvailabilitySceneMarker
```

## See Also

- [static buildBlock(_:)](scenebuilder/buildblock(_:).md)
  Passes a single scene written as a child scene through unmodified.
- [static func buildExpression<Content>(Content) -> Content](scenebuilder/buildexpression(_:).md)
  Builds an expression within the builder.
- [static func buildOptional((any Scene & _LimitedAvailabilitySceneMarker)?) -> some Scene](scenebuilder/buildoptional(_:).md)
  Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenebuilder/buildlimitedavailability(_:))*