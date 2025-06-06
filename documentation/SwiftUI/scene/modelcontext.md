# modelContext(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the model context in this scene’s environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func modelContext(_ modelContext: ModelContext) -> some Scene
```

#### Discussion

In this example, `RecipesApp` sets a shared model context to use for all of its windows:

```swift
@Model class Recipe { ... }

@main
struct RecipesApp: App {
    var body: some Scene {
        WindowGroup {
            RecipesList()
        }
        .modelContext(myContext)
    }
}
```

The environment’s [`modelContext`](environmentvalues/modelcontext.md) property will be assigned a `myContext`. All implicit model context operations in this scene, such as `Query` properties, will use the environment’s context.

## Parameters

- `modelContext`: The model context to set in this scene’s environment.

## See Also

- [func modelContainer(ModelContainer) -> some Scene](scene/modelcontainer(_:).md)
  Sets the model container and associated model context in this scene’s environment.
- [func modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](scene/modelcontainer(for:inmemory:isautosaveenabled:isundoenabled:onsetup:).md)
  Sets the model container in this scene for storing the provided model type, creating a new container if necessary, and also sets a model context for that container in this scene’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/modelcontext(_:))*