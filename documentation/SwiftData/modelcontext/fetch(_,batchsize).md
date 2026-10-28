# fetch(_:batchSize:)

**Framework**: SwiftData  
**Kind**: method  
**Role**: Instance Method

Returns a collection of typed models, in batches, which match the criteria of the specified fetch descriptor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
func fetch<T>(_ descriptor: FetchDescriptor<T>, batchSize: Int) throws -> FetchResultsCollection<T> where T : PersistentModel
```

## Return Value

The collection of typed models that satisfy the criteria of the fetch descriptor. If no models match the criteria, the collection is empty.

## Discussion

As you access the models in the returned collection (either sequentially, or directly using subscripting), the context automatically fetches the necessary batches.

## Parameters

- `descriptor`: A fetch descriptor that provides the configuration for the fetch.
- `batchSize`: The maximum number of models to include in each batch.

## See Also

### Fetching models
- [func fetch<T>(FetchDescriptor<T>) throws -> [T]](./fetch%28_%29.md)
  Returns an array of typed models that match the criteria of the specified fetch descriptor.
- [func fetchCount<T>(FetchDescriptor<T>) throws -> Int](./fetchcount%28_%29.md)
  Returns the number of models that match the criteria of the specified fetch descriptor.
- [struct FetchDescriptor](../fetchdescriptor.md)
  A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
- [struct FetchResultsCollection](../fetchresultscollection.md)
  A collection that efficiently provides the results of a completed fetch.
- [func enumerate<T>(FetchDescriptor<T>, batchSize: Int, allowEscapingMutations: Bool, block: (T) throws -> Void) throws](./enumerate%28_,batchsize,allowescapingmutations,block%29.md)
  Runs a closure for each model that matches the criteria of the specified fetch descriptor.
- [func model(for: PersistentIdentifier) -> any PersistentModel](./model%28for%29.md)
  Returns the persistent model for the specified identifier.
- [func registeredModel<T>(for: PersistentIdentifier) -> T?](./registeredmodel%28for%29.md)
  Returns the typed model for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/fetch(_:batchsize:))*