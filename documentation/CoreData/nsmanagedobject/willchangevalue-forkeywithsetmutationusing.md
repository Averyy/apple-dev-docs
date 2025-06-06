# willChangeValue(forKey:withSetMutation:using:)

**Framework**: Core Data  
**Kind**: method

Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.

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
func willChangeValue(forKey inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, using inObjects: Set<AnyHashable>)
```

#### Discussion

For more details, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

You must not override this method.

## Parameters

- `inKey`: The name of a property that is a to-many relationship
- `inMutationKind`: The type of change that will be made.
- `inObjects`: The objects that were involved in the change (see  ).

## See Also

- [func didAccessValue(forKey: String?)](nsmanagedobject/didaccessvalue(forkey:).md)
  Provides support for key-value observing access notification.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/willchangevalue(forkey:withsetmutation:using:))*