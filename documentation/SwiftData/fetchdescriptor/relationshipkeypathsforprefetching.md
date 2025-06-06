# relationshipKeyPathsForPrefetching

**Framework**: SwiftData  
**Kind**: property

The key paths that identify any related models to include as part of the fetch.

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
var relationshipKeyPathsForPrefetching: [PartialKeyPath<T>]
```

#### Discussion

Prefetching enables SwiftData to obtain any related models in a single fetch, instead of incurring subsequent access to the persistent storage as you access each related model.

For example, given an `Employee` model with a relationship to a `Department` model, and suppose you fetch all employees as you want to display both their name and the name of the department where they work. In such a scenario, the model context may need to perform additional fetches for each individual department, resulting in significant overhead. You can avoid this by prefetching the department relationship as part of the employee fetch.

The default value is an empty array.

## See Also

- [var propertiesToFetch: [PartialKeyPath<T>]](fetchdescriptor/propertiestofetch.md)
  The specific subset of attributes to fetch if you don’t require them all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchdescriptor/relationshipkeypathsforprefetching)*