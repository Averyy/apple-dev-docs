# relationshipKeyPathsForPrefetching

**Framework**: Core Data  
**Kind**: property

The relationship key paths to prefetch along with the entity for the request.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var relationshipKeyPathsForPrefetching: [String]? { get set }
```

#### Discussion

This property is an array of relationship key-path strings in NSKeyValueCoding notation (as you typically use with [`value(forKeyPath:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/value(forKeyPath:))). The default value is an empty array (no prefetching).

Prefetching allows Core Data to obtain related objects in a single fetch (per entity), rather than incurring subsequent access to the store for each individual record as their faults are tripped. For example, given an Employee entity with a relationship to a Department entity, suppose you fetch all the employees, and then for each print out their name and the name of the department to which they belong. In this case, a fault might be fired for each individual Department object. This can represent a significant overhead. You can avoid this by prefetching the department relationship in the Employee fetch, as illustrated in Listing 1.

(For more details, see Core Data Performance in Core Data Programming Guide)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/relationshipkeypathsforprefetching)*