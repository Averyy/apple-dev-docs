# method_getNumberOfArguments(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns the number of arguments accepted by a method.

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
func method_getNumberOfArguments(_ m: Method) -> UInt32
```

```c
extern unsigned int method_getNumberOfArguments(Method m);
```

## Return Value

An integer containing the number of arguments accepted by the given method.

## Parameters

- `m`: A pointer to a [`Method`](./method.md) data structure. Pass the method in question.

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
- [func method_getArgumentType(Method, UInt32, UnsafeMutablePointer<CChar>?, Int)](./method_getargumenttype%28_,_,_,_%29.md)
  Returns by reference a string describing a single parameter type of a method.
- [func method_getDescription(Method) -> UnsafeMutablePointer<objc_method_description>](./method_getdescription%28_%29.md)
  Returns a method description structure for a specified method.
- [func method_setImplementation(Method, IMP) -> IMP](./method_setimplementation%28_,_%29.md)
  Sets the implementation of a method.
- [func method_exchangeImplementations(Method, Method)](./method_exchangeimplementations%28_,_%29.md)
  Exchanges the implementations of two methods.
- [method_invoke](./method_invoke.md)
  Calls the implementation of a specified method.
- [method_invoke_stret](./method_invoke_stret.md)
  Calls the implementation of a specified method that returns a data-structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/method_getnumberofarguments(_:))*