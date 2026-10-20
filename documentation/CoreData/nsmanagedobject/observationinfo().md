# observationInfo()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void *) observationInfo;
```

#### Return Value

The observation info of the receiver.

#### Discussion

For more about key-value observation, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

> ❗ **Important**:  You must not override this method.

## See Also

### Supporting Key-Value Observing
- [func didAccessValue(forKey: String?)](./didaccessvalue%28forkey%29.md)
  Provides support for key-value observing access notification.
- [func setObservationInfo(UnsafeMutableRawPointer?)](./setobservationinfo%28_%29.md)
  Sets the observation info of the managed object.
- [func willAccessValue(forKey: String?)](./willaccessvalue%28forkey%29.md)
  Provides support for key-value observing access notification.
- [func didChangeValue(forKey: String)](./didchangevalue%28forkey%29.md)
  Provides an opportunity to respond when a value of a given property has changed.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./didchangevalue%28forkey,withsetmutation,using%29.md)
  Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [func willChangeValue(forKey: String)](./willchangevalue%28forkey%29.md)
  Provides an opportunity to respond when a value of a given property is about to change.
- [func willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./willchangevalue%28forkey,withsetmutation,using%29.md)
  Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/observationinfo())*