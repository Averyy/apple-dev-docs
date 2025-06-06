# init(fetchRequest:managedObjectContext:sectionNameKeyPath:cacheName:)

**Framework**: Core Data  
**Kind**: init

Returns a fetch request controller initialized using the given arguments.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(fetchRequest: NSFetchRequest<ResultType>, managedObjectContext context: NSManagedObjectContext, sectionNameKeyPath: String?, cacheName name: String?)
```

#### Return Value

The receiver initialized with the specified fetch request, context, key path, and cache name.

## Parameters

- `fetchRequest`: The fetch request must have at least one sort descriptor. If the controller generates sections, the first sort descriptor in the array is used to group the objects into sections; its key must either be the same as   or the relative ordering using its key must match that using  .
- `context`: The managed object against which   is executed.
- `sectionNameKeyPath`: If this key path is not the same as that specified by the first sort descriptor in  , they must generate the same relative orderings. For example, the first sort descriptor in   might specify the key for a persistent property;   might specify a key for a transient property derived from the persistent property.
- `name`: Pre-computed section info is cached to a private directory under this name. If Core Data finds a cache stored with this name, it is checked to see if it matches the  . If it does, the cache is loaded directly—this avoids the overhead of computing the section and index information. If the cached information doesn’t match the request, the cache is deleted and recomputed when the fetch happens.

## See Also

- [Core Data Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [func performFetch() throws](nsfetchedresultscontroller/performfetch.md)
  Executes the controller’s fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/init(fetchrequest:managedobjectcontext:sectionnamekeypath:cachename:))*