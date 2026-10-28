# didChangeValue(forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Informs the observed object that the value of a given property has changed.

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
func didChangeValue(forKey key: String)
```

```objc
- (void) didChangeValueForKey:(NSString *) key;
```

## Discussion

Use this method when implementing key-value observer compliance manually to inform the observed object that the value at `key` has just changed. Calls to this method are always paired with a matching call to [`willChangeValue(forKey:)`](./willchangevalue%28forkey%29.md).

### Special Considerations

You rarely need to override this method in subclasses, but if you do, be sure to call `super`.

## Parameters

- `key`: The name of the property that changed.

## See Also

### Notifying Observers of Changes
- [func willChangeValue(forKey: String)](./willchangevalue%28forkey%29.md)
  Informs the observed object that the value of a given property is about to change.
- [func willChange(NSKeyValueChange, valuesAt: IndexSet, forKey: String)](./willchange%28_,valuesat,forkey%29.md)
  Informs the observed object that the specified change is about to be executed at given indexes for a specified ordered to-many relationship.
- [func didChange(NSKeyValueChange, valuesAt: IndexSet, forKey: String)](./didchange%28_,valuesat,forkey%29.md)
  Informs the observed object that the specified change has occurred on the indexes for a specified ordered to-many relationship.
- [func willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./willchangevalue%28forkey,withsetmutation,using%29.md)
  Informs the observed object that the specified change is about to be made to a specified unordered to-many relationship.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./didchangevalue%28forkey,withsetmutation,using%29.md)
  Informs the observed object that the specified change was made to a specified unordered to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/didchangevalue(forkey:))*