# willChange(_:valuesAt:forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Informs the observed object that the specified change is about to be executed at given indexes for a specified ordered to-many relationship.

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
func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)
```

```objc
- (void) willChange:(NSKeyValueChange) changeKind valuesAtIndexes:(NSIndexSet *) indexes forKey:(NSString *) key;
```

## Discussion

Use this method when implementing key-value-observing compliance manually.

> ❗ **Important**:  After the values have been changed, a corresponding [`didChange(_:valuesAt:forKey:)`](./didchange%28_,valuesat,forkey%29.md) must be invoked with the same parameters.

### Special Considerations

You rarely need to override this method in subclasses, but if you do, be sure to call `super`.

## Parameters

- `changeKind`: The type of change that is about to be made.
- `indexes`: The indexes of the to-many relationship that will be affected by the change.
- `key`: The name of a property that is an ordered to-many relationship.

## See Also

### Notifying Observers of Changes
- [func willChangeValue(forKey: String)](./willchangevalue%28forkey%29.md)
  Informs the observed object that the value of a given property is about to change.
- [func didChangeValue(forKey: String)](./didchangevalue%28forkey%29.md)
  Informs the observed object that the value of a given property has changed.
- [func didChange(NSKeyValueChange, valuesAt: IndexSet, forKey: String)](./didchange%28_,valuesat,forkey%29.md)
  Informs the observed object that the specified change has occurred on the indexes for a specified ordered to-many relationship.
- [func willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./willchangevalue%28forkey,withsetmutation,using%29.md)
  Informs the observed object that the specified change is about to be made to a specified unordered to-many relationship.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./didchangevalue%28forkey,withsetmutation,using%29.md)
  Informs the observed object that the specified change was made to a specified unordered to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/willchange(_:valuesat:forkey:))*