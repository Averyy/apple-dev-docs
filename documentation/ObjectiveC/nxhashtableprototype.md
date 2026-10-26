# NXHashTablePrototype

**Framework**: Objective-C Runtime  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct NXHashTablePrototype
```

```c
typedef struct { ... } NXHashTablePrototype;
```

## Topics

### Initializers
- [init(hash: (UnsafeRawPointer?, UnsafeRawPointer?) -> UInt, isEqual: (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32, free: (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void, style: Int32)](./nxhashtableprototype/init%28hash,isequal,free,style%29.md)
### Instance Properties
- [var free: (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void](./nxhashtableprototype/free.md)
- [var hash: (UnsafeRawPointer?, UnsafeRawPointer?) -> UInt](./nxhashtableprototype/hash.md)
- [var isEqual: (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32](./nxhashtableprototype/isequal.md)
- [var style: Int32](./nxhashtableprototype/style.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Structures
- [struct NSZone](./nszone.md)
- [struct ObjCBool](./objcbool.md)
- [struct ObjCClassList](./objcclasslist.md)
- [struct Selector](./selector.md)
- [struct objc_method_description](./objc_method_description.md)
  Defines an Objective-C method.
- [struct objc_object](./objc_object.md)
  Represents an instance of a class.
- [struct objc_property_attribute_t](./objc_property_attribute_t.md)
  Defines a property attribute.
- [struct objc_super](./objc_super-swift.struct.md)
  Specifies the superclass of an instance.
- [NXHashState](./nxhashstate.md)
- [NXHashTable](./nxhashtable.md)
- [id](./id.md)
  A pointer to an instance of a class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nxhashtableprototype)*