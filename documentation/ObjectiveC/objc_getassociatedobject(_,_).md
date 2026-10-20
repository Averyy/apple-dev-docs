# objc_getAssociatedObject(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns the value associated with a given object for a given key.

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
func objc_getAssociatedObject(_ object: Any, _ key: UnsafeRawPointer) -> Any?
```

```c
extern idobjc_getAssociatedObject(id object, const void *key);
```

#### Return Value

The value associated with the key `key` for `object`.

## Parameters

- `object`: The source object for the association.
- `key`: The key for the association.

## See Also

### Associative References
- [func objc_setAssociatedObject(Any, UnsafeRawPointer, Any?, objc_AssociationPolicy)](./objc_setassociatedobject%28_,_,_,_%29.md)
  Sets an associated value for a given object using a given key and association policy.
- [func objc_removeAssociatedObjects(Any)](./objc_removeassociatedobjects%28_%29.md)
  Removes all associations for a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_getassociatedobject(_:_:))*