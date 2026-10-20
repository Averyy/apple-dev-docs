# value(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.

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
func value(forKey key: String) -> Any
```

```objc
- (id) valueForKey:(NSString *) key;
```

#### Return Value

A set containing the results of invoking `valueForKey:` (with the argument `key`) on each of the receiving set’s members.

#### Discussion

The returned set might not have the same number of members as the receiving set. The returned set will not contain any elements corresponding to instances of `valueForKey:` returning `nil` (note that this is in contrast with `NSArray`’s implementation, which may put `NSNull` values in the arrays it returns).

## Parameters

- `key`: The name of one of the properties of the receiving set’s members.

## See Also

### Comparing Sets
- [func isSubset(of: Set<AnyHashable>) -> Bool](./issubset%28of%29.md)
  Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [func intersects(Set<AnyHashable>) -> Bool](./intersects%28_%29.md)
  Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [func isEqual(to: Set<AnyHashable>) -> Bool](./isequal%28to%29.md)
  Compares the receiving set to another set.
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Invokes `setValue:forKey:` on each of the set’s members.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/value(forkey:))*