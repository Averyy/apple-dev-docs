# registeredModel(for:)

**Framework**: SwiftData  
**Kind**: method

Returns the typed model for the specified identifier.

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
func registeredModel<T>(for persistentModelID: PersistentIdentifier) -> T? where T : PersistentModel
```

#### Return Value

A typed instance of the identified model, if known to the context; otherwise, `nil`.

## Parameters

- `persistentModelID`: The identifier of the model to fetch. For more information, see  .

## See Also

- [func fetch<T>(FetchDescriptor<T>) throws -> [T]](modelcontext/fetch(_:).md)
  Returns an array of typed models that match the criteria of the specified fetch descriptor.
- [func fetch<T>(FetchDescriptor<T>, batchSize: Int) throws -> FetchResultsCollection<T>](modelcontext/fetch(_:batchsize:).md)
  Returns a collection of typed models, in batches, which match the criteria of the specified fetch descriptor.
- [func fetchCount<T>(FetchDescriptor<T>) throws -> Int](modelcontext/fetchcount(_:).md)
  Returns the number of models that match the criteria of the specified fetch descriptor.
- [struct FetchDescriptor](fetchdescriptor.md)
  A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
- [struct FetchResultsCollection](fetchresultscollection.md)
  A collection that efficiently provides the results of a completed fetch.
- [func enumerate<T>(FetchDescriptor<T>, batchSize: Int, allowEscapingMutations: Bool, block: (T) throws -> Void) throws](modelcontext/enumerate(_:batchsize:allowescapingmutations:block:).md)
  Runs a closure for each model that matches the criteria of the specified fetch descriptor.
- [func model(for: PersistentIdentifier) -> any PersistentModel](modelcontext/model(for:).md)
  Returns the persistent model for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/registeredmodel(for:))*