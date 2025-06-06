# remove(_:)

**Framework**: Foundation  
**Kind**: method

Removes a given object from the set.

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
func remove(_ object: Any)
```

## Parameters

- `object`: The object to remove from the set.

## See Also

- [func minus(Set<AnyHashable>)](nsmutableset/minus(_:).md)
  Removes each object in another given set from the receiving set, if present.
- [func intersect(Set<AnyHashable>)](nsmutableset/intersect(_:).md)
  Removes from the receiving set each object that isn’t a member of another given set.
- [func add(Any)](nsmutableset/add(_:).md)
  Adds a given object to the set, if it is not already a member.
- [func filter(using: NSPredicate)](nsmutableset/filter(using:).md)
  Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [func removeAllObjects()](nsmutableset/removeallobjects.md)
  Empties the set of all of its members.
- [func addObjects(from: [Any])](nsmutableset/addobjects(from:).md)
  Adds to the set each object contained in a given array that is not already a member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/remove(_:))*