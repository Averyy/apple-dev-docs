# init(fetchRequest:sectionIdentifier:transaction:)

**Framework**: SwiftUI  
**Kind**: init

Creates a fully configured sectioned fetch request that uses the specified transaction when updating results.

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
@preconcurrency init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result, SectionIdentifier>, transaction: Transaction)
```

#### Discussion

Use this initializer if you need a fetch request with updates that affect the user interface based on a [`Transaction`](transaction.md). Otherwise, use [`init(fetchRequest:sectionIdentifier:animation:)`](sectionedfetchrequest/init(fetchrequest:sectionidentifier:animation:).md).

## Parameters

- `fetchRequest`: An     instance that describes the search criteria for retrieving data   from the persistent store.
- `sectionIdentifier`: A key path that SwiftUI applies to the    type to get an object’s section identifier.
- `transaction`: A transaction to use for user interface changes that   result from changes to the fetched results.

## See Also

- [init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result, SectionIdentifier>, animation: Animation?)](sectionedfetchrequest/init(fetchrequest:sectionidentifier:animation:).md)
  Creates a fully configured sectioned fetch request that uses the specified animation when updating results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/init(fetchrequest:sectionidentifier:transaction:))*