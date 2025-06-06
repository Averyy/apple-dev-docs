# observationInfo()

**Framework**: Core Data  
**Kind**: method

Returns the observation info of the managed object.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func observationInfo() -> UnsafeMutableRawPointer?
```

#### Return Value

The observation info of the receiver.

#### Discussion

For more about key-value observation, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

> ❗ **Important**:  You must not override this method.

 You must not override this method.

## See Also

- [func didAccessValue(forKey: String?)](nsmanagedobject/didaccessvalue(forkey:).md)
  Provides support for key-value observing access notification.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/observationinfo())*