# modelContext

**Framework**: SwiftData  
**Kind**: property

Current model context `Query` interacts with.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency var modelContext: ModelContext { get }
```

#### Discussion

Access this value from `Query` property wrapper’s stored property:

```swift
struct RecipeList: View {
    @Query var recipes: [Recipe]
    var body: some View {
        ChangesIndicator(
            hasChanges: _recipes.modelContext.hasChanges)
    }
}
```

Only access this property within of a view’s `body` property, otherwise its value may be invalid.

## See Also

- [var fetchError: (any Error)?](query/fetcherror.md)
  An error encountered during the most recent attempt to fetch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/modelcontext)*