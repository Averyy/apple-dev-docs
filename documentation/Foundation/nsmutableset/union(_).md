# union(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds each object in another given set to the receiving set, if not present.

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
func union(_ otherSet: Set<AnyHashable>)
```

```objc
- (void) unionSet:(NSSet<id> *) otherSet;
```

## Parameters

- `otherSet`: The set of objects to add to the receiving set.

## See Also

### Related Documentation
- [func add(Any)](./add%28_%29.md)
  Adds a given object to the set, if it is not already a member.
- [func addObjects(from: [Any])](./addobjects%28from%29.md)
  Adds to the set each object contained in a given array that is not already a member.
### Combining and recombining sets
- [func minus(Set<AnyHashable>)](./minus%28_%29.md)
  Removes each object in another given set from the receiving set, if present.
- [func intersect(Set<AnyHashable>)](./intersect%28_%29.md)
  Removes from the receiving set each object that isn’t a member of another given set.
- [func setSet(Set<AnyHashable>)](./setset%28_%29.md)
  Empties the receiving set, then adds each object contained in another given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/union(_:))*