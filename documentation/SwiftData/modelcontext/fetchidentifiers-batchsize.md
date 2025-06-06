# fetchIdentifiers(_:batchSize:)

**Framework**: SwiftData  
**Kind**: method

Returns a collection of persistent identifiers, in batches, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.

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
func fetchIdentifiers<T>(_ descriptor: FetchDescriptor<T>, batchSize: Int) throws -> FetchResultsCollection<PersistentIdentifier> where T : PersistentModel
```

#### Return Value

The collection of persistent identifiers. If no models match the descriptor’s criteria, the array is empty.

#### Discussion

The collection automatically fetches subsequent batches as you iterate over the identifiers, or access one at a specific index.

## Parameters

- `descriptor`: A fetch descriptor that provides the configuration for the fetch.
- `batchSize`: The maximum number of identifiers to include in each batch.

## See Also

- [func fetchIdentifiers<T>(FetchDescriptor<T>) throws -> [PersistentIdentifier]](modelcontext/fetchidentifiers(_:).md)
  Returns an array of persistent identifiers, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/fetchidentifiers(_:batchsize:))*