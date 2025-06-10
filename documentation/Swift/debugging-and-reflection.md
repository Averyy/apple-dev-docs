# Debugging and Reflection

**Framework**: Swift

Fortify your code with runtime checks, and examine your values’ runtime representation.

## Topics

### Printing and Dumping
- [func print(Any..., separator: String, terminator: String)](print(_:separator:terminator:).md)
  Writes the textual representations of the given items into the standard output.
- [func print<Target>(Any..., separator: String, terminator: String, to: inout Target)](print(_:separator:terminator:to:).md)
  Writes the textual representations of the given items into the given output stream.
- [func debugPrint(Any..., separator: String, terminator: String)](debugprint(_:separator:terminator:).md)
  Writes the textual representations of the given items most suitable for debugging into the standard output.
- [func debugPrint<Target>(Any..., separator: String, terminator: String, to: inout Target)](debugprint(_:separator:terminator:to:).md)
  Writes the textual representations of the given items most suitable for debugging into the given output stream.
- [func dump<T>(T, name: String?, indent: Int, maxDepth: Int, maxItems: Int) -> T](dump(_:name:indent:maxdepth:maxitems:).md)
  Dumps the given object’s contents using its mirror to standard output.
- [func dump<T, TargetStream>(T, to: inout TargetStream, name: String?, indent: Int, maxDepth: Int, maxItems: Int) -> T](dump(_:to:name:indent:maxdepth:maxitems:).md)
  Dumps the given object’s contents using its mirror to the specified output stream.
### Testing
- [func assert(@autoclosure () -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](assert(_:_:file:line:).md)
  Performs a traditional C-style assert with an optional message.
- [func assertionFailure(@autoclosure () -> String, file: StaticString, line: UInt)](assertionfailure(_:file:line:).md)
  Indicates that an internal consistency check failed.
- [func precondition(@autoclosure () -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](precondition(_:_:file:line:).md)
  Checks a necessary condition for making forward progress.
- [func preconditionFailure(@autoclosure () -> String, file: StaticString, line: UInt) -> Never](preconditionfailure(_:file:line:).md)
  Indicates that a precondition was violated.
### Exiting a Program
- [func fatalError(@autoclosure () -> String, file: StaticString, line: UInt) -> Never](fatalerror(_:file:line:).md)
  Unconditionally prints a given message and stops execution.
- [enum Never](never.md)
  A type that has no values and can’t be constructed.
### Querying Runtime Values
- [struct Mirror](mirror.md)
  A representation of the substructure and display style of an instance of any type.
- [struct ObjectIdentifier](objectidentifier.md)
  A unique identifier for a class instance or metatype.
- [func type<T, Metatype>(of: borrowing T) -> Metatype](type(of:).md)
  Returns the dynamic type of a value.
### Customizing Your Type’s Reflection
- [protocol CustomReflectable](customreflectable.md)
  A type that explicitly supplies its own mirror.
- [protocol CustomLeafReflectable](customleafreflectable.md)
  A type that explicitly supplies its own mirror, but whose descendant classes are not represented in the mirror unless they also override `customMirror`.
- [protocol CustomPlaygroundDisplayConvertible](customplaygrounddisplayconvertible.md)
  A type that supplies a custom description for playground logging.
- [typealias PlaygroundQuickLook](playgroundquicklook.md)
  The sum of types that can be used as a Quick Look representation.
- [macro DebugDescription()](debugdescription().md)
  Converts description definitions to a debugger Type Summary.

## See Also

- [Input and Output](input-and-output.md)
  Print values to the console, read from and write to text streams, and use command line arguments.
- [Macros](macros.md)
  Generate boilerplate code and perform other compile-time operations.
- [Concurrency](concurrency.md)
  Perform asynchronous and parallel operations.
- [Key-Path Expressions](key-path-expressions.md)
  Use key-path expressions to access properties dynamically.
- [Manual Memory Management](manual-memory-management.md)
  Allocate and manage memory manually.
- [Type Casting and Existential Types](type-casting-and-existential-types.md)
  Perform casts between types or represent values of any type.
- [C Interoperability](c-interoperability.md)
  Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md)
  Work with prefix, postfix, and infix operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/debugging-and-reflection)*