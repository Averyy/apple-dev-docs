# setObservationInfo(_:)

**Framework**: Core Data  
**Kind**: method

Sets the observation info of the managed object.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func setObservationInfo(_ inObservationInfo: UnsafeMutableRawPointer?)
```

#### Discussion

For more about observation information, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## Parameters

- `inObservationInfo`: The new observation info for the receiver.

## See Also

- [func didAccessValue(forKey: String?)](nsmanagedobject/didaccessvalue(forkey:).md)
  Provides support for key-value observing access notification.
- [func observationInfo() -> UnsafeMutableRawPointer?](nsmanagedobject/observationinfo.md)
  Returns the observation info of the managed object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/setobservationinfo(_:))*