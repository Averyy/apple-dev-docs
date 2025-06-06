# init(filter:sort:animation:)

**Framework**: SwiftData  
**Kind**: init

Create a query with a predicate, and a list of sort descriptors.

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
@preconcurrency init(filter: Predicate<Element>? = nil, sort descriptors: [SortDescriptor<Element>] = [], animation: Animation) where Result == [Element]
```

#### Discussion

Use `Query` within a view by wrapping the variable for the query’s result:

```swift
struct RecipeList: View {
    // Favorite recipes sorted by date of creation
    @Query(
        filter: #Predicate { $0.isFavorite == true },
        sort: [SortDescriptor(\.dateCreated)]
    )
    var favoriteRecipes: [Recipe]

    var body: some View {
        List(favoriteRecipes) { RecipeDetails($0) }
    }
}
```

## Parameters

- `filter`: A predicate on 
- `descriptors`: Sort orders for the result.
- `animation`: The animation to use for user interface changes that   result from changes to the fetched results.

## See Also

- [init(FetchDescriptor<Element>, animation: Animation)](query/init(_:animation:).md)
  Create a query with a SwiftData fetch descriptor.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation)](query/init(filter:sort:order:animation:)-1qfoj.md)
  Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation)](query/init(filter:sort:order:animation:)-3qovd.md)
  Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(FetchDescriptor<Element>, transaction: Transaction?)](query/init(_:transaction:).md)
  Create a query with a SwiftData fetch descriptor.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?)](query/init(filter:sort:transaction:).md)
  Create a query with a predicate, and a list of sort descriptors.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?)](query/init(filter:sort:order:transaction:)-2bx9a.md)
  Create a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?)](query/init(filter:sort:order:transaction:)-8q7vs.md)
  Create a query with a predicate, a key path to a property for sorting, and the order to sort by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/init(filter:sort:animation:))*