# method_invoke_stret

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Calls the implementation of a specified method that returns a data-structure.

**Availability**:
- macOS 10.5+

## Declaration

```c
extern void method_invoke_stret();
```

#### Parameters

- **`receiver`**: A pointer to the instance of the class that you want to invoke the method on. This value must not be `nil`.
- **`method`**: The method whose implementation you want to call.
- **`...`**: A variable argument list containing the arguments to the method.

#### Discussion

Using this function to call the implementation of a method is faster than calling [`method_getImplementation(_:)`](./method_getimplementation%28_%29.md) and [`method_getName(_:)`](./method_getname%28_%29.md).

## See Also

### Working with Methods
- [method_invoke](./method_invoke.md)
  Calls the implementation of a specified method.
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
- [func method_getDescription(Method) -> UnsafeMutablePointer<objc_method_description>](./method_getdescription%28_%29.md)
  Returns a method description structure for a specified method.
- [func method_setImplementation(Method, IMP) -> IMP](./method_setimplementation%28_,_%29.md)
  Sets the implementation of a method.
- [func method_exchangeImplementations(Method, Method)](./method_exchangeimplementations%28_,_%29.md)
  Exchanges the implementations of two methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/method_invoke_stret)*