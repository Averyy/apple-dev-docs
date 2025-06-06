# class_addMethod(_:_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Adds a new method to a class with a given name and implementation.

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
func class_addMethod(_ cls: AnyClass?, _ name: Selector, _ imp: IMP, _ types: UnsafePointer<CChar>?) -> Bool
```

#### Return Value

[`YES`](yes.md) if the method was added successfully, otherwise [`NO`](no.md) (for example, the class already contains a method implementation with that name).

#### Discussion

[`class_addMethod(_:_:_:_:)`](class_addmethod(_:_:_:_:).md) will add an override of a superclass’s implementation, but will not replace an existing implementation in this class. To change an existing implementation, use [`method_setImplementation(_:_:)`](method_setimplementation(_:_:).md).

An Objective-C method is simply a C function that take at least two arguments—`self` and `_cmd`. For example, given the following function:

```objc
void myMethodIMP(id self, SEL _cmd)
{
    // implementation ....
}
```

you can dynamically add it to a class as a method (called `resolveThisMethodDynamically`) like this:

```objc
class_addMethod([self class], @selector(resolveThisMethodDynamically), (IMP) myMethodIMP, "v@:");
```

## Parameters

- `cls`: The class to which to add a method.
- `name`: A selector that specifies the name of the method being added.
- `imp`: A function which is the implementation of the new method. The function must take at least two arguments—  and  .
- `types`: An array of characters that describe the types of the arguments to the method. For possible values, see   >  . Since the function must take at least two arguments—  and  , the second and third characters must be “ ” (the first character is the return type).

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
- [func class_copyPropertyList(AnyClass?, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_t>?](class_copypropertylist(_:_:).md)
  Describes the properties declared by a class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/class_addmethod(_:_:_:_:))*