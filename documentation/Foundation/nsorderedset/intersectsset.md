# intersectsSet(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given set.

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
func intersectsSet(_ set: Set<AnyHashable>) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if at least one object in the receiving ordered set is also present in `other`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `set`: The set.

## See Also

- [func isEqual(to: NSOrderedSet) -> Bool](nsorderedset/isequal(to:).md)
  Compares the receiving ordered set to another ordered set.
- [func intersects(NSOrderedSet) -> Bool](nsorderedset/intersects(_:).md)
  Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given ordered set.
- [func isSubset(of: NSOrderedSet) -> Bool](nsorderedset/issubset(of:)-7brc.md)
  Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given ordered set.
- [func isSubset(of: Set<AnyHashable>) -> Bool](nsorderedset/issubset(of:)-8zx9x.md)
  Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/intersectsset(_:))*