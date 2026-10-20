# removeAllObjects()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Empties the set of all of its members.

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
func removeAllObjects()
```

```objc
- (void) removeAllObjects;
```

## See Also

### Related Documentation
- [func minus(Set<AnyHashable>)](./minus%28_%29.md)
  Removes each object in another given set from the receiving set, if present.
- [func intersect(Set<AnyHashable>)](./intersect%28_%29.md)
  Removes from the receiving set each object that isn’t a member of another given set.
### Adding and removing entries
- [func add(Any)](./add%28_%29.md)
  Adds a given object to the set, if it is not already a member.
- [func filter(using: NSPredicate)](./filter%28using%29.md)
  Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [func remove(Any)](./remove%28_%29.md)
  Removes a given object from the set.
- [func addObjects(from: [Any])](./addobjects%28from%29.md)
  Adds to the set each object contained in a given array that is not already a member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/removeallobjects())*