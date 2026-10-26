# Objective-C Root Class

**Framework**: Objective-C Runtime  
**Role**: API Collection

This macro annotates a class as being an Objective-C root class.

## Topics

### Constants
- [OBJC_ROOT_CLASS](./objc_root_class.md)
  If you define an Objective-C root class, you receive a compiler error indicating that the class is defined without specifying a base class. You can avoid this compiler error by preceding the definition of the root class (that is, before the `@interface` directive) with `OBJC_ROOT_CLASS`.

## See Also

### Constants
- [Boolean Values](./boolean-values.md)
  These macros define convenient constants to represent Boolean values.
- [Null Values](./null-values.md)
  These macros define null values for classes and instances.
- [Dispatch Function Prototypes](./dispatch-function-prototypes.md)
  This macro indicates whether dispatch functions must be cast to an appropriate function pointer type.
- [Local Variable Storage Duration](./local-variable-storage-duration.md)
  This macro indicates that the values stored in certain local variables should not be aggressively released by the compiler during optimization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objective-c-root-class)*