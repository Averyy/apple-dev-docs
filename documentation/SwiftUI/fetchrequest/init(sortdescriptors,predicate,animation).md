# init(sortDescriptors:predicate:animation:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Result` inherits `NSManagedObject`.

**Other overloads**:

```swift
@MainActor
@preconcurrency init(sortDescriptors: [SortDescriptor<Result>], predicate: NSPredicate? = nil, animation: Animation? = nil)
```

## Discussion

The request gets the entity type from the `Result` instance by calling that managed object’s [`entity()`](../../CoreData/nsmanagedobject/entity%28%29.md) type method. If you need to specify the entity type explicitly, use the [`init(entity:sortDescriptors:predicate:animation:)`](./init%28entity,sortdescriptors,predicate,animation%29.md) initializer instead. If you need more control over the fetch request configuration, use [`init(fetchRequest:animation:)`](./init%28fetchrequest,animation%29.md).

## Parameters

- `sortDescriptors`: An array of sort descriptors that define the sort order of the fetched results.
- `predicate`: An [`NSPredicate`](../../Foundation/nspredicate.md) instance that defines logical conditions used to filter the fetched results.
- `animation`: The animation to use for user interface changes that result from changes to the fetched results.

## See Also

### Creating a fetch request
- [init(entity: NSEntityDescription, sortDescriptors: [NSSortDescriptor], predicate: NSPredicate?, animation: Animation?)](./init%28entity,sortdescriptors,predicate,animation%29.md)
  Creates a fetch request for a specified entity description, based on a predicate and sort parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/init(sortdescriptors:predicate:animation:))*