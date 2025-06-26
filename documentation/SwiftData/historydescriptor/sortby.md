# sortBy

**Framework**: SwiftData  
**Kind**: property

The sort descriptor to use to sort the returned history data.

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
var sortBy: [SortDescriptor<TransactionType>]
```

## See Also

- [var fetchLimit: UInt64](historydescriptor/fetchlimit.md)
  The maximum number of transactions to retrieve from the model store’s history.
- [var predicate: Predicate<TransactionType>?](historydescriptor/predicate.md)
  The predicate used to initialize the history descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydescriptor/sortby)*