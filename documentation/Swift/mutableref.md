# MutableRef

**Framework**: Swift  
**Kind**: struct

A safe mutable reference allowing in-place mutation to an exclusive value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@frozen
struct MutableRef<Value> where Value : ~Copyable
```

## Topics

### Initializers
- [init(inout Value)](mutableref/init(_:).md)
  Initializes an instance of `MutableRef` with the given mutable value. This creates a mutable reference to that value preventing writes to the original value while this mutable reference is still active.
- [init<Owner>(unsafeAddress: UnsafeMutablePointer<Value>, mutating: inout Owner)](mutableref/init(unsafeaddress:mutating:).md)
  Unsafely initializes an instance of `MutableRef` using the given ‘unsafeAddress’ as the mutable reference based on the mutating lifetime of the given ‘owner’ argument.
### Instance Properties
- [var value: Value](mutableref/value.md)
  Dereferences the mutable reference allowing for in-place reads and writes to the underlying value.

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Ref](ref.md)
  A safe reference allowing in-place reads to a shared value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutableref)*