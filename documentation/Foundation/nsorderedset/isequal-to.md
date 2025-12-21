# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

Compares the receiving ordered set to another ordered set.

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
func isEqual(to other: NSOrderedSet) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the contents of `other` are equal to the contents of the receiving ordered set, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Two ordered sets have equal contents if they each have the same number of members, if each member of one ordered set is present in the other, and the members are in the same order.

## Parameters

- `other`: The ordered set with which to compare the receiving ordered set.

## See Also

- [func isEqual(Any?) -> Bool](../ObjectiveC/NSObjectProtocol/isEqual(_:).md)
  Returns a Boolean value that indicates whether the receiver and a given object are equal.
- [func intersects(NSOrderedSet) -> Bool](nsorderedset/intersects(_:).md)
  Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given ordered set.
- [func intersectsSet(Set<AnyHashable>) -> Bool](nsorderedset/intersectsset(_:).md)
  Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given set.
- [func isSubset(of: NSOrderedSet) -> Bool](nsorderedset/issubset(of:)-7brc.md)
  Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given ordered set.
- [func isSubset(of: Set<AnyHashable>) -> Bool](nsorderedset/issubset(of:)-8zx9x.md)
  Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/isequal(to:))*