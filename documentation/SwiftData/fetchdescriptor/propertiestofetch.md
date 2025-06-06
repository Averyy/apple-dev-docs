# propertiesToFetch

**Framework**: SwiftData  
**Kind**: property

The specific subset of attributes to fetch if you don’t require them all.

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
var propertiesToFetch: [PartialKeyPath<T>]
```

#### Discussion

If you know ahead of time that you’re going to process (or display) a subset of a model’s attributes, use this property to provide the key paths of those attributes. When the fetch runs, it’ll return values for only the specified key paths, which may result in faster and more efficient fetches. However, if you subsequently access a nonfetched attribute, you’ll incur the additional overhead of fetching the corresponding value from the persistent storage.

> **Note**: An empty array causes the fetch to include all attributes, not none.

An empty array causes the fetch to include all attributes, not none.

The default value is an empty array.

## See Also

- [var relationshipKeyPathsForPrefetching: [PartialKeyPath<T>]](fetchdescriptor/relationshipkeypathsforprefetching.md)
  The key paths that identify any related models to include as part of the fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchdescriptor/propertiestofetch)*