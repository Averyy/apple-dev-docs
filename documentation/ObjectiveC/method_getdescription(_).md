# method_getDescription(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns a method description structure for a specified method.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.5+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 8.0

> **Deprecated**: Use method_getName and method_getTypeEncoding.

## Declaration

```swift
func method_getDescription(_ m: Method) -> UnsafeMutablePointer<objc_method_description>
```

```c
extern struct objc_method_description *method_getDescription(Method m);
```

#### Return Value

An `objc_method_description` structure that describes the method specified by `m`.

## Parameters

- `m`: The method you want to inquire about.

## See Also

### Working with Methods
- [func method_getName(Method) -> Selector](./method_getname%28_%29.md)
  Returns the name of a method.
- [func method_getImplementation(Method) -> IMP](./method_getimplementation%28_%29.md)
  Returns the implementation of a method.
- [func method_getTypeEncoding(Method) -> UnsafePointer<CChar>?](./method_gettypeencoding%28_%29.md)
  Returns a string describing a method’s parameter and return types.
- [func method_copyReturnType(Method) -> UnsafeMutablePointer<CChar>](./method_copyreturntype%28_%29.md)
  Returns a string describing a method’s return type.
- [func method_copyArgumentType(Method, UInt32) -> UnsafeMutablePointer<CChar>?](./method_copyargumenttype%28_,_%29.md)
  Returns a string describing a single parameter type of a method.
- [func method_getReturnType(Method, UnsafeMutablePointer<CChar>, Int)](./method_getreturntype%28_,_,_%29.md)
  Returns by reference a string describing a method’s return type.
- [func method_getNumberOfArguments(Method) -> UInt32](./method_getnumberofarguments%28_%29.md)
  Returns the number of arguments accepted by a method.
- [func method_getArgumentType(Method, UInt32, UnsafeMutablePointer<CChar>?, Int)](./method_getargumenttype%28_,_,_,_%29.md)
  Returns by reference a string describing a single parameter type of a method.
- [func method_setImplementation(Method, IMP) -> IMP](./method_setimplementation%28_,_%29.md)
  Sets the implementation of a method.
- [func method_exchangeImplementations(Method, Method)](./method_exchangeimplementations%28_,_%29.md)
  Exchanges the implementations of two methods.
- [method_invoke](./method_invoke.md)
  Calls the implementation of a specified method.
- [method_invoke_stret](./method_invoke_stret.md)
  Calls the implementation of a specified method that returns a data-structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/method_getdescription(_:))*