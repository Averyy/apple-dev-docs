# willChangeValue(forKey:withSetMutation:using:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Informs the observed object that the specified change is about to be made to a specified unordered to-many relationship.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)
```

```objc
- (void) willChangeValueForKey:(NSString *) key withSetMutation:(NSKeyValueSetMutationKind) mutationKind usingObjects:(NSSet *) objects;
```

## Discussion

Use this method when implementing key-value observer compliance manually.

> ❗ **Important**:  After the values have been changed, a corresponding [`didChangeValue(forKey:withSetMutation:using:)`](./didchangevalue%28forkey,withsetmutation,using%29.md) must be invoked with the same parameters.

### Special Considerations

You rarely need to override this method in subclasses, but if you do, be sure to call `super`.

## Parameters

- `key`: The name of a property that is an unordered to-many relationship
- `mutationKind`: The type of change that will be made.
- `objects`: The objects that are involved in the change (see [`NSKeyValueSetMutationKind`](../../Foundation/nskeyvaluesetmutationkind.md)).

## See Also

### Notifying Observers of Changes
- [func willChangeValue(forKey: String)](./willchangevalue%28forkey%29.md)
  Informs the observed object that the value of a given property is about to change.
- [func didChangeValue(forKey: String)](./didchangevalue%28forkey%29.md)
  Informs the observed object that the value of a given property has changed.
- [func willChange(NSKeyValueChange, valuesAt: IndexSet, forKey: String)](./willchange%28_,valuesat,forkey%29.md)
  Informs the observed object that the specified change is about to be executed at given indexes for a specified ordered to-many relationship.
- [func didChange(NSKeyValueChange, valuesAt: IndexSet, forKey: String)](./didchange%28_,valuesat,forkey%29.md)
  Informs the observed object that the specified change has occurred on the indexes for a specified ordered to-many relationship.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./didchangevalue%28forkey,withsetmutation,using%29.md)
  Informs the observed object that the specified change was made to a specified unordered to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/willchangevalue(forkey:withsetmutation:using:))*