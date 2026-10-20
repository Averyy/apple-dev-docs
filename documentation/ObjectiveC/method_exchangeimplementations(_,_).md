# method_exchangeImplementations(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Exchanges the implementations of two methods.

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
func method_exchangeImplementations(_ m1: Method, _ m2: Method)
```

```c
extern void method_exchangeImplementations(Method m1, Method m2);
```

#### Discussion

This is an atomic version of the following:

```objc
IMP imp1 = method_getImplementation(m1);
IMP imp2 = method_getImplementation(m2);
method_setImplementation(m1, imp2);
method_setImplementation(m2, imp1);
```

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
- [func method_getDescription(Method) -> UnsafeMutablePointer<objc_method_description>](./method_getdescription%28_%29.md)
  Returns a method description structure for a specified method.
- [func method_setImplementation(Method, IMP) -> IMP](./method_setimplementation%28_,_%29.md)
  Sets the implementation of a method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/method_exchangeimplementations(_:_:))*