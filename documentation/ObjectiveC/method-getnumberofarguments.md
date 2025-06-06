# method_getNumberOfArguments(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

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

#### Return Value

An integer containing the number of arguments accepted by the given method.

## Parameters

- `m`: A pointer to a   data structure. Pass the method in question.

## See Also

- [func method_getName(Method) -> Selector](method_getname(_:).md)
  Returns the name of a method.
- [func method_getImplementation(Method) -> IMP](method_getimplementation(_:).md)
  Returns the implementation of a method.
- [func method_getTypeEncoding(Method) -> UnsafePointer<CChar>?](method_gettypeencoding(_:).md)
  Returns a string describing a method’s parameter and return types.
- [func method_copyReturnType(Method) -> UnsafeMutablePointer<CChar>](method_copyreturntype(_:).md)
  Returns a string describing a method’s return type.
- [func method_copyArgumentType(Method, UInt32) -> UnsafeMutablePointer<CChar>?](method_copyargumenttype(_:_:).md)
  Returns a string describing a single parameter type of a method.
- [func method_getReturnType(Method, UnsafeMutablePointer<CChar>, Int)](method_getreturntype(_:_:_:).md)
  Returns by reference a string describing a method’s return type.
- [func method_getArgumentType(Method, UInt32, UnsafeMutablePointer<CChar>?, Int)](method_getargumenttype(_:_:_:_:).md)
  Returns by reference a string describing a single parameter type of a method.
- [func method_getDescription(Method) -> UnsafeMutablePointer<objc_method_description>](method_getdescription(_:).md)
  Returns a method description structure for a specified method.
- [func method_setImplementation(Method, IMP) -> IMP](method_setimplementation(_:_:).md)
  Sets the implementation of a method.
- [func method_exchangeImplementations(Method, Method)](method_exchangeimplementations(_:_:).md)
  Exchanges the implementations of two methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/method_getnumberofarguments(_:))*