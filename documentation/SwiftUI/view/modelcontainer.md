# modelContainer(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the model container and associated model context in this view’s environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func modelContainer(_ container: ModelContainer) -> some View
```

#### Discussion

In this example, `ContentView` sets a model container to use for `RecipesList`:

```swift
struct ContentView: View {
    @State private var container = ModelContainer(...)

    var body: some Scene {
        RecipesList()
            .modelContainer(container)
    }
}
```

The environment’s [`modelContext`](environmentvalues/modelcontext.md) property will be assigned a new context associated with this container. All implicit model context operations in this view, such as `Query` properties, will use the environment’s context.

## Parameters

- `container`: The model container to use for this view.

## See Also

- [func modelContext(ModelContext) -> some View](view/modelcontext(_:).md)
  Sets the model context in this view’s environment.
- [func modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](view/modelcontainer(for:inmemory:isautosaveenabled:isundoenabled:onsetup:).md)
  Sets the model container in this view for storing the provided model type, creating a new container if necessary, and also sets a model context for that container in this view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/modelcontainer(_:))*