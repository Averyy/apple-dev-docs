# init(predicate:sortBy:)

**Framework**: SwiftData  
**Kind**: init

Initializes a new history descriptor with the provided predicate and sort descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)
- Swift 5.9+

## Declaration

```swift
init(predicate: Predicate<TransactionType>? = nil, sortBy: [SortDescriptor<TransactionType>] = [])
```

#### Discussion

If you don’t specify a predicate, any fetch using this descriptor will return all models of the associated type. If you expect the number of fetched transactions to be high, use [`fetchLimit`](historydescriptor/fetchlimit.md) to limit the number of transactions returned.

## Parameters

- `predicate`: The logical condition that determines whether the history includes a specific model in its results. The default value is  .
- `sortBy`: The array of sort descriptors that tell the history how to order its results. The default value is an empty array.

## See Also

- [init(predicate: Predicate<TransactionType>?)](historydescriptor/init(predicate:).md)
  Initializes a new history descriptor with the provided predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydescriptor/init(predicate:sortby:))*