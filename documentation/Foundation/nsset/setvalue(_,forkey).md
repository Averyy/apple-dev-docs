# setValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setValue:(id) value forKey:(NSString *) key;
```

## Parameters

- `value`: The value for the property identified by `key`.
- `key`: The name of one of the properties of the set’s members.

## See Also

### Comparing Sets
- [func isSubset(of: Set<AnyHashable>) -> Bool](./issubset%28of%29.md)
  Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [func intersects(Set<AnyHashable>) -> Bool](./intersects%28_%29.md)
  Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [func isEqual(to: Set<AnyHashable>) -> Bool](./isequal%28to%29.md)
  Compares the receiving set to another set.
- [func value(forKey: String) -> Any](./value%28forkey%29.md)
  Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/setvalue(_:forkey:))*