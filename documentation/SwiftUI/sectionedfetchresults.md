# SectionedFetchResults

**Framework**: SwiftUI  
**Kind**: struct

A collection of results retrieved from a Core Data persistent store, grouped into sections.

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
@preconcurrency struct SectionedFetchResults<SectionIdentifier, Result> where SectionIdentifier : Hashable, Result : NSFetchRequestResult
```

#### Overview

Use a `SectionedFetchResults` instance to show or edit Core Data managed objects, grouped into sections, in your app’s user interface. If you don’t need sectioning, use [`FetchedResults`](fetchedresults.md) instead.

You request a particular set of results by annotating the fetched results property declaration with a [`SectionedFetchRequest`](sectionedfetchrequest.md) property wrapper. Indicate the type of the fetched entities with a `Results` type, and the type of the identifier that distinguishes the sections with a `SectionIdentifier` type. For example, you can create a request to list all `Quake` managed objects that the [`Loading and Displaying a Large Data Feed`](loading_and_displaying_a_large_data_feed.md) sample code project defines to store earthquake data, sorted by their `time` property and grouped by a string that represents the days when earthquakes occurred:

```swift
@SectionedFetchRequest<String, Quake>(
    sectionIdentifier: \.day,
    sortDescriptors: [SortDescriptor(\.time, order: .reverse)]
)
private var quakes: SectionedFetchResults<String, Quake>
```

The `quakes` property acts as a collection of [`SectionedFetchResults.Section`](sectionedfetchresults/section.md) instances, each containing a collection of `Quake` instances. The example above depends on the `Quake` model object declaring both `time` and `day` properties, either stored or computed. For best performance with large data sets, use stored properties.

The collection of sections, as well as the collection of managed objects in each section, conforms to the [`RandomAccessCollection`](https://developer.apple.com/documentation/Swift/RandomAccessCollection) protocol, so you can access them as you would any other collection. For example, you can create nested [`ForEach`](foreach.md) loops inside a [`List`](list.md) to iterate over the results:

```swift
List {
    ForEach(quakes) { section in
        Section(header: Text(section.id)) {
            ForEach(section) { quake in
                QuakeRow(quake: quake) // Displays information about a quake.
            }
        }
    }
}
```

Don’t confuse the [`Section`](section.md) view that you use to create a hierarchical display with the [`SectionedFetchResults.Section`](sectionedfetchresults/section.md) instances that hold the fetched results.

When you need to dynamically change the request’s section identifier, predicate, or sort descriptors, set the result instance’s [`sectionIdentifier`](sectionedfetchresults/sectionidentifier.md), [`nsPredicate`](sectionedfetchresults/nspredicate.md), and [`sortDescriptors`](sectionedfetchresults/sortdescriptors.md) or [`nsSortDescriptors`](sectionedfetchresults/nssortdescriptors.md) properties, respectively. Be sure that the sorting and sectioning work together to avoid discontinguous sections.

The fetch request and its results use the managed object context stored in the environment, which you can access using the [`managedObjectContext`](environmentvalues/managedobjectcontext.md) environment value. To support user interface activity, you typically rely on the [`viewContext`](https://developer.apple.com/documentation/CoreData/NSPersistentContainer/viewContext) property of a shared [`NSPersistentContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentContainer) instance. For example, you can set a context on your top-level content view using a container that you define as part of your model:

```swift
ContentView()
    .environment(
        \.managedObjectContext,
        QuakesProvider.shared.container.viewContext)
```

## Topics

### Configuring the associated sectioned fetch request
- [var nsPredicate: NSPredicate?](sectionedfetchresults/nspredicate.md)
  The request’s predicate.
- [var sortDescriptors: [SortDescriptor<Result>]](sectionedfetchresults/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var nsSortDescriptors: [NSSortDescriptor]](sectionedfetchresults/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.
- [var sectionIdentifier: KeyPath<Result, SectionIdentifier>](sectionedfetchresults/sectionidentifier.md)
  The key path that the system uses to group fetched results into sections.
- [SectionedFetchResults.Section](sectionedfetchresults/section.md)
  A collection of fetched results that share a specified identifier.
### Getting indices
- [var startIndex: Int](sectionedfetchresults/startindex.md)
  The index of the first section in the results collection.
- [var endIndex: Int](sectionedfetchresults/endindex.md)
  The index that’s one greater than that of the last section.
### Getting results
- [subscript(Int) -> SectionedFetchResults<SectionIdentifier, Result>.Section](sectionedfetchresults/subscript(_:).md)
  Gets the section at the specified index.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [Loading and Displaying a Large Data Feed](loading_and_displaying_a_large_data_feed.md)
  Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [var managedObjectContext: NSManagedObjectContext](environmentvalues/managedobjectcontext.md)
- [struct FetchRequest](fetchrequest.md)
  A property wrapper type that retrieves entities from a Core Data persistent store.
- [struct FetchedResults](fetchedresults.md)
  A collection of results retrieved from a Core Data store.
- [struct SectionedFetchRequest](sectionedfetchrequest.md)
  A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchresults)*