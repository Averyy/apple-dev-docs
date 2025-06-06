# objc_removeAssociatedObjects(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Removes all associations for a given object.

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
func objc_removeAssociatedObjects(_ object: Any)
```

#### Discussion

The main purpose of this function is to make it easy to return an object to a “pristine state”. You should not use this function for general removal of associations from objects, since it also removes associations that other clients may have added to the object. Typically you should use [`objc_setAssociatedObject(_:_:_:_:)`](objc_setassociatedobject(_:_:_:_:).md) with a `nil` value to clear an association.

## Parameters

- `object`: An object that maintains associated objects.

## See Also

- [func objc_setAssociatedObject(Any, UnsafeRawPointer, Any?, objc_AssociationPolicy)](objc_setassociatedobject(_:_:_:_:).md)
  Sets an associated value for a given object using a given key and association policy.
- [func objc_getAssociatedObject(Any, UnsafeRawPointer) -> Any?](objc_getassociatedobject(_:_:).md)
  Returns the value associated with a given object for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_removeassociatedobjects(_:))*