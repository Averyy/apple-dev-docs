# fetchCount(_:)

**Framework**: SwiftData  
**Kind**: method

Returns the number of models that match the criteria of the specified fetch descriptor.

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
func fetchCount<T>(_ descriptor: FetchDescriptor<T>) throws -> Int where T : PersistentModel
```

#### Return Value

The total number of models that satisfy the criteria of the fetch descriptor.

## Parameters

- `descriptor`: A fetch descriptor that provides the configuration for the fetch.

## See Also

- [func fetch<T>(FetchDescriptor<T>) throws -> [T]](modelcontext/fetch(_:).md)
  Returns an array of typed models that match the criteria of the specified fetch descriptor.
- [func fetch<T>(FetchDescriptor<T>, batchSize: Int) throws -> FetchResultsCollection<T>](modelcontext/fetch(_:batchsize:).md)
  Returns a collection of typed models, in batches, which match the criteria of the specified fetch descriptor.
- [struct FetchDescriptor](fetchdescriptor.md)
  A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
- [struct FetchResultsCollection](fetchresultscollection.md)
  A collection that efficiently provides the results of a completed fetch.
- [func enumerate<T>(FetchDescriptor<T>, batchSize: Int, allowEscapingMutations: Bool, block: (T) throws -> Void) throws](modelcontext/enumerate(_:batchsize:allowescapingmutations:block:).md)
  Runs a closure for each model that matches the criteria of the specified fetch descriptor.
- [func model(for: PersistentIdentifier) -> any PersistentModel](modelcontext/model(for:).md)
  Returns the persistent model for the specified identifier.
- [func registeredModel<T>(for: PersistentIdentifier) -> T?](modelcontext/registeredmodel(for:).md)
  Returns the typed model for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/fetchcount(_:))*