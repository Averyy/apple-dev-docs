# class_getClassMethod(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns a pointer to the data structure describing a given class method for a given class.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func class_getClassMethod(_ cls: AnyClass?, _ name: Selector) -> Method?
```

```c
extern Methodclass_getClassMethod(Class cls, SEL name);
```

## Return Value

A pointer to the [`Method`](./method.md) data structure that corresponds to the implementation of the selector specified by `aSelector` for the class specified by `aClass`, or `NULL` if the specified class or its superclasses do not contain a class method with the specified selector.

## Discussion

Note that this function searches superclasses for implementations, whereas [`class_copyMethodList(_:_:)`](./class_copymethodlist%28_,_%29.md) does not.

## Parameters

- `cls`: A pointer to a class definition. Pass the class that contains the method you want to retrieve.
- `name`: A pointer of type [`SEL`](./sel.md). Pass the selector of the method you want to retrieve.

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
- [func class_copyIvarList(AnyClass?, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<Ivar>?](./class_copyivarlist%28_,_%29.md)
  Describes the instance variables declared by a class.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/class_getclassmethod(_:_:))*