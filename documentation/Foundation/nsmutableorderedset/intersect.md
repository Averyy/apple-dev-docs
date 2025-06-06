# intersect(_:)

**Framework**: Foundation  
**Kind**: method

Removes from the receiving ordered set each object that isn’t a member of another ordered set.

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
func intersect(_ other: NSOrderedSet)
```

## Parameters

- `other`: The ordered set with which to perform the intersection.

## See Also

- [func intersectSet(Set<AnyHashable>)](nsmutableorderedset/intersectset(_:).md)
  Removes from the receiving ordered set each object that isn’t a member of another set.
- [func minus(NSOrderedSet)](nsmutableorderedset/minus(_:).md)
  Removes each object in another given ordered set from the receiving mutable ordered set, if present.
- [func minusSet(Set<AnyHashable>)](nsmutableorderedset/minusset(_:).md)
  Removes each object in another given set from the receiving mutable ordered set, if present.
- [func union(NSOrderedSet)](nsmutableorderedset/union(_:).md)
  Adds each object in another given ordered set to the receiving mutable ordered set, if not present.
- [func unionSet(Set<AnyHashable>)](nsmutableorderedset/unionset(_:).md)
  Adds each object in another given set to the receiving mutable ordered set, if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/intersect(_:))*