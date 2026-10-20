# init(fetchRequest:transaction:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Result` conforms to `NSFetchRequestResult`.

#### Discussion

Use this initializer if you need a fetch request with updates that affect the user interface based on a [`Transaction`](../transaction.md). Otherwise, use [`init(fetchRequest:animation:)`](./init%28fetchrequest,animation%29.md).

## Parameters

- `fetchRequest`: An [`NSFetchRequest`](../../CoreData/nsfetchrequest.md) instance that describes the search criteria for retrieving data from the persistent store.
- `transaction`: A transaction to use for user interface changes that result from changes to the fetched results.

## See Also

### Creating a fully configured fetch request
- [init(fetchRequest: NSFetchRequest<Result>, animation: Animation?)](./init%28fetchrequest,animation%29.md)
  Creates a fully configured fetch request that uses the specified animation when updating results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/init(fetchrequest:transaction:))*