# willChangeValue(forKey:withSetMutation:using:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.

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
func willChangeValue(forKey inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, using inObjects: Set<AnyHashable>)
```

```objc
- (void) willChangeValueForKey:(NSString *) inKey withSetMutation:(NSKeyValueSetMutationKind) inMutationKind usingObjects:(NSSet *) inObjects;
```

## Discussion

For more details, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

You must not override this method.

## Parameters

- `inKey`: The name of a property that is a to-many relationship
- `inMutationKind`: The type of change that will be made.
- `inObjects`: The objects that were involved in the change (see [`NSKeyValueSetMutationKind`](../../Foundation/nskeyvaluesetmutationkind.md)).

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
- [func didChangeValue(forKey: String)](./didchangevalue%28forkey%29.md)
  Provides an opportunity to respond when a value of a given property has changed.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](./didchangevalue%28forkey,withsetmutation,using%29.md)
  Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [func willChangeValue(forKey: String)](./willchangevalue%28forkey%29.md)
  Provides an opportunity to respond when a value of a given property is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/willchangevalue(forkey:withsetmutation:using:))*