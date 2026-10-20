# objectIDs(forRelationshipNamed:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the object IDs for all of the managed objects that are in the named relationship.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func objectIDs(forRelationshipNamed key: String) -> [NSManagedObjectID]
```

```objc
- (NSArray<NSManagedObjectID *> *) objectIDsForRelationshipNamed:(NSString *) key;
```

## See Also

### Supporting Key-Value Coding
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value for the property specified by `key`.
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Sets the specified property of the managed object to the specified value.
- [func primitiveValue(forKey: String) -> Any?](./primitivevalue%28forkey%29.md)
  Returns the value for the specified property from the managed object’s private internal storage .
- [func setPrimitiveValue(Any?, forKey: String)](./setprimitivevalue%28_,forkey%29.md)
  Sets the value of a given property in the managed object’s private internal storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/objectids(forrelationshipnamed:))*