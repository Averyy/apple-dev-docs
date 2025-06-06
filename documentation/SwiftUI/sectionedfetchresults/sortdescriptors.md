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

Set this value to cause the associated [`SectionedFetchRequest`](sectionedfetchrequest.md) to execute a fetch with a new collection of [`SortDescriptor`](https://developer.apple.com/documentation/Foundation/SortDescriptor) instances. The order of entities stored in the results collection may change as a result. Use care to coordinate section and sort updates, as described in [`SectionedFetchRequest.Configuration`](sectionedfetchrequest/configuration.md).

If you want to use [`NSSortDescriptor`](https://developer.apple.com/documentation/Foundation/NSSortDescriptor) instances, set [`nsSortDescriptors`](sectionedfetchresults/nssortdescriptors.md) instead.

## See Also

- [var nsPredicate: NSPredicate?](sectionedfetchresults/nspredicate.md)
  The request’s predicate.
- [var nsSortDescriptors: [NSSortDescriptor]](sectionedfetchresults/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.
- [var sectionIdentifier: KeyPath<Result, SectionIdentifier>](sectionedfetchresults/sectionidentifier.md)
  The key path that the system uses to group fetched results into sections.
- [SectionedFetchResults.Section](sectionedfetchresults/section.md)
  A collection of fetched results that share a specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchresults/sortdescriptors)*