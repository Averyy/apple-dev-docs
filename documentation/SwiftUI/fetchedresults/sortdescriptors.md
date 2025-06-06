# sortDescriptors

**Framework**: SwiftUI  
**Kind**: property

The request’s sort descriptors, accessed as value types.

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
@preconcurrency var sortDescriptors: [SortDescriptor<Result>] { get nonmutating set }
```

#### Discussion

Set this value to cause the associated [`FetchRequest`](fetchrequest.md) to execute a fetch with a new collection of [`SortDescriptor`](https://developer.apple.com/documentation/Foundation/SortDescriptor) instances. The order of entities stored in the results collection may change as a result.

If you want to use [`NSSortDescriptor`](https://developer.apple.com/documentation/Foundation/NSSortDescriptor) instances, set [`nsSortDescriptors`](fetchedresults/nssortdescriptors.md) instead.

## See Also

- [var nsPredicate: NSPredicate?](fetchedresults/nspredicate.md)
  The request’s predicate.
- [var nsSortDescriptors: [NSSortDescriptor]](fetchedresults/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchedresults/sortdescriptors)*