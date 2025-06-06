# withExtendedLifetime(_:_:)

**Framework**: Swift  
**Kind**: func

Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.

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
func withExtendedLifetime<T, E, Result>(_ x: borrowing T, _ body: (borrowing T) throws(E) -> Result) throws(E) -> Result where E : Error, T : ~Copyable, Result : ~Copyable
```

#### Return Value

The return value, if any, of the `body` closure parameter.

## Parameters

- `x`: An instance to preserve until the execution of   is completed.
- `body`: A closure to execute that depends on the lifetime of   being   extended. If   has a return value, that value is also used as the   return value for the   method.

## See Also

- [struct Unmanaged](unmanaged.md)
  A type for propagating an unmanaged object reference.
- [func withExtendedLifetime<T, E, Result>(borrowing T, () throws(E) -> Result) throws(E) -> Result](withextendedlifetime(_:_:)-6mq1.md)
  Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withextendedlifetime(_:_:)-4kl68)*