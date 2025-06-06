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

Set this value to cause the associated [`SectionedFetchRequest`](sectionedfetchrequest.md) to execute a fetch with a new predicate, producing an updated collection of results.

## See Also

- [var sortDescriptors: [SortDescriptor<Result>]](sectionedfetchresults/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var nsSortDescriptors: [NSSortDescriptor]](sectionedfetchresults/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.
- [var sectionIdentifier: KeyPath<Result, SectionIdentifier>](sectionedfetchresults/sectionidentifier.md)
  The key path that the system uses to group fetched results into sections.
- [SectionedFetchResults.Section](sectionedfetchresults/section.md)
  A collection of fetched results that share a specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchresults/nspredicate)*