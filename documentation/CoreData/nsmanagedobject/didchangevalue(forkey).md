# didChangeValue(forKey:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to respond when a value of a given property has changed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func didChangeValue(forKey key: String)
```

```objc
- (void) didChangeValueForKey:(NSString *) key;
```

#### Discussion

For more details, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

You must not override this method.

## Parameters

- `key`: The name of the property that changed.

## See Also

### Supporting Key-Value Observing
- [func didAccessValue(forKey: String?)](./didaccessvalue%28forkey%29.md)
  Provides support for key-value observing access notification.
- [func observationInfo() -> UnsafeMutableRawPointer?](./observationinfo%28%29.md)
  Returns the observation info of the managed object.
- [func setObservationInfo(UnsafeMutableRawPointer?)](./setobservationinfo%28_%29.md)
  Sets the observation info of the managed object.
- [func willAccessValue(forKey: String?)](./willaccessvalue%28forkey%29.md)
  Provides support for key-value observing access notification.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./didchangevalue%28forkey,withsetmutation,using%29.md)
  Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [func willChangeValue(forKey: String)](./willchangevalue%28forkey%29.md)
  Provides an opportunity to respond when a value of a given property is about to change.
- [func willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./willchangevalue%28forkey,withsetmutation,using%29.md)
  Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/didchangevalue(forkey:))*