# fetchIdentifiers(_:)

**Framework**: SwiftData  
**Kind**: method

Returns an array of persistent identifiers, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.

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
func fetchIdentifiers<T>(_ descriptor: FetchDescriptor<T>) throws -> [PersistentIdentifier] where T : PersistentModel
```

#### Return Value

The array of persistent identifiers. If no models match the descriptor’s criteria, the array is empty.

## Parameters

- `descriptor`: A fetch descriptor that provides the configuration for the fetch.

## See Also

- [func fetchIdentifiers<T>(FetchDescriptor<T>, batchSize: Int) throws -> FetchResultsCollection<PersistentIdentifier>](modelcontext/fetchidentifiers(_:batchsize:).md)
  Returns a collection of persistent identifiers, in batches, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/fetchidentifiers(_:))*