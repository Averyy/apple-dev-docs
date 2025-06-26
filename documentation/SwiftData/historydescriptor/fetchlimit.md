# fetchLimit

**Framework**: SwiftData  
**Kind**: property

The maximum number of transactions to retrieve from the model store’s history.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
var fetchLimit: UInt64
```

#### Discussion

> ❗ **Important**: Use `nil` to tell the fetch to return all transactions of the associated type, not `0`.

The default value is `nil`.

## See Also

- [var predicate: Predicate<TransactionType>?](historydescriptor/predicate.md)
  The predicate used to initialize the history descriptor.
- [var sortBy: [SortDescriptor<TransactionType>]](historydescriptor/sortby.md)
  The sort descriptor to use to sort the returned history data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydescriptor/fetchlimit)*