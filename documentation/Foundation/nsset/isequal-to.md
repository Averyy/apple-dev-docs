# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

Compares the receiving set to another set.

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
func isEqual(to otherSet: Set<AnyHashable>) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the contents of `otherSet` are equal to the contents of the receiving set, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Two sets have equal contents if they each have the same number of members and if each member of one set is present in the other. Object equality is tested using isEqual:.

## Parameters

- `otherSet`: The set with which to compare the receiving set.

## See Also

- [func isEqual(_ object: Any?) -> Bool](../ObjectiveC/NSObjectProtocol/isEqual(_:).md)
  Returns a Boolean value that indicates whether the receiver and a given object are equal.
- [func isSubset(of: Set<AnyHashable>) -> Bool](nsset/issubset(of:).md)
  Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [func intersects(Set<AnyHashable>) -> Bool](nsset/intersects(_:).md)
  Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [func value(forKey: String) -> Any](nsset/value(forkey:).md)
  Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.
- [func setValue(Any?, forKey: String)](nsset/setvalue(_:forkey:).md)
  Invokes `setValue:forKey:` on each of the set’s members.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/isequal(to:))*