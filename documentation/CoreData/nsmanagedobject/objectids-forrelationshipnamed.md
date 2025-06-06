# objectIDs(forRelationshipNamed:)

**Framework**: Core Data  
**Kind**: method

Returns the object IDs for all of the managed objects that are in the named relationship.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func objectIDs(forRelationshipNamed key: String) -> [NSManagedObjectID]
```

## See Also

- [func value(forKey: String) -> Any?](nsmanagedobject/value(forkey:).md)
  Returns the value for the property specified by `key`.
- [func setValue(Any?, forKey: String)](nsmanagedobject/setvalue(_:forkey:).md)
  Sets the specified property of the managed object to the specified value.
- [func primitiveValue(forKey: String) -> Any?](nsmanagedobject/primitivevalue(forkey:).md)
  Returns the value for the specified property from the managed object’s private internal storage .
- [func setPrimitiveValue(Any?, forKey: String)](nsmanagedobject/setprimitivevalue(_:forkey:).md)
  Sets the value of a given property in the managed object’s private internal storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/objectids(forrelationshipnamed:))*