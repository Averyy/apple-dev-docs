# configurationName(forStoreIdentifier:)

**Framework**: SwiftData  
**Kind**: method

Returns the configuration name associated with the given on-disk store identifier.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Swift 5.9+

## Declaration

```swift
func configurationName(forStoreIdentifier identifier: String) -> String?
```

#### Return Value

The `name` of the `ModelConfiguration` that backs the given store, or `nil` if no store with that identifier exists in this container or if `invalidate()` has been called.

#### Discussion

Use this when you already have a store identifier — such as `PersistentIdentifier.storeIdentifier` from a fetched object or a store identifier from a history transaction — and need to map it back to the human-readable configuration name that produced that store.

## Parameters

- `identifier`: A store identifier string, for example from `PersistentIdentifier.storeIdentifier` or a history transaction’s store identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontainer/configurationname(forstoreidentifier:))*