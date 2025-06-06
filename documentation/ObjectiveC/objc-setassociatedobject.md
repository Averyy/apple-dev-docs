# objc_setAssociatedObject(_:_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Sets an associated value for a given object using a given key and association policy.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func objc_setAssociatedObject(_ object: Any, _ key: UnsafeRawPointer, _ value: Any?, _ policy: objc_AssociationPolicy)
```

## Parameters

- `object`: The source object for the association.
- `key`: The key for the association.
- `value`: The value to associate with the key   for  . Pass   to clear an existing association.
- `policy`: The policy for the association. For possible values, see  .

## See Also

- [func objc_getAssociatedObject(Any, UnsafeRawPointer) -> Any?](objc_getassociatedobject(_:_:).md)
  Returns the value associated with a given object for a given key.
- [func objc_removeAssociatedObjects(Any)](objc_removeassociatedobjects(_:).md)
  Removes all associations for a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_setassociatedobject(_:_:_:_:))*