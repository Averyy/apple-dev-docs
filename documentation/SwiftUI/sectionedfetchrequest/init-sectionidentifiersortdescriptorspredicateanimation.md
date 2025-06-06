# init(sectionIdentifier:sortDescriptors:predicate:animation:)

**Framework**: SwiftUI  
**Kind**: init

Creates a sectioned fetch request based on a section identifier, a predicate, and reference type sort parameters.

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
@preconcurrency init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors: [NSSortDescriptor], predicate: NSPredicate? = nil, animation: Animation? = nil)
```

#### Discussion

The request gets the entity type from the `Result` instance by calling that managed object’s [`entity()`](https://developer.apple.com/documentation/CoreData/NSManagedObject/entity()) type method. If you need to specify the entity type explicitly, use the [`init(entity:sectionIdentifier:sortDescriptors:predicate:animation:)`](sectionedfetchrequest/init(entity:sectionidentifier:sortdescriptors:predicate:animation:).md) initializer instead. If you need more control over the fetch request configuration, use [`init(fetchRequest:sectionIdentifier:animation:)`](sectionedfetchrequest/init(fetchrequest:sectionidentifier:animation:).md). For value type sort descriptors, use [`init(sectionIdentifier:sortDescriptors:predicate:animation:)`](sectionedfetchrequest/init(sectionidentifier:sortdescriptors:predicate:animation:).md).

## Parameters

- `sectionIdentifier`: A key path that SwiftUI applies to the    type to get an object’s section identifier.
- `sortDescriptors`: An array of sort descriptors that define the sort   order of the fetched results.
- `predicate`: An     instance that defines logical conditions used to filter the fetched   results.
- `animation`: The animation to use for user interface changes that   result from changes to the fetched results.

## See Also

- [init(entity: NSEntityDescription, sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors: [NSSortDescriptor], predicate: NSPredicate?, animation: Animation?)](sectionedfetchrequest/init(entity:sectionidentifier:sortdescriptors:predicate:animation:).md)
  Creates a sectioned fetch request for a specified entity description, based on a section identifier, a predicate, and sort parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/init(sectionidentifier:sortdescriptors:predicate:animation:))*