# intersect(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) intersectOrderedSet:(NSOrderedSet<id> *) other;
```

## Parameters

- `other`: The ordered set with which to perform the intersection.

## See Also

### Combining and Recombining Entries
- [func intersectSet(Set<AnyHashable>)](./intersectset%28_%29.md)
  Removes from the receiving ordered set each object that isn’t a member of another set.
- [func minus(NSOrderedSet)](./minus%28_%29.md)
  Removes each object in another given ordered set from the receiving mutable ordered set, if present.
- [func minusSet(Set<AnyHashable>)](./minusset%28_%29.md)
  Removes each object in another given set from the receiving mutable ordered set, if present.
- [func union(NSOrderedSet)](./union%28_%29.md)
  Adds each object in another given ordered set to the receiving mutable ordered set, if not present.
- [func unionSet(Set<AnyHashable>)](./unionset%28_%29.md)
  Adds each object in another given set to the receiving mutable ordered set, if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/intersect(_:))*