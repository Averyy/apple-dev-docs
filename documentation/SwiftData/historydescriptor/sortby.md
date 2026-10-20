# sortBy

**Framework**: SwiftData  
**Kind**: property  
**Role**: Instance Property

The sort descriptor to use to sort the returned history data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+
- Swift 5.9+

## Declaration

```swift
var sortBy: [SortDescriptor<TransactionType>]
```

## See Also

### Getting the descriptor configuration
- [var fetchLimit: UInt64](./fetchlimit.md)
  The maximum number of transactions to retrieve from the model store’s history.
- [var predicate: Predicate<TransactionType>?](./predicate.md)
  The predicate used to initialize the history descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydescriptor/sortby)*