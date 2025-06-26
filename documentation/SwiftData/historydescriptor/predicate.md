# predicate

**Framework**: SwiftData  
**Kind**: property

The predicate used to initialize the history descriptor.

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
var predicate: Predicate<TransactionType>?
```

## See Also

- [var fetchLimit: UInt64](historydescriptor/fetchlimit.md)
  The maximum number of transactions to retrieve from the model store’s history.
- [var sortBy: [SortDescriptor<TransactionType>]](historydescriptor/sortby.md)
  The sort descriptor to use to sort the returned history data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydescriptor/predicate)*