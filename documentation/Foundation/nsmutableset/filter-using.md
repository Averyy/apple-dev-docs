# filter(using:)

**Framework**: Foundation  
**Kind**: method

Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func filter(using predicate: NSPredicate)
```

#### Discussion

The following example illustrates the use of this method.

```objc
NSMutableSet *mutableSet =
    [NSMutableSet setWithObjects:@"One", @"Two", @"Three", @"Four", nil];
NSPredicate *predicate =
    [NSPredicate predicateWithFormat:@"SELF beginswith 'T'"];
[mutableSet filterUsingPredicate:predicate];
// mutableSet contains (Two, Three)
```

## Parameters

- `predicate`: A predicate.

## See Also

- [func add(Any)](nsmutableset/add(_:).md)
  Adds a given object to the set, if it is not already a member.
- [func remove(Any)](nsmutableset/remove(_:).md)
  Removes a given object from the set.
- [func removeAllObjects()](nsmutableset/removeallobjects.md)
  Empties the set of all of its members.
- [func addObjects(from: [Any])](nsmutableset/addobjects(from:).md)
  Adds to the set each object contained in a given array that is not already a member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/filter(using:))*