# extendLifetime(_:)

**Framework**: Swift  
**Kind**: func

Extends the lifetime of the given instance.

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
func extendLifetime<T>(_ x: borrowing T) where T : ~Copyable, T : ~Escapable
```

## Parameters

- `x`: An instance to preserve until this function returns.

## See Also

- [struct Unmanaged](unmanaged.md)
  A type for propagating an unmanaged object reference.
- [func withExtendedLifetime<T, E, Result>(borrowing T, () throws(E) -> Result) throws(E) -> Result](withextendedlifetime(_:_:)-4mmpv.md)
  Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [func withExtendedLifetime<T, E, Result>(borrowing T, (borrowing T) throws(E) -> Result) throws(E) -> Result](withextendedlifetime(_:_:)-59dz3.md)
  Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/extendlifetime(_:))*