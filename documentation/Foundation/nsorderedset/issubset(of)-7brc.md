# isSubset(of:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given ordered set.

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
func isSubset(of other: NSOrderedSet) -> Bool
```

```objc
- (BOOL) isSubsetOfOrderedSet:(NSOrderedSet<id> *) other;
```

#### Return Value

[`true`](../../Swift/true.md) if every object in the receiving set is also present in `other`, otherwise [`false`](../../Swift/false.md).

## Parameters

- `other`: The ordered set with which to compare the receiving ordered set.

## See Also

### Comparing Sets
- [func isEqual(to: NSOrderedSet) -> Bool](./isequal%28to%29.md)
  Compares the receiving ordered set to another ordered set.
- [func intersects(NSOrderedSet) -> Bool](./intersects%28_%29.md)
  Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given ordered set.
- [func intersectsSet(Set<AnyHashable>) -> Bool](./intersectsset%28_%29.md)
  Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given set.
- [func isSubset(of: Set<AnyHashable>) -> Bool](./issubset%28of%29-8zx9x.md)
  Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/issubset(of:)-7brc)*