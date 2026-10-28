# modelContainer(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the model container and associated model context in this scene’s environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func modelContainer(_ container: ModelContainer) -> some Scene
```

## Discussion

In this example, `RecipesApp` sets a shared model container to use for all of its windows:

```swift
@main
struct RecipesApp: App {
    @State private var container = ModelContainer(...)

    var body: some Scene {
        WindowGroup {
            RecipesList()
        }
        .modelContainer(container)
    }
}
```

The environment’s [`modelContext`](../environmentvalues/modelcontext.md) property will be assigned a new context associated with this container. All implicit model context operations in this scene, such as `Query` properties, will use the environment’s context.

## Parameters

- `container`: The model container to use for this scene.

## See Also

### Configuring a data model
- [func modelContext(ModelContext) -> some Scene](./modelcontext%28_%29.md)
  Sets the model context in this scene’s environment.
- [func modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](./modelcontainer%28for,inmemory,isautosaveenabled,isundoenabled,onsetup%29.md)
  Sets the model container in this scene for storing the provided model type, creating a new container if necessary, and also sets a model context for that container in this scene’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/modelcontainer(_:))*