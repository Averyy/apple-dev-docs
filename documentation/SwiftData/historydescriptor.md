# HistoryDescriptor

**Framework**: SwiftData  
**Kind**: struct

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
struct HistoryDescriptor<TransactionType> where TransactionType : HistoryTransaction
```

## Topics

### Initializers
- [init(predicate: Predicate<TransactionType>?)](historydescriptor/init(predicate:).md)
- [init(predicate: Predicate<TransactionType>?, sortBy: [SortDescriptor<TransactionType>])](historydescriptor/init(predicate:sortby:).md)
### Instance Properties
- [var fetchLimit: UInt64](historydescriptor/fetchlimit.md)
- [var predicate: Predicate<TransactionType>?](historydescriptor/predicate.md)
- [var sortBy: [SortDescriptor<TransactionType>]](historydescriptor/sortby.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydescriptor)*