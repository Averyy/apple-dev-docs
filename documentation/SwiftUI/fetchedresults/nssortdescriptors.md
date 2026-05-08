# nsSortDescriptors

**Framework**: SwiftUI  
**Kind**: property

The request’s sort descriptors, accessed as reference types.

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
@preconcurrency var nsSortDescriptors: [NSSortDescriptor] { get nonmutating set }
```

#### Discussion

Set this value to cause the associated [`FetchRequest`](fetchrequest.md) to execute a fetch with a new collection of [`NSSortDescriptor`](https://developer.apple.com/documentation/Foundation/NSSortDescriptor) instances. The order of managed objects stored in the results collection may change as a result.

If you want to use [`SortDescriptor`](https://developer.apple.com/documentation/Foundation/SortDescriptor) instances, set [`sortDescriptors`](fetchedresults/sortdescriptors.md) instead.

## See Also

- [var nsPredicate: NSPredicate?](fetchedresults/nspredicate.md)
  The request’s predicate.
- [var sortDescriptors: [SortDescriptor<Result>]](fetchedresults/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchedresults/nssortdescriptors)*