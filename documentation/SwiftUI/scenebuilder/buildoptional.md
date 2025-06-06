# buildOptional(_:)

**Framework**: SwiftUI  
**Kind**: method

Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

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
static func buildOptional(_ scene: (any Scene & _LimitedAvailabilitySceneMarker)?) -> some Scene
```

#### Discussion

Conditional statements in a [`SceneBuilder`](scenebuilder.md) can contain an `if` statement but not an `else` statement, and the condition can only perform a compiler check for availability, like in the following code:

```swift
var body: some Scene {
    if #available(iOS 16, *) {
        WindowGroup {
            ContentView()
        }
    }
}
```

## See Also

- [static buildBlock(_:)](scenebuilder/buildblock(_:).md)
  Passes a single scene written as a child scene through unmodified.
- [static func buildExpression<Content>(Content) -> Content](scenebuilder/buildexpression(_:).md)
  Builds an expression within the builder.
- [static buildLimitedAvailability(_:)](scenebuilder/buildlimitedavailability(_:).md)
  Processes scene content for a conditional compiler-control statement that performs an availability check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenebuilder/buildoptional(_:))*