# SystemRandomNumberGenerator

**Framework**: Swift  
**Kind**: struct

The system’s default source of random data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct SystemRandomNumberGenerator
```

#### Overview

When you generate random values, shuffle a collection, or perform another operation that depends on random data, this type is the generator used by default. For example, the two method calls in this example are equivalent:

```swift
let x = Int.random(in: 1...100)
var g = SystemRandomNumberGenerator()
let y = Int.random(in: 1...100, using: &g)
```

`SystemRandomNumberGenerator` is automatically seeded, is safe to use in multiple threads, and uses a cryptographically secure algorithm whenever possible.

### Platform Implementation of Systemrandomnumbergenerator

While the system generator is automatically seeded and thread-safe on every platform, the cryptographic quality of the stream of random data produced by the generator may vary. For more detail, see the documentation for the APIs used by each platform.

- Apple platforms use `arc4random_buf(3)`.
- Linux platforms use `getrandom(2)` when available; otherwise, they read from `/dev/urandom`.
- Windows uses `BCryptGenRandom`.

## Topics

### Creating a Generator
- [init()](systemrandomnumbergenerator/init.md)
  Creates a new instance of the system’s default random number generator.
### Generating Random Binary Data
- [func next() -> UInt64](systemrandomnumbergenerator/next.md)
  Returns a value from a uniform, independent distribution of binary data.
- [func next<T>() -> T](systemrandomnumbergenerator/next-2x0ly.md)
  Returns a value from a uniform, independent distribution of binary data.
- [func next<T>(upperBound: T) -> T](systemrandomnumbergenerator/next(upperbound:).md)
  Returns a random value that is less than the given upper bound.
### Default Implementations
- [RandomNumberGenerator Implementations](systemrandomnumbergenerator/randomnumbergenerator-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [RandomNumberGenerator](randomnumbergenerator.md)
- [Sendable](sendable.md)

## See Also

- [protocol RandomNumberGenerator](randomnumbergenerator.md)
  A type that provides uniformly distributed random data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/systemrandomnumbergenerator)*