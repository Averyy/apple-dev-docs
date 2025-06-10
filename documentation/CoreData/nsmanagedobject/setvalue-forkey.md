# setValue(_:forKey:)

**Framework**: Core Data  
**Kind**: method

Sets the specified property of the managed object to the specified value.

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
func setValue(_ value: Any?, forKey key: String)
```

#### Discussion

If `key` is not a property defined by the model, the method raises an exception. If `key` identifies a to-one relationship, relates the object specified by `value` to the receiver, unrelating the previously related object if there was one. Given a collection object and a key that identifies a to-many relationship, relates the objects contained in the collection to the receiver, unrelating previously related objects if there were any.

This method is overridden by `NSManagedObject` to access the managed object’s generic dictionary storage unless the receiver’s class explicitly provides key-value coding compliant accessor methods for `key`.

> ❗ **Important**:  You must not override this method.

## Parameters

- `value`: The new value for the property specified by  .
- `key`: The name of one of the receiver’s properties.

## See Also

- [func setObservationInfo(UnsafeMutableRawPointer?)](nsmanagedobject/setobservationinfo(_:).md)
  Sets the observation info of the managed object.
- [func value(forKey: String) -> Any?](nsmanagedobject/value(forkey:).md)
  Returns the value for the property specified by `key`.
- [func primitiveValue(forKey: String) -> Any?](nsmanagedobject/primitivevalue(forkey:).md)
  Returns the value for the specified property from the managed object’s private internal storage .
- [func setPrimitiveValue(Any?, forKey: String)](nsmanagedobject/setprimitivevalue(_:forkey:).md)
  Sets the value of a given property in the managed object’s private internal storage.
- [func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]](nsmanagedobject/objectids(forrelationshipnamed:).md)
  Returns the object IDs for all of the managed objects that are in the named relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/setvalue(_:forkey:))*