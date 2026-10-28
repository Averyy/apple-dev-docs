# sortDescriptors

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

Available when `SectionIdentifier` conforms to `Hashable` and `Result` inherits `NSManagedObject`.

## Discussion

Set this value to cause the associated [`SectionedFetchRequest`](../sectionedfetchrequest.md) to execute a fetch with a new collection of [`SortDescriptor`](../../Foundation/sortdescriptor.md) instances. The order of entities stored in the results collection may change as a result. Use care to coordinate section and sort updates, as described in [`SectionedFetchRequest.Configuration`](../sectionedfetchrequest/configuration.md).

If you want to use [`NSSortDescriptor`](../../Foundation/nssortdescriptor.md) instances, set [`nsSortDescriptors`](./nssortdescriptors.md) instead.

## See Also

### Configuring the associated sectioned fetch request
- [var nsPredicate: NSPredicate?](./nspredicate.md)
  The request’s predicate.
- [var nsSortDescriptors: [NSSortDescriptor]](./nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.
- [var sectionIdentifier: KeyPath<Result, SectionIdentifier>](./sectionidentifier.md)
  The key path that the system uses to group fetched results into sections.
- [SectionedFetchResults.Section](./section.md)
  A collection of fetched results that share a specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchresults/sortdescriptors)*