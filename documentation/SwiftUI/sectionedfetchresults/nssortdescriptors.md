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

Set this value to cause the associated [`SectionedFetchRequest`](sectionedfetchrequest.md) to execute a fetch with a new collection of [`NSSortDescriptor`](https://developer.apple.com/documentation/Foundation/NSSortDescriptor) instances. The order of managed objects stored in the results collection may change as a result. Use care to coordinate section and sort updates, as described in [`SectionedFetchRequest.Configuration`](sectionedfetchrequest/configuration.md).

If you want to use [`SortDescriptor`](https://developer.apple.com/documentation/Foundation/SortDescriptor) instances, set [`sortDescriptors`](sectionedfetchresults/sortdescriptors.md) instead.

## See Also

- [var nsPredicate: NSPredicate?](sectionedfetchresults/nspredicate.md)
  The request’s predicate.
- [var sortDescriptors: [SortDescriptor<Result>]](sectionedfetchresults/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var sectionIdentifier: KeyPath<Result, SectionIdentifier>](sectionedfetchresults/sectionidentifier.md)
  The key path that the system uses to group fetched results into sections.
- [SectionedFetchResults.Section](sectionedfetchresults/section.md)
  A collection of fetched results that share a specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchresults/nssortdescriptors)*