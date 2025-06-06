# didChangeValue(forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Informs the observed object that the value of a given property has changed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func didChangeValue(forKey key: String)
```

#### Discussion

Use this method when implementing key-value observer compliance manually to inform the observed object that the value at `key` has just changed. Calls to this method are always paired with a matching call to [`willChangeValue(forKey:)`](nsobject-swift.class/willchangevalue(forkey:).md).

##### Special Considerations

You rarely need to override this method in subclasses, but if you do, be sure to call `super`.

## Parameters

- `key`: The name of the property that changed.

## See Also

- [func willChangeValue(forKey: String)](nsobject-swift.class/willchangevalue(forkey:).md)
  Informs the observed object that the value of a given property is about to change.
- [func willChange(NSKeyValueChange, valuesAt: IndexSet, forKey: String)](nsobject-swift.class/willchange(_:valuesat:forkey:).md)
  Informs the observed object that the specified change is about to be executed at given indexes for a specified ordered to-many relationship.
- [func didChange(NSKeyValueChange, valuesAt: IndexSet, forKey: String)](nsobject-swift.class/didchange(_:valuesat:forkey:).md)
  Informs the observed object that the specified change has occurred on the indexes for a specified ordered to-many relationship.
- [func willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsobject-swift.class/willchangevalue(forkey:withsetmutation:using:).md)
  Informs the observed object that the specified change is about to be made to a specified unordered to-many relationship.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsobject-swift.class/didchangevalue(forkey:withsetmutation:using:).md)
  Informs the observed object that the specified change was made to a specified unordered to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/didchangevalue(forkey:))*