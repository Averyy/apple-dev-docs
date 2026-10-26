# Local Variable Storage Duration

**Framework**: Objective-C Runtime

This macro indicates that the values stored in certain local variables should not be aggressively released by the compiler during optimization.

## Topics

### Constants
- [NS_VALID_UNTIL_END_OF_SCOPE](../Foundation/ns_valid_until_end_of_scope.md)
  Marks local variables of type `id` or pointer-to-ObjC-object-type so that values stored into those local variable are not aggressively released by the compiler during optimization. Instead, the values are held until either the variable is assigned to again, or the end of the scope of the local variable (such as in a compound statement or a method definition).

## See Also

### Constants
- [Boolean Values](./boolean-values.md)
  These macros define convenient constants to represent Boolean values.
- [Null Values](./null-values.md)
  These macros define null values for classes and instances.
- [Dispatch Function Prototypes](./dispatch-function-prototypes.md)
  This macro indicates whether dispatch functions must be cast to an appropriate function pointer type.
- [Objective-C Root Class](./objective-c-root-class.md)
  This macro annotates a class as being an Objective-C root class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/local-variable-storage-duration)*