# willAccessValue(forKey:)

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
func willAccessValue(forKey key: String?)
```

#### Discussion

See [`didAccessValue(forKey:)`](nsmanagedobject/didaccessvalue(forkey:).md) for more details. You can invoke this method with the `key` value of `nil` to ensure that a fault has been fired, as illustrated by the following example.

```objc
[aManagedObject willAccessValueForKey:nil];
```

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

- [func didAccessValue(forKey: String?)](nsmanagedobject/didaccessvalue(forkey:).md)
  Provides support for key-value observing access notification.
- [func observationInfo() -> UnsafeMutableRawPointer?](nsmanagedobject/observationinfo.md)
  Returns the observation info of the managed object.
- [func setObservationInfo(UnsafeMutableRawPointer?)](nsmanagedobject/setobservationinfo(_:).md)
  Sets the observation info of the managed object.
- [func didChangeValue(forKey: String)](nsmanagedobject/didchangevalue(forkey:).md)
  Provides an opportunity to respond when a value of a given property has changed.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsmanagedobject/didchangevalue(forkey:withsetmutation:using:).md)
  Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [func willChangeValue(forKey: String)](nsmanagedobject/willchangevalue(forkey:).md)
  Provides an opportunity to respond when a value of a given property is about to change.
- [func willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsmanagedobject/willchangevalue(forkey:withsetmutation:using:).md)
  Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/willaccessvalue(forkey:))*