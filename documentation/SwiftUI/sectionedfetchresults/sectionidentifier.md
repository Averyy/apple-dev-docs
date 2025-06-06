# sectionIdentifier

**Framework**: SwiftUI  
**Kind**: property

The key path that the system uses to group fetched results into sections.

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
@preconcurrency var sectionIdentifier: KeyPath<Result, SectionIdentifier> { get nonmutating set }
```

#### Discussion

Set this value to cause the associated [`SectionedFetchRequest`](sectionedfetchrequest.md) to execute a fetch with a new section identifier, producing an updated collection of results. Changing this value produces a new set of sections. Use care to coordinate section and sort updates, as described in [`SectionedFetchRequest.Configuration`](sectionedfetchrequest/configuration.md).

## See Also

- [var nsPredicate: NSPredicate?](sectionedfetchresults/nspredicate.md)
  The request’s predicate.
- [var sortDescriptors: [SortDescriptor<Result>]](sectionedfetchresults/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var nsSortDescriptors: [NSSortDescriptor]](sectionedfetchresults/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.
- [SectionedFetchResults.Section](sectionedfetchresults/section.md)
  A collection of fetched results that share a specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchresults/sectionidentifier)*