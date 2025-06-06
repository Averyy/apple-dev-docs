# Input and Output

**Framework**: Swift

Print values to the console, read from and write to text streams, and use command line arguments.

## Topics

### Text Output
- [func print(Any..., separator: String, terminator: String)](print(_:separator:terminator:).md)
  Writes the textual representations of the given items into the standard output.
- [func print<Target>(Any..., separator: String, terminator: String, to: inout Target)](print(_:separator:terminator:to:).md)
  Writes the textual representations of the given items into the given output stream.
### Command Line Input
- [enum CommandLine](commandline.md)
  Command-line arguments for the current process.
- [func readLine(strippingNewline: Bool) -> String?](readline(strippingnewline:).md)
  Returns a string read from standard input through the end of the current line or until EOF is reached.
### Streams
- [protocol TextOutputStream](textoutputstream.md)
  A type that can be the target of text-streaming operations.
- [protocol TextOutputStreamable](textoutputstreamable.md)
  A source of text-streaming operations.

## See Also

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
- [Type Casting and Existential Types](type-casting-and-existential-types.md)
  Perform casts between types or represent values of any type.
- [C Interoperability](c-interoperability.md)
  Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md)
  Work with prefix, postfix, and infix operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/input-and-output)*