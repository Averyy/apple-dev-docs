# Ref

**Framework**: Swift  
**Kind**: struct

A safe reference allowing in-place reads to a shared value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct Ref<Value> where Value : ~Copyable, Value : ~Escapable
```

## Topics

### Initializers
- [init(borrowing Value)](ref/init(_:).md)
  Initializes an instance of `Ref` with the given borrowed value. This creates a constant reference to that value preventing writes on the original value while this reference is still active.
- [init<Owner>(unsafeAddress: UnsafePointer<Value>, borrowing: borrowing Owner)](ref/init(unsafeaddress:borrowing:).md)
  Unsafely initializes an instance of `Ref` using the given ‘unsafeAddress’ as the reference based on the borrowed lifetime of the given ‘owner’ argument.
### Instance Properties
- [var value: Value](ref/value.md)
  Dereferences the constant reference allowing for in-place reads to the underlying value.

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/ref)*