# class_addIvar(_:_:_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Adds a new instance variable to a class.

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
func class_addIvar(_ cls: AnyClass?, _ name: UnsafePointer<CChar>, _ size: Int, _ alignment: UInt8, _ types: UnsafePointer<CChar>?) -> Bool
```

#### Return Value

[`YES`](yes.md) if the instance variable was added successfully, otherwise [`NO`](no.md) (for example, the class already contains an instance variable with that name).

#### Discussion

This function may only be called after [`objc_allocateClassPair(_:_:_:)`](objc_allocateclasspair(_:_:_:).md) and before [`objc_registerClassPair(_:)`](objc_registerclasspair(_:).md). Adding an instance variable to an existing class is not supported.

The class must not be a metaclass. Adding an instance variable to a metaclass is not supported.

The instance variable’s minimum alignment in bytes is `1<<align`. The minimum alignment of an instance variable depends on the ivar’s type and the machine architecture. For variables of any pointer type, pass `log2(sizeof(pointer_type))`.

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
- [func class_copyPropertyList(AnyClass?, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_t>?](class_copypropertylist(_:_:).md)
  Describes the properties declared by a class.
- [func class_addMethod(AnyClass?, Selector, IMP, UnsafePointer<CChar>?) -> Bool](class_addmethod(_:_:_:_:).md)
  Adds a new method to a class with a given name and implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/class_addivar(_:_:_:_:_:))*