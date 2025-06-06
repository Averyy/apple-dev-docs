# intersect(_:)

**Framework**: Foundation  
**Kind**: method

Removes from the receiving set each object that isn’t a member of another given set.

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
func intersect(_ otherSet: Set<AnyHashable>)
```

## Parameters

- `otherSet`: The set with which to perform the intersection.

## See Also

- [func remove(Any)](nsmutableset/remove(_:).md)
  Removes a given object from the set.
- [func removeAllObjects()](nsmutableset/removeallobjects.md)
  Empties the set of all of its members.
- [func union(Set<AnyHashable>)](nsmutableset/union(_:).md)
  Adds each object in another given set to the receiving set, if not present.
- [func minus(Set<AnyHashable>)](nsmutableset/minus(_:).md)
  Removes each object in another given set from the receiving set, if present.
- [func setSet(Set<AnyHashable>)](nsmutableset/setset(_:).md)
  Empties the receiving set, then adds each object contained in another given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/intersect(_:))*