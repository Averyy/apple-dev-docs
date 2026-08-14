# NSFetchRequest

**Framework**: Core Data  
**Kind**: class

A description of search criteria used to retrieve data from a persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSFetchRequest<ResultType> where ResultType : NSFetchRequestResult
```

#### Overview

An instance of [`NSFetchRequest`](nsfetchrequest.md) collects the criteria needed to select and optionally to sort a group of [`NSManagedObject`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/Cocoa/CoreDataReleaseNotes/index.html#//apple_ref/doc/uid/TP40006503-SW6) managed objects held in an [`NSPersistentStore`](nspersistentstore.md) persistent store. A fetch request contains an [`NSEntityDescription`](nsentitydescription.md) or an entity name that specifies which entity to search. It frequently also contains:

- An [`NSPredicate`](https://developer.apple.com/documentation/foundation/nspredicate) predicate that specifies which properties to filter by and the constraints on selection, such as, `“last name begins with a ‘J’”`. If you don’t specify a predicate, then the system fetches all instances of the entity that you specified, subject to other constraints. For more information, see [`fetch(_:)`](nsmanagedobjectcontext/fetch(_:)-38ys1.md).
- An array of [`NSSortDescriptor`](https://developer.apple.com/documentation/foundation/nssortdescriptor) sort descriptors that specify how to order the returned objects, such as ascending by last name and then by first name.

You can also specify other aspects of a fetch request:

- **[`fetchLimit`](nsfetchrequest/fetchlimit.md)**: The maximum number of objects that a request returns
- **[`fetchOffset`](nsfetchrequest/fetchoffset.md)**: The number of objects to skip
- **[`affectedStores`](nsfetchrequest/affectedstores.md)**: Which data stores the request accesses
- **[`resultType`](nsfetchrequest/resulttype.md)**: Whether the fetch returns managed objects, object IDs, dictionaries, or a count
- **[`includesPropertyValues`](nsfetchrequest/includespropertyvalues.md) and**: Whether objects are fully populated with their properties
- **[`returnsObjectsAsFaults`](nsfetchrequest/returnsobjectsasfaults.md)**: Whether the objects are faults
- **[`includesSubentities`](nsfetchrequest/includessubentities.md)**: Whether the fetch includes subentities of the fetched entity
- **[`propertiesToFetch`](nsfetchrequest/propertiestofetch.md)**: Which properties to fetch
- **[`includesPendingChanges`](nsfetchrequest/includespendingchanges.md)**: Whether to include unsaved changes

Use [`execute()`](nsfetchrequest/execute().md) to perform the fetch directly on the managed object context that’s associated with the current queue. Or use one of the [`NSManagedObjectContext`](nsmanagedobjectcontext.md) methods such as [`perform(_:)`](nsmanagedobjectcontext/perform(_:).md) to execute the fetch.

> **Note**:  When you execute an instance of [`NSFetchRequest`](nsfetchrequest.md), it always accesses the underlying persistent stores to retrieve the latest results.

In [`SwiftUI`](https://developer.apple.com/documentation/swiftui), you can use a [`FetchRequest`](https://developer.apple.com/documentation/swiftui/fetchrequest) property wrapper to execute the fetch and assign the results to a property. First, create the request:

```swift
let request: NSFetchRequest = {
    // Create a fetch request.
    let request = ShoppingItem.fetchRequest()
    
    // Limit the maximum number of items that the request returns.
    request.fetchLimit = 100
            
    // Filter the request results, such as to only return unchecked items.
    request.predicate = NSPredicate(format: "isChecked = false")
    
    // Sort the fetched results, such as ascending by name.
    request.sortDescriptors = [NSSortDescriptor(keyPath: \ShoppingItem.name, ascending: true)]

    return request
}()
```

Then use a [`FetchRequest`](https://developer.apple.com/documentation/swiftui/fetchrequest) property wrapper with the request to declare a property that receives the objects that the fetch returns:

```swift
// Use a `FetchRequest` property wrapper to fetch the managed objects
// and assign the result.
@FetchRequest(fetchRequest: request) private var items: FetchedResults<ShoppingItem>
```

> 💡 **Tip**:  If you don’t need to specify multiple properties of the fetch, you can avoid creating the fetch request separately and declare it in the property wrapper instead. See [`FetchRequest`](https://developer.apple.com/documentation/swiftui/fetchrequest) for more information.

You often predefine fetch requests in an [`NSManagedObjectModel`](nsmanagedobjectmodel.md) managed object model to provide an API to retrieve a stored fetch request by name. Stored fetch requests can include placeholders for variable substitution, and serve as templates for later completion. Fetch request templates allow you to predefine queries with variables to substitute at runtime.

## Topics

### Managing the Fetch Request’s Entity
- [convenience init(entityName: String)](nsfetchrequest/init(entityname:)-5anoo.md)
  Returns a fetch request configured with a given entity name.
- [init()](nsfetchrequest/init.md)
  Creates a new fetch request.
- [var entityName: String?](nsfetchrequest/entityname.md)
  The name of the entity the request is configured to fetch.
- [var entity: NSEntityDescription?](nsfetchrequest/entity.md)
  The entity specified for the fetch request.
- [var includesSubentities: Bool](nsfetchrequest/includessubentities.md)
  A Boolean value that indicates whether the fetch request includes subentities in the results.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.
### Specifying Fetch Constraints
- [var predicate: NSPredicate?](nsfetchrequest/predicate.md)
  The predicate of the fetch request.
- [var fetchLimit: Int](nsfetchrequest/fetchlimit.md)
  The fetch limit of the fetch request.
- [var fetchOffset: Int](nsfetchrequest/fetchoffset.md)
  The fetch offset of the fetch request.
- [var fetchBatchSize: Int](nsfetchrequest/fetchbatchsize.md)
  The batch size of the objects specified in the fetch request.
- [var affectedStores: [NSPersistentStore]?](nsfetchrequest/affectedstores.md)
  An array of persistent stores specified for the fetch request.
- [class NSFetchRequestExpression](nsfetchrequestexpression.md)
  An expression that evaluates the result of a fetch request on a managed object context.
- [class NSExpressionDescription](nsexpressiondescription.md)
  An object that describes an expression to include with a fetch request.
- [class NSFetchedPropertyDescription](nsfetchedpropertydescription.md)
  A description object used to define which properties are fetched from Core Data.
### Sorting the Results
- [var sortDescriptors: [NSSortDescriptor]?](nsfetchrequest/sortdescriptors.md)
  The sort descriptors of the fetch request.
### Prefetching Related Objects
- [var relationshipKeyPathsForPrefetching: [String]?](nsfetchrequest/relationshipkeypathsforprefetching.md)
  The relationship key paths to prefetch along with the entity for the request.
### Managing How Results Are Returned
- [var resultType: NSFetchRequestResultType](nsfetchrequest/resulttype.md)
  The result type of the fetch request.
- [var includesPendingChanges: Bool](nsfetchrequest/includespendingchanges.md)
  A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [var propertiesToFetch: [Any]?](nsfetchrequest/propertiestofetch.md)
  A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [var returnsDistinctResults: Bool](nsfetchrequest/returnsdistinctresults.md)
  A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [`propertiesToFetch`](nsfetchrequest/propertiestofetch.md).
- [var includesPropertyValues: Bool](nsfetchrequest/includespropertyvalues.md)
  A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [var shouldRefreshRefetchedObjects: Bool](nsfetchrequest/shouldrefreshrefetchedobjects.md)
  A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [var returnsObjectsAsFaults: Bool](nsfetchrequest/returnsobjectsasfaults.md)
  A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.
- [protocol NSFetchRequestResult](nsfetchrequestresult.md)
  An abstract protocol used with parameterized fetch requests.
### Grouping and Filtering Dictionary Results
- [var propertiesToGroupBy: [Any]?](nsfetchrequest/propertiestogroupby.md)
  An array of objects that indicates how data should be grouped before a select statement is run in a SQL database.
- [var havingPredicate: NSPredicate?](nsfetchrequest/havingpredicate.md)
  The predicate used to filter rows being returned by a query containing a GROUP BY directive.
### Executing a Fetch Request Directly
- [func execute() throws -> [ResultType]](nsfetchrequest/execute.md)
  Executes the fetch request against the managed object context that is associated with the current queue.
### Initializers
- [init?(coder: NSCoder)](nsfetchrequest/init(coder:).md)
- [convenience init(entityName: String)](nsfetchrequest/init(entityname:)-yd3.md)

## Relationships

### Inherits From
- [NSPersistentStoreRequest](nspersistentstorerequest.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class NSAsynchronousFetchRequest](nsasynchronousfetchrequest.md)
  A fetch request that retrieves results asynchronously and supports progress notification.
- [class NSAsynchronousFetchResult](nsasynchronousfetchresult.md)
  A fetch result object that encompasses the response from an executed asynchronous fetch request.
- [class NSFetchedResultsController](nsfetchedresultscontroller.md)
  A controller that you use to manage the results of a Core Data fetch request and to display data to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest)*