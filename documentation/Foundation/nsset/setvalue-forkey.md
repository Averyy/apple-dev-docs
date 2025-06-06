# setValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Invokes `setValue:forKey:` on each of the set’s members.

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
func setValue(_ value: Any?, forKey key: String)
```

## Parameters

- `value`: The value for the property identified by  .
- `key`: The name of one of the properties of the set’s members.

## See Also

- [func isSubset(of: Set<AnyHashable>) -> Bool](nsset/issubset(of:).md)
  Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [func intersects(Set<AnyHashable>) -> Bool](nsset/intersects(_:).md)
  Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [func isEqual(to: Set<AnyHashable>) -> Bool](nsset/isequal(to:).md)
  Compares the receiving set to another set.
- [func value(forKey: String) -> Any](nsset/value(forkey:).md)
  Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/setvalue(_:forkey:))*