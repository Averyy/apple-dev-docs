# FetchedResults

**Framework**: SwiftUI  
**Kind**: struct

A collection of results retrieved from a Core Data store.

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
@preconcurrency struct FetchedResults<Result> where Result : NSFetchRequestResult
```

#### Overview

Use a `FetchedResults` instance to show or edit Core Data managed objects in your app’s user interface. You request a particular set of results by specifying a `Result` type as the entity type, and annotating the fetched results property declaration with a [`FetchRequest`](fetchrequest.md) property wrapper. For example, you can create a request to list all `Quake` managed objects that the [`Loading and Displaying a Large Data Feed`](loading_and_displaying_a_large_data_feed.md) sample code project defines to store earthquake data, sorted by their `time` property:

```swift
@FetchRequest(sortDescriptors: [SortDescriptor(\.time, order: .reverse)])
private var quakes: FetchedResults<Quake>
```

The results instance conforms to [`RandomAccessCollection`](https://developer.apple.com/documentation/Swift/RandomAccessCollection), so you access it like any other collection. For example, you can create a [`List`](list.md) that iterates over all the results:

```swift
List(quakes) { quake in
    NavigationLink(destination: QuakeDetail(quake: quake)) {
        QuakeRow(quake: quake)
    }
}
```

When you need to dynamically change the request’s predicate or sort descriptors, set the result instance’s [`nsPredicate`](fetchedresults/nspredicate.md) and [`sortDescriptors`](fetchedresults/sortdescriptors.md) or [`nsSortDescriptors`](fetchedresults/nssortdescriptors.md) properties, respectively.

The fetch request and its results use the managed object context stored in the environment, which you can access using the [`managedObjectContext`](environmentvalues/managedobjectcontext.md) environment value. To support user interface activity, you typically rely on the [`viewContext`](https://developer.apple.com/documentation/CoreData/NSPersistentContainer/viewContext) property of a shared [`NSPersistentContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentContainer) instance. For example, you can set a context on your top level content view using a container that you define as part of your model:

```swift
ContentView()
    .environment(
        \.managedObjectContext,
        QuakesProvider.shared.container.viewContext)
```

## Topics

### Configuring the associated fetch request
- [var nsPredicate: NSPredicate?](fetchedresults/nspredicate.md)
  The request’s predicate.
- [var sortDescriptors: [SortDescriptor<Result>]](fetchedresults/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var nsSortDescriptors: [NSSortDescriptor]](fetchedresults/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.
### Getting indices
- [var startIndex: Int](fetchedresults/startindex.md)
  The index of the first entity in the results collection.
- [var endIndex: Int](fetchedresults/endindex.md)
  The index that’s one greater than the last valid subscript argument.
### Getting results
- [subscript(Int) -> Result](fetchedresults/subscript(_:).md)
  Gets the entity at the specified index.

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
- [struct SectionedFetchRequest](sectionedfetchrequest.md)
  A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.
- [struct SectionedFetchResults](sectionedfetchresults.md)
  A collection of results retrieved from a Core Data persistent store, grouped into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchedresults)*