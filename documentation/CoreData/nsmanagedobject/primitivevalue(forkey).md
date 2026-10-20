# primitiveValue(forKey:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the value for the specified property from the managed object’s private internal storage .

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
func primitiveValue(forKey key: String) -> Any?
```

```objc
- (id) primitiveValueForKey:(NSString *) key;
```

#### Return Value

The value of the property specified by `key`. Returns `nil` if no value has been set.

#### Discussion

This method does not invoke the access notification methods ([`willAccessValue(forKey:)`](./willaccessvalue%28forkey%29.md) and [`didAccessValue(forKey:)`](./didaccessvalue%28forkey%29.md)). This method is used primarily by subclasses that implement custom accessor methods that need direct access to the receiver’s private storage.

##### Special Considerations

Subclasses should not override this method.

The following points also apply:

- Primitive accessor methods are only supported on *modeled* properties. If you invoke a primitive accessor on an unmodeled property, it will instead operate upon a random modeled property. (The debug libraries and frameworks (available from [Apple Developer Website](http://developer.apple.com/)) have assertions to test for passing unmodeled keys to these methods.)
- You are strongly encouraged to use the dynamically-generated accessors rather than using this method directly (for example, `primitiveName:` instead of `primitiveValueForKey:@"name"`). The dynamic accessors are much more efficient, and allow for compile-time checking.

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

### Related Documentation
- [func setObservationInfo(UnsafeMutableRawPointer?)](./setobservationinfo%28_%29.md)
  Sets the observation info of the managed object.
### Supporting Key-Value Coding
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value for the property specified by `key`.
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Sets the specified property of the managed object to the specified value.
- [func setPrimitiveValue(Any?, forKey: String)](./setprimitivevalue%28_,forkey%29.md)
  Sets the value of a given property in the managed object’s private internal storage.
- [func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]](./objectids%28forrelationshipnamed%29.md)
  Returns the object IDs for all of the managed objects that are in the named relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/primitivevalue(forkey:))*