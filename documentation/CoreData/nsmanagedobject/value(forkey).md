# value(forKey:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the value for the property specified by `key`.

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
func value(forKey key: String) -> Any?
```

```objc
- (id) valueForKey:(NSString *) key;
```

#### Return Value

The value of the property specified by `key`.

#### Discussion

If `key` is not a property defined by the model, the method raises an exception. This method is overridden by `NSManagedObject` to access the managed object’s generic dictionary storage unless the receiver’s class explicitly provides key-value coding compliant accessor methods for `key`.

> ❗ **Important**:  You must not override this method.

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

### Related Documentation
- [func setObservationInfo(UnsafeMutableRawPointer?)](./setobservationinfo%28_%29.md)
  Sets the observation info of the managed object.
### Supporting Key-Value Coding
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Sets the specified property of the managed object to the specified value.
- [func primitiveValue(forKey: String) -> Any?](./primitivevalue%28forkey%29.md)
  Returns the value for the specified property from the managed object’s private internal storage .
- [func setPrimitiveValue(Any?, forKey: String)](./setprimitivevalue%28_,forkey%29.md)
  Sets the value of a given property in the managed object’s private internal storage.
- [func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]](./objectids%28forrelationshipnamed%29.md)
  Returns the object IDs for all of the managed objects that are in the named relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/value(forkey:))*