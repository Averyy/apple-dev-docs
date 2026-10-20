# addObjects(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds to the set each object contained in a given array that is not already a member.

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
func addObjects(from array: [Any])
```

```objc
- (void) addObjectsFromArray:(NSArray<id> *) array;
```

## Parameters

- `array`: An array of objects to add to the set.

## See Also

### Related Documentation
- [func union(Set<AnyHashable>)](./union%28_%29.md)
  Adds each object in another given set to the receiving set, if not present.
### Adding and removing entries
- [func add(Any)](./add%28_%29.md)
  Adds a given object to the set, if it is not already a member.
- [func filter(using: NSPredicate)](./filter%28using%29.md)
  Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [func remove(Any)](./remove%28_%29.md)
  Removes a given object from the set.
- [func removeAllObjects()](./removeallobjects%28%29.md)
  Empties the set of all of its members.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/addobjects(from:))*