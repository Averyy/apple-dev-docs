# Objective-C Runtime Utilities

**Framework**: Foundation  
**Role**: API Collection

Interact with the Objective-C runtime.

## Topics

### Type Lookup
- [func NSClassFromString(String) -> AnyClass?](./nsclassfromstring%28_%29.md)
  Obtains a class by name.
- [func NSStringFromClass(AnyClass) -> String](./nsstringfromclass%28_%29.md)
  Returns the name of a class as a string.
- [func NSSelectorFromString(String) -> Selector](./nsselectorfromstring%28_%29.md)
  Returns the selector with a given name.
- [func NSStringFromSelector(Selector) -> String](./nsstringfromselector%28_%29.md)
  Returns a string representation of a given selector.
- [func NSStringFromProtocol(Protocol) -> String](./nsstringfromprotocol%28_%29.md)
  Returns the name of a protocol as a string.
- [func NSProtocolFromString(String) -> Protocol?](./nsprotocolfromstring%28_%29.md)
  Returns a the protocol with a given name.
### Serialization
- [func NSGetSizeAndAlignment(UnsafePointer<CChar>, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?) -> UnsafePointer<CChar>](./nsgetsizeandalignment%28_,_,_%29.md)
  Obtains the actual size and the aligned size of an encoded type.
### Object Allocation and Deallocation
- [NSAllocateObject](./nsallocateobject.md)
  Creates and returns a new instance of a given class.
- [NSCopyObject](./nscopyobject.md)
  Creates an exact copy of an object.
- [NSDeallocateObject](./nsdeallocateobject.md)
  Destroys an existing object.
- [NSDecrementExtraRefCountWasZero](./nsdecrementextrarefcountwaszero.md)
  Decrements the specified object’s reference count.
- [NSExtraRefCount](./nsextrarefcount.md)
  Returns the specified object’s reference count.
- [NSIncrementExtraRefCount](./nsincrementextrarefcount.md)
  Increments the specified object’s reference count.
- [NSShouldRetainWithZone](./nsshouldretainwithzone.md)
  Indicates whether an object should be retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/objective-c-runtime-utilities)*