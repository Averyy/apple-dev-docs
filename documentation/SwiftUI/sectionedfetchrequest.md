# SectionedFetchRequest

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.

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
@propertyWrapper @preconcurrency struct SectionedFetchRequest<SectionIdentifier, Result> where SectionIdentifier : Hashable, Result : NSFetchRequestResult
```

#### Overview

Use a `SectionedFetchRequest` property wrapper to declare a [`SectionedFetchResults`](sectionedfetchresults.md) property that provides a grouped collection of Core Data managed objects to a SwiftUI view. If you don’t need sectioning, use [`FetchRequest`](fetchrequest.md) instead.

Configure a sectioned fetch request with an optional predicate and sort descriptors, and include a `sectionIdentifier` parameter to indicate how to group the fetched results. Be sure that you choose sorting and sectioning that work together to avoid discontiguous sections. For example, you can request a list of earthquakes, composed of `Quake` managed objects that the [`Loading and Displaying a Large Data Feed`](loading_and_displaying_a_large_data_feed.md) sample code project defines to store earthquake data, sorted by time and grouped by date:

```swift
@SectionedFetchRequest<String, Quake>(
    sectionIdentifier: \.day,
    sortDescriptors: [SortDescriptor(\.time, order: .reverse)]
)
private var quakes: SectionedFetchResults<String, Quake>
```

Always declare properties that have a sectioned fetch request wrapper as private. This lets the compiler help you avoid accidentally setting the property from the memberwise initializer of the enclosing view.

The request infers the entity type from the `Result` type that you specify, which is `Quake` in the example above. Indicate a `SectionIdentifier` type to declare the type found at the fetched object’s `sectionIdentifier` key path. The section identifier type must conform to the [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) protocol.

The example above depends on the `Quake` type having a `day` property that’s either a stored or computed string. Be sure to mark any computed property with the `@objc` attribute for it to function as a section identifier. For best performance with large data sets, use stored properties.

The sectioned fetch request and its results use the managed object context stored in the environment, which you can access using the [`managedObjectContext`](environmentvalues/managedobjectcontext.md) environment value. To support user interface activity, you typically rely on the [`viewContext`](https://developer.apple.com/documentation/CoreData/NSPersistentContainer/viewContext) property of a shared [`NSPersistentContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentContainer) instance. For example, you can set a context on your top-level content view using a shared container that you define as part of your model:

```swift
ContentView()
    .environment(
        \.managedObjectContext,
        QuakesProvider.shared.container.viewContext)
```

When you need to dynamically change the section identifier, predicate, or sort descriptors, access the request’s [`SectionedFetchRequest.Configuration`](sectionedfetchrequest/configuration.md) structure, either directly or with a binding.

## Topics

### Creating a fetch request
- [init(sectionIdentifier:sortDescriptors:predicate:animation:)](sectionedfetchrequest/init(sectionidentifier:sortdescriptors:predicate:animation:).md)
  Creates a sectioned fetch request based on a section identifier, a predicate, and reference type sort parameters.
- [init(entity: NSEntityDescription, sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors: [NSSortDescriptor], predicate: NSPredicate?, animation: Animation?)](sectionedfetchrequest/init(entity:sectionidentifier:sortdescriptors:predicate:animation:).md)
  Creates a sectioned fetch request for a specified entity description, based on a section identifier, a predicate, and sort parameters.
### Creating a fully configured fetch request
- [init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result, SectionIdentifier>, animation: Animation?)](sectionedfetchrequest/init(fetchrequest:sectionidentifier:animation:).md)
  Creates a fully configured sectioned fetch request that uses the specified animation when updating results.
- [init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result, SectionIdentifier>, transaction: Transaction)](sectionedfetchrequest/init(fetchrequest:sectionidentifier:transaction:).md)
  Creates a fully configured sectioned fetch request that uses the specified transaction when updating results.
### Configuring a request dynamically
- [SectionedFetchRequest.Configuration](sectionedfetchrequest/configuration.md)
  The request’s configurable properties.
- [var projectedValue: Binding<SectionedFetchRequest<SectionIdentifier, Result>.Configuration>](sectionedfetchrequest/projectedvalue.md)
  A binding to the request’s mutable configuration properties.
### Getting the fetched results
- [func update()](sectionedfetchrequest/update.md)
  Updates the fetched results.
- [var wrappedValue: SectionedFetchResults<SectionIdentifier, Result>](sectionedfetchrequest/wrappedvalue.md)
  The fetched results of the fetch request.
### Default Implementations
- [DynamicProperty Implementations](sectionedfetchrequest/dynamicproperty-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [DynamicProperty](dynamicproperty.md)

## See Also

- [Loading and displaying a large data feed](loading-and-displaying-a-large-data-feed.md)
  Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [var managedObjectContext: NSManagedObjectContext](environmentvalues/managedobjectcontext.md)
- [struct FetchRequest](fetchrequest.md)
  A property wrapper type that retrieves entities from a Core Data persistent store.
- [struct FetchedResults](fetchedresults.md)
  A collection of results retrieved from a Core Data store.
- [struct SectionedFetchResults](sectionedfetchresults.md)
  A collection of results retrieved from a Core Data persistent store, grouped into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest)*