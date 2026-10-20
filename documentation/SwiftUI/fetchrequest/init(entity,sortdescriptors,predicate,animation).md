# init(entity:sortDescriptors:predicate:animation:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a fetch request for a specified entity description, based on a predicate and sort parameters.

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
@preconcurrency init(entity: NSEntityDescription, sortDescriptors: [NSSortDescriptor], predicate: NSPredicate? = nil, animation: Animation? = nil)
```

Available when `Result` conforms to `NSFetchRequestResult`.

#### Discussion

Use this initializer if you need to explicitly specify the entity type for the request. If you specify a placeholder `Result` type in the request declaration, use the [`init(sortDescriptors:predicate:animation:)`](./init%28sortdescriptors,predicate,animation%29.md) initializer to let the request infer the entity type. If you need more control over the fetch request configuration, use [`init(fetchRequest:animation:)`](./init%28fetchrequest,animation%29.md).

## Parameters

- `entity`: The description of the Core Data entity to fetch.
- `sortDescriptors`: An array of sort descriptors that define the sort order of the fetched results.
- `predicate`: An [`NSPredicate`](../../Foundation/nspredicate.md) instance that defines logical conditions used to filter the fetched results.
- `animation`: The animation to use for user interface changes that result from changes to the fetched results.

## See Also

### Creating a fetch request
- [init(sortDescriptors:predicate:animation:)](./init%28sortdescriptors,predicate,animation%29.md)
  Creates a fetch request based on a predicate and reference type sort parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/init(entity:sortdescriptors:predicate:animation:))*