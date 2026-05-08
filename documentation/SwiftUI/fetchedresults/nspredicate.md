# nsPredicate

**Framework**: SwiftUI  
**Kind**: property

The request’s predicate.

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
@preconcurrency var nsPredicate: NSPredicate? { get nonmutating set }
```

#### Discussion

Set this value to cause the associated [`FetchRequest`](fetchrequest.md) to execute a fetch with a new predicate, producing an updated collection of results.

## See Also

- [var sortDescriptors: [SortDescriptor<Result>]](fetchedresults/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var nsSortDescriptors: [NSSortDescriptor]](fetchedresults/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchedresults/nspredicate)*