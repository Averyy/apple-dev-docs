# filter(using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) filterUsingPredicate:(NSPredicate *) predicate;
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

### Adding and removing entries
- [func add(Any)](./add%28_%29.md)
  Adds a given object to the set, if it is not already a member.
- [func remove(Any)](./remove%28_%29.md)
  Removes a given object from the set.
- [func removeAllObjects()](./removeallobjects%28%29.md)
  Empties the set of all of its members.
- [func addObjects(from: [Any])](./addobjects%28from%29.md)
  Adds to the set each object contained in a given array that is not already a member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/filter(using:))*