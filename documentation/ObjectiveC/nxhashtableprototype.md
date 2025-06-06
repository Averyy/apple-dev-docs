# NXHashTablePrototype

**Framework**: Objective-C Runtime  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct NXHashTablePrototype
```

## Topics

### Initializers
- [init(hash: (UnsafeRawPointer?, UnsafeRawPointer?) -> UInt, isEqual: (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32, free: (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void, style: Int32)](nxhashtableprototype/init(hash:isequal:free:style:).md)
### Instance Properties
- [var free: (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void](nxhashtableprototype/free.md)
- [var hash: (UnsafeRawPointer?, UnsafeRawPointer?) -> UInt](nxhashtableprototype/hash.md)
- [var isEqual: (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32](nxhashtableprototype/isequal.md)
- [var style: Int32](nxhashtableprototype/style.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct NSZone](nszone.md)
- [struct ObjCBool](objcbool.md)
- [struct ObjCClassList](objcclasslist.md)
- [struct Selector](selector.md)
- [struct objc_method_description](objc_method_description.md)
  Defines an Objective-C method.
- [struct objc_object](objc_object.md)
  Represents an instance of a class.
- [struct objc_property_attribute_t](objc_property_attribute_t.md)
  Defines a property attribute.
- [struct objc_super](objc_super-swift.struct.md)
  Specifies the superclass of an instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nxhashtableprototype)*