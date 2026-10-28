# nsSortDescriptors

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

Set this value to cause the associated [`SectionedFetchRequest`](../sectionedfetchrequest.md) to execute a fetch with a new collection of [`NSSortDescriptor`](../../Foundation/nssortdescriptor.md) instances. The order of managed objects stored in the results collection may change as a result. Use care to coordinate section and sort updates, as described in [`SectionedFetchRequest.Configuration`](../sectionedfetchrequest/configuration.md).

If you want to use [`SortDescriptor`](../../Foundation/sortdescriptor.md) instances, set [`sortDescriptors`](./sortdescriptors.md) instead.

## See Also

### Configuring the associated sectioned fetch request
- [var nsPredicate: NSPredicate?](./nspredicate.md)
  The request’s predicate.
- [var sortDescriptors: [SortDescriptor<Result>]](./sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var sectionIdentifier: KeyPath<Result, SectionIdentifier>](./sectionidentifier.md)
  The key path that the system uses to group fetched results into sections.
- [SectionedFetchResults.Section](./section.md)
  A collection of fetched results that share a specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchresults/nssortdescriptors)*