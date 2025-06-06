# init(fetchRequest:animation:)

**Framework**: SwiftUI  
**Kind**: init

Creates a fully configured fetch request that uses the specified animation when updating results.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency init(fetchRequest: NSFetchRequest<Result>, animation: Animation? = nil)
```

#### Discussion

Use this initializer when you want to configure a fetch request with more than a predicate and sort descriptors. For example, you can vend a request from a `Quake` managed object that the [`Loading and Displaying a Large Data Feed`](loading_and_displaying_a_large_data_feed.md) sample code project defines to store earthquake data. Limit the number of results to `1000` by setting a [`fetchLimit`](https://developer.apple.com/documentation/CoreData/NSFetchRequest/fetchLimit) for the request:

```swift
extension Quake {
    var request: NSFetchRequest<Quake> {
        let request = NSFetchRequest<Quake>(entityName: "Quake")
        request.sortDescriptors = [
            NSSortDescriptor(
                keyPath: \Quake.time,
                ascending: true)]
        request.fetchLimit = 1000
        return request
    }
}
```

Use the request to define a [`FetchedResults`](fetchedresults.md) property:

```swift
@FetchRequest(fetchRequest: Quake.request)
private var quakes: FetchedResults<Quake>
```

If you only need to configure the request’s predicate and sort descriptors, use [`init(sortDescriptors:predicate:animation:)`](fetchrequest/init(sortdescriptors:predicate:animation:).md) instead. If you need to specify a [`Transaction`](transaction.md) rather than an optional [`Animation`](animation.md), use [`init(fetchRequest:transaction:)`](fetchrequest/init(fetchrequest:transaction:).md).

## Parameters

- `fetchRequest`: An     instance that describes the search criteria for retrieving data   from the persistent store.
- `animation`: The animation to use for user interface changes that   result from changes to the fetched results.

## See Also

- [init(fetchRequest: NSFetchRequest<Result>, transaction: Transaction)](fetchrequest/init(fetchrequest:transaction:).md)
  Creates a fully configured fetch request that uses the specified transaction when updating results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/init(fetchrequest:animation:))*