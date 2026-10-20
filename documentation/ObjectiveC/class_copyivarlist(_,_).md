# class_copyIvarList(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Describes the instance variables declared by a class.

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
func class_copyIvarList(_ cls: AnyClass?, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<Ivar>?
```

```c
extern Ivar*class_copyIvarList(Class cls, unsigned int *outCount);
```

#### Return Value

An array of pointers of type Ivar describing the instance variables declared by the class. Any instance variables declared by superclasses are not included. The array contains `*outCount` pointers followed by a `NULL` terminator. You must free the array with `free()`.

If the class declares no instance variables, or `cls` is `Nil`, `NULL` is returned and `*outCount` is `0`.

## Parameters

- `cls`: The class to inspect.
- `outCount`: On return, contains the length of the returned array. If `outCount` is `NULL`, the length is not returned.

## See Also

### Working with Classes
- [func class_getName(AnyClass?) -> UnsafePointer<CChar>](./class_getname%28_%29.md)
  Returns the name of a class.
- [func class_getSuperclass(AnyClass?) -> AnyClass?](./class_getsuperclass%28_%29.md)
  Returns the superclass of a class.
- [func class_setSuperclass(AnyClass, AnyClass) -> AnyClass](./class_setsuperclass%28_,_%29.md)
  Sets the superclass of a given class.
- [func class_isMetaClass(AnyClass?) -> Bool](./class_ismetaclass%28_%29.md)
  Returns a Boolean value that indicates whether a class object is a metaclass.
- [func class_getInstanceSize(AnyClass?) -> Int](./class_getinstancesize%28_%29.md)
  Returns the size of instances of a class.
- [func class_getInstanceVariable(AnyClass?, UnsafePointer<CChar>) -> Ivar?](./class_getinstancevariable%28_,_%29.md)
  Returns the `Ivar` for a specified instance variable of a given class.
- [func class_getClassVariable(AnyClass?, UnsafePointer<CChar>) -> Ivar?](./class_getclassvariable%28_,_%29.md)
  Returns the `Ivar` for a specified class variable of a given class.
- [func class_addIvar(AnyClass?, UnsafePointer<CChar>, Int, UInt8, UnsafePointer<CChar>?) -> Bool](./class_addivar%28_,_,_,_,_%29.md)
  Adds a new instance variable to a class.
- [func class_getIvarLayout(AnyClass?) -> UnsafePointer<UInt8>?](./class_getivarlayout%28_%29.md)
  Returns a description of the `Ivar` layout for a given class.
- [func class_setIvarLayout(AnyClass?, UnsafePointer<UInt8>?)](./class_setivarlayout%28_,_%29.md)
  Sets the `Ivar` layout for a given class.
- [func class_getWeakIvarLayout(AnyClass?) -> UnsafePointer<UInt8>?](./class_getweakivarlayout%28_%29.md)
  Returns a description of the layout of weak `Ivar`s for a given class.
- [func class_setWeakIvarLayout(AnyClass?, UnsafePointer<UInt8>?)](./class_setweakivarlayout%28_,_%29.md)
  Sets the layout for weak `Ivar`s for a given class.
- [func class_getProperty(AnyClass?, UnsafePointer<CChar>) -> objc_property_t?](./class_getproperty%28_,_%29.md)
  Returns a property with a given name of a given class.
- [func class_copyPropertyList(AnyClass?, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_t>?](./class_copypropertylist%28_,_%29.md)
  Describes the properties declared by a class.
- [func class_addMethod(AnyClass?, Selector, IMP, UnsafePointer<CChar>?) -> Bool](./class_addmethod%28_,_,_,_%29.md)
  Adds a new method to a class with a given name and implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/class_copyivarlist(_:_:))*