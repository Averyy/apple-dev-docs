# isSubset(of:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.

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
func isSubset(of otherSet: Set<AnyHashable>) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if every object in the receiving set is also present in `otherSet`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Object equality is tested using isEqual:.

## Parameters

- `otherSet`: The set with which to compare the receiving set.

## See Also

- [func intersects(Set<AnyHashable>) -> Bool](nsset/intersects(_:).md)
  Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [func isEqual(to: Set<AnyHashable>) -> Bool](nsset/isequal(to:).md)
  Compares the receiving set to another set.
- [func value(forKey: String) -> Any](nsset/value(forkey:).md)
  Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.
- [func setValue(Any?, forKey: String)](nsset/setvalue(_:forkey:).md)
  Invokes `setValue:forKey:` on each of the set’s members.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/issubset(of:))*