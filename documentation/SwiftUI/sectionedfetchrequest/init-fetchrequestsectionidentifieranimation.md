# init(fetchRequest:sectionIdentifier:animation:)

**Framework**: SwiftUI  
**Kind**: init

Creates a fully configured sectioned fetch request that uses the specified animation when updating results.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
@preconcurrency init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result, SectionIdentifier>, animation: Animation? = nil)
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

Use the request to define a `SectionedFetchedResults` property:

```swift
@SectionedFetchRequest<String, Quake>(
    fetchRequest: Quake.request,
    sectionIdentifier: \.day)
private var quakes: FetchedResults<String, Quake>
```

If you only need to configure the request’s section identifier, predicate, and sort descriptors, use [`init(sectionIdentifier:sortDescriptors:predicate:animation:)`](sectionedfetchrequest/init(sectionidentifier:sortdescriptors:predicate:animation:).md) instead. If you need to specify a [`Transaction`](transaction.md) rather than an optional [`Animation`](animation.md), use [`init(fetchRequest:sectionIdentifier:transaction:)`](sectionedfetchrequest/init(fetchrequest:sectionidentifier:transaction:).md).

## Parameters

- `fetchRequest`: An     instance that describes the search criteria for retrieving data   from the persistent store.
- `sectionIdentifier`: A key path that SwiftUI applies to the    type to get an object’s section identifier.
- `animation`: The animation to use for user interface changes that   result from changes to the fetched results.

## See Also

- [init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result, SectionIdentifier>, transaction: Transaction)](sectionedfetchrequest/init(fetchrequest:sectionidentifier:transaction:).md)
  Creates a fully configured sectioned fetch request that uses the specified transaction when updating results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/init(fetchrequest:sectionidentifier:animation:))*