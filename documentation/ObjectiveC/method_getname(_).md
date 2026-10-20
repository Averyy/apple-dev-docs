# method_getName(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns the name of a method.

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
func method_getName(_ m: Method) -> Selector
```

```c
extern SELmethod_getName(Method m);
```

#### Return Value

A pointer of type SEL.

#### Discussion

To get the method name as a C string, call `sel_getName(method_getName(method))`.

## Parameters

- `m`: The method to inspect.

## See Also

### Working with Methods
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
- [func method_getDescription(Method) -> UnsafeMutablePointer<objc_method_description>](./method_getdescription%28_%29.md)
  Returns a method description structure for a specified method.
- [func method_setImplementation(Method, IMP) -> IMP](./method_setimplementation%28_,_%29.md)
  Sets the implementation of a method.
- [func method_exchangeImplementations(Method, Method)](./method_exchangeimplementations%28_,_%29.md)
  Exchanges the implementations of two methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/method_getname(_:))*