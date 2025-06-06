# Swift Standard Library

**Framework**: Swift

Solve complex problems and write high-performance, readable code.

#### Overview

The Swift standard library defines a base layer of functionality for writing Swift programs, including:

- Fundamental data types such as [`Int`](int.md), [`Double`](double.md), and [`String`](string.md)
- Common data structures such as [`Array`](array.md), [`Dictionary`](dictionary.md), and [`Set`](set.md)
- Global functions such as [`print(_:separator:terminator:)`](print(_:separator:terminator:).md) and [`abs(_:)`](abs(_:).md)
- Protocols, such as [`Collection`](collection.md) and [`Equatable`](equatable.md), that describe common abstractions.
- Protocols, such as [`CustomDebugStringConvertible`](customdebugstringconvertible.md) and [`CustomReflectable`](customreflectable.md), that you use to customize operations that are available to all types.
- Protocols, such as [`OptionSet`](optionset.md), that you use to provide implementations that would otherwise require boilerplate code.

> **Note**: Experiment with Swift standard library types and learn high-level concepts using visualizations and practical examples. Learn how the Swift standard library uses protocols and generics to express powerful constraints. Download the playground below to get started. [`Swift Standard Library.playground`](https://developer.apple.comhttps://developer.apple.com/sample-code/swift/downloads/standard-library.zip)

Experiment with Swift standard library types and learn high-level concepts using visualizations and practical examples. Learn how the Swift standard library uses protocols and generics to express powerful constraints. Download the playground below to get started.

[`Swift Standard Library.playground`](https://developer.apple.comhttps://developer.apple.com/sample-code/swift/downloads/standard-library.zip)

## Topics

### Values and Collections
- [Numbers and Basic Values](numbers-and-basic-values.md)
  Model data with numbers, Boolean values, and other fundamental types.
- [Strings and Text](strings-and-text.md)
  Work with text using Unicode-safe strings.
- [Collections](collections.md)
  Store and organize data using arrays, dictionaries, sets, and other data structures.
- [Time](time-and-duration.md)
  Measure how long an operation takes and determine schedules in the future.
### Tools for Your Types
- [Basic Behaviors](basic-behaviors.md)
  Use your custom types in operations that depend on testing for equality or order and as members of sets and dictionaries.
- [Encoding, Decoding, and Serialization](encoding-decoding-and-serialization.md)
  Serialize and deserialize instances of your types with implicit or customized encoding.
- [Initialization with Literals](initialization-with-literals.md)
  Allow values of your type to be expressed using different kinds of literals.
### Programming Tasks
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
- [Type Casting and Existential Types](type-casting-and-existential-types.md)
  Perform casts between types or represent values of any type.
- [C Interoperability](c-interoperability.md)
  Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md)
  Work with prefix, postfix, and infix operators.
### Deprecated
- [Deprecated](deprecated.md)

## See Also

- [struct Int](int.md)
  A signed integer value type.
- [struct Double](double.md)
  A double-precision, floating-point value type.
- [struct String](string.md)
  A Unicode string value that is a collection of characters.
- [struct Array](array.md)
  An ordered, random-access collection.
- [struct Dictionary](dictionary.md)
  A collection whose elements are key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/swift-standard-library)*