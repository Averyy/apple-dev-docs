# isSubset(of:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given set.

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
func isSubset(of set: Set<AnyHashable>) -> Bool
```

```objc
- (BOOL) isSubsetOfSet:(NSSet<id> *) set;
```

## Return Value

[`true`](../../Swift/true.md) if every object in the receiving ordered set is also present in `set`, otherwise [`false`](../../Swift/false.md).

## Parameters

- `set`: The set with which to compare the receiving ordered set.

## See Also

### Comparing Sets
- [func isEqual(to: NSOrderedSet) -> Bool](./isequal%28to%29.md)
  Compares the receiving ordered set to another ordered set.
- [func intersects(NSOrderedSet) -> Bool](./intersects%28_%29.md)
  Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given ordered set.
- [func intersectsSet(Set<AnyHashable>) -> Bool](./intersectsset%28_%29.md)
  Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given set.
- [func isSubset(of: NSOrderedSet) -> Bool](./issubset%28of%29-7brc.md)
  Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given ordered set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/issubset(of:)-8zx9x)*