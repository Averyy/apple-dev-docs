# class_copyPropertyList(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Describes the properties declared by a class.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func class_copyPropertyList(_ cls: AnyClass?, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_t>?
```

#### Return Value

An array of pointers of type `objc_property_t` describing the properties declared by the class. Any properties declared by superclasses are not included. The array contains `*outCount` pointers followed by a `NULL` terminator. You must free the array with `free()`.

If `cls` declares no properties, or `cls` is `Nil`, returns `NULL` and `*outCount` is `0`.

## Parameters

- `cls`: The class you want to inspect.
- `outCount`: On return, contains the length of the returned array. If   is  , the length is not returned.

## See Also

- [func class_getName(AnyClass?) -> UnsafePointer<CChar>](class_getname(_:).md)
  Returns the name of a class.
- [func class_getSuperclass(AnyClass?) -> AnyClass?](class_getsuperclass(_:).md)
  Returns the superclass of a class.
- [func class_setSuperclass(AnyClass, AnyClass) -> AnyClass](class_setsuperclass(_:_:).md)
  Sets the superclass of a given class.
- [func class_isMetaClass(AnyClass?) -> Bool](class_ismetaclass(_:).md)
  Returns a Boolean value that indicates whether a class object is a metaclass.
- [func class_getInstanceSize(AnyClass?) -> Int](class_getinstancesize(_:).md)
  Returns the size of instances of a class.
- [func class_getInstanceVariable(AnyClass?, UnsafePointer<CChar>) -> Ivar?](class_getinstancevariable(_:_:).md)
  Returns the `Ivar` for a specified instance variable of a given class.
- [func class_getClassVariable(AnyClass?, UnsafePointer<CChar>) -> Ivar?](class_getclassvariable(_:_:).md)
  Returns the `Ivar` for a specified class variable of a given class.
- [func class_addIvar(AnyClass?, UnsafePointer<CChar>, Int, UInt8, UnsafePointer<CChar>?) -> Bool](class_addivar(_:_:_:_:_:).md)
  Adds a new instance variable to a class.
- [func class_copyIvarList(AnyClass?, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<Ivar>?](class_copyivarlist(_:_:).md)
  Describes the instance variables declared by a class.
- [func class_getIvarLayout(AnyClass?) -> UnsafePointer<UInt8>?](class_getivarlayout(_:).md)
  Returns a description of the `Ivar` layout for a given class.
- [func class_setIvarLayout(AnyClass?, UnsafePointer<UInt8>?)](class_setivarlayout(_:_:).md)
  Sets the `Ivar` layout for a given class.
- [func class_getWeakIvarLayout(AnyClass?) -> UnsafePointer<UInt8>?](class_getweakivarlayout(_:).md)
  Returns a description of the layout of weak `Ivar`s for a given class.
- [func class_setWeakIvarLayout(AnyClass?, UnsafePointer<UInt8>?)](class_setweakivarlayout(_:_:).md)
  Sets the layout for weak `Ivar`s for a given class.
- [func class_getProperty(AnyClass?, UnsafePointer<CChar>) -> objc_property_t?](class_getproperty(_:_:).md)
  Returns a property with a given name of a given class.
- [func class_addMethod(AnyClass?, Selector, IMP, UnsafePointer<CChar>?) -> Bool](class_addmethod(_:_:_:_:).md)
  Adds a new method to a class with a given name and implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/class_copypropertylist(_:_:))*