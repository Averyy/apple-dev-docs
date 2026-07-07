# modelContext(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the model context in this view’s environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func modelContext(_ modelContext: ModelContext) -> some View
```

#### Discussion

In this example, the `RecipesList` view sets a model context to use for all of its content:

```swift
@Model class Recipe { ... }
...
RecipesList()
    .modelContext(myContext)
```

The environment’s [`modelContext`](environmentvalues/modelcontext.md) property will be assigned `myContext`. All implicit model context operations in this view, such as `Query` properties, will use the environment’s context.

## Parameters

- `modelContext`: The model context to set in this view’s environment.

## See Also

- [func modelContainer(ModelContainer) -> some View](view/modelcontainer(_:).md)
  Sets the model container and associated model context in this view’s environment.
- [func modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](view/modelcontainer(for:inmemory:isautosaveenabled:isundoenabled:onsetup:).md)
  Sets the model container in this view for storing the provided model type, creating a new container if necessary, and also sets a model context for that container in this view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/modelcontext(_:))*