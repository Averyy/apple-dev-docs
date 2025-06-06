# init(fetchRequest:transaction:)

**Framework**: SwiftUI  
**Kind**: init

Creates a fully configured fetch request that uses the specified transaction when updating results.

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
@preconcurrency init(fetchRequest: NSFetchRequest<Result>, transaction: Transaction)
```

#### Discussion

Use this initializer if you need a fetch request with updates that affect the user interface based on a [`Transaction`](transaction.md). Otherwise, use [`init(fetchRequest:animation:)`](fetchrequest/init(fetchrequest:animation:).md).

## Parameters

- `fetchRequest`: An     instance that describes the search criteria for retrieving data   from the persistent store.
- `transaction`: A transaction to use for user interface changes that   result from changes to the fetched results.

## See Also

- [init(fetchRequest: NSFetchRequest<Result>, animation: Animation?)](fetchrequest/init(fetchrequest:animation:).md)
  Creates a fully configured fetch request that uses the specified animation when updating results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/init(fetchrequest:transaction:))*