# didAccessValue(forKey:)

**Framework**: Core Data  
**Kind**: method

Provides support for key-value observing access notification.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func didAccessValue(forKey key: String?)
```

#### Discussion

Together with [`willAccessValue(forKey:)`](nsmanagedobject/willaccessvalue(forkey:).md), this method is used to fire faults, to maintain inverse relationships, and so on. Each read access must be wrapped in this method pair (in the same way that each write access must be wrapped in the `willChangeValueForKey:`/`didChangeValueForKey:` method pair). In the default implementation of `NSManagedObject` these methods are invoked for you automatically. If, say, you create a custom subclass that uses explicit instance variables, you must invoke them yourself, as in the following example.

```objc
- (NSString *)firstName
{
    [self willAccessValueForKey:@"firstName"];
    NSString *rtn = firstName;
    [self didAccessValueForKey:@"firstName"];
    return rtn;
}
```

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

- [func observationInfo() -> UnsafeMutableRawPointer?](nsmanagedobject/observationinfo.md)
  Returns the observation info of the managed object.
- [func setObservationInfo(UnsafeMutableRawPointer?)](nsmanagedobject/setobservationinfo(_:).md)
  Sets the observation info of the managed object.
- [func willAccessValue(forKey: String?)](nsmanagedobject/willaccessvalue(forkey:).md)
  Provides support for key-value observing access notification.
- [func didChangeValue(forKey: String)](nsmanagedobject/didchangevalue(forkey:).md)
  Provides an opportunity to respond when a value of a given property has changed.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsmanagedobject/didchangevalue(forkey:withsetmutation:using:).md)
  Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [func willChangeValue(forKey: String)](nsmanagedobject/willchangevalue(forkey:).md)
  Provides an opportunity to respond when a value of a given property is about to change.
- [func willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsmanagedobject/willchangevalue(forkey:withsetmutation:using:).md)
  Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/didaccessvalue(forkey:))*