# Objective-C Runtime Utilities

**Framework**: Foundation

Interact with the Objective-C runtime.

## Topics

### Type Lookup
- [func NSClassFromString(String) -> AnyClass?](nsclassfromstring(_:).md)
  Obtains a class by name.
- [func NSStringFromClass(AnyClass) -> String](nsstringfromclass(_:).md)
  Returns the name of a class as a string.
- [func NSSelectorFromString(String) -> Selector](nsselectorfromstring(_:).md)
  Returns the selector with a given name.
- [func NSStringFromSelector(Selector) -> String](nsstringfromselector(_:).md)
  Returns a string representation of a given selector.
- [func NSStringFromProtocol(Protocol) -> String](nsstringfromprotocol(_:).md)
  Returns the name of a protocol as a string.
- [func NSProtocolFromString(String) -> Protocol?](nsprotocolfromstring(_:).md)
  Returns a the protocol with a given name.
### Serialization
- [func NSGetSizeAndAlignment(UnsafePointer<CChar>, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?) -> UnsafePointer<CChar>](nsgetsizeandalignment(_:_:_:).md)
  Obtains the actual size and the aligned size of an encoded type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/objective-c-runtime-utilities)*