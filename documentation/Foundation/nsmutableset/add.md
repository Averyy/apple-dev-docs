# add(_:)

**Framework**: Foundation  
**Kind**: method

Adds a given object to the set, if it is not already a member.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func add(_ object: Any)
```

## Parameters

- `object`: The object to add to the set.

## See Also

- [func union(Set<AnyHashable>)](nsmutableset/union(_:).md)
  Adds each object in another given set to the receiving set, if not present.
- [func filter(using: NSPredicate)](nsmutableset/filter(using:).md)
  Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [func remove(Any)](nsmutableset/remove(_:).md)
  Removes a given object from the set.
- [func removeAllObjects()](nsmutableset/removeallobjects.md)
  Empties the set of all of its members.
- [func addObjects(from: [Any])](nsmutableset/addobjects(from:).md)
  Adds to the set each object contained in a given array that is not already a member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/add(_:))*