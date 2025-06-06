# Type Casting and Existential Types

**Framework**: Swift

Perform casts between types or represent values of any type.

## Topics

### Integer Value Casting
- [func numericCast<T, U>(T) -> U](numericcast(_:).md)
  Returns the given integer as the equivalent value in a different integer type.
### Closure Casting
- [func withoutActuallyEscaping<ClosureType, ResultType, Failure>(ClosureType, do: (ClosureType) throws(Failure) -> ResultType) throws(Failure) -> ResultType](withoutactuallyescaping(_:do:).md)
  Allows a nonescaping closure to temporarily be used as if it were allowed to escape.
### Instance Casting
- [func unsafeDowncast<T>(AnyObject, to: T.Type) -> T](unsafedowncast(_:to:).md)
  Returns the given instance cast unconditionally to the specified type.
- [func unsafeBitCast<T, U>(T, to: U.Type) -> U](unsafebitcast(_:to:).md)
  Returns the bits of the given instance, interpreted as having the specified type.
### Existential Types
- [typealias AnyObject](anyobject.md)
  The protocol to which all classes implicitly conform.
- [typealias AnyClass](anyclass.md)
  The protocol to which all class types implicitly conform.
### Comparing Identity
- [func === (AnyObject?, AnyObject?) -> Bool](===(_:_:).md)
- [func !== (AnyObject?, AnyObject?) -> Bool](!==(_:_:).md)
### Void Type
- [typealias Void](void.md)
  The return type of functions that don’t explicitly specify a return type, that is, an empty tuple `()`.

## See Also

- [Input and Output](input-and-output.md)
  Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](debugging-and-reflection.md)
  Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](macros.md)
  Generate boilerplate code and perform other compile-time operations.
- [Concurrency](concurrency.md)
  Perform asynchronous and parallel operations.
- [Key-Path Expressions](key-path-expressions.md)
  Use key-path expressions to access properties dynamically.
- [Manual Memory Management](manual-memory-management.md)
  Allocate and manage memory manually.
- [C Interoperability](c-interoperability.md)
  Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md)
  Work with prefix, postfix, and infix operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/type-casting-and-existential-types)*