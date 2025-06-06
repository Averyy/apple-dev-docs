# enumerate(_:batchSize:allowEscapingMutations:block:)

**Framework**: SwiftData  
**Kind**: method

Runs a closure for each model that matches the criteria of the specified fetch descriptor.

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
func enumerate<T>(_ fetch: FetchDescriptor<T>, batchSize: Int = 5000, allowEscapingMutations: Bool = false, block: (T) throws -> Void) throws where T : PersistentModel
```

## Parameters

- `fetch`: A fetch descriptor that provides the configuration for the fetch.
- `batchSize`: The maximum number of models to include in each batch. The default value is 5000.
- `allowEscapingMutations`: A Boolean value that determines whether the closure can leave the context in a modified state after it completes. The default value is  .
- `block`: The closure to run for each fetched model.

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
- [func model(for: PersistentIdentifier) -> any PersistentModel](modelcontext/model(for:).md)
  Returns the persistent model for the specified identifier.
- [func registeredModel<T>(for: PersistentIdentifier) -> T?](modelcontext/registeredmodel(for:).md)
  Returns the typed model for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/enumerate(_:batchsize:allowescapingmutations:block:))*