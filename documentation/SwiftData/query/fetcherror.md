# fetchError

**Framework**: SwiftData  
**Kind**: property

An error encountered during the most recent attempt to fetch data.

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
@preconcurrency var fetchError: (any Error)? { get }
```

#### Discussion

This value is `nil` unless an fetch attempt failed. It contains the latest error from SwiftData. Access it from Query’s stored property:

```swift
struct RecipeList: View {
    @Query var recipes: [Recipe]
    var body: some View {
        ErrorIndicatorView(_recipes.fetchError)
    }
}
```

> **Note**: Only access this property within of a view’s `body` property, otherwise its value may be invalid.

> **Note**: When an fetch error occurs, `wrappedValue` retains results from the last successful fetch. Its value will update once a new fetch succeeds.

## See Also

- [var modelContext: ModelContext](query/modelcontext.md)
  Current model context `Query` interacts with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/fetcherror)*