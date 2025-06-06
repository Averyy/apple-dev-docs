# init(sortDescriptors:predicate:animation:)

**Framework**: SwiftUI  
**Kind**: init

Creates a fetch request based on a predicate and reference type sort parameters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency init(sortDescriptors: [NSSortDescriptor], predicate: NSPredicate? = nil, animation: Animation? = nil)
```

#### Discussion

The request gets the entity type from the `Result` instance by calling that managed object’s [`entity()`](https://developer.apple.com/documentation/CoreData/NSManagedObject/entity()) type method. If you need to specify the entity type explicitly, use the [`init(entity:sortDescriptors:predicate:animation:)`](fetchrequest/init(entity:sortdescriptors:predicate:animation:).md) initializer instead. If you need more control over the fetch request configuration, use [`init(fetchRequest:animation:)`](fetchrequest/init(fetchrequest:animation:).md).

## Parameters

- `sortDescriptors`: An array of sort descriptors that define the sort   order of the fetched results.
- `predicate`: An     instance that defines logical conditions used to filter the fetched   results.
- `animation`: The animation to use for user interface changes that   result from changes to the fetched results.

## See Also

- [init(entity: NSEntityDescription, sortDescriptors: [NSSortDescriptor], predicate: NSPredicate?, animation: Animation?)](fetchrequest/init(entity:sortdescriptors:predicate:animation:).md)
  Creates a fetch request for a specified entity description, based on a predicate and sort parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/init(sortdescriptors:predicate:animation:))*