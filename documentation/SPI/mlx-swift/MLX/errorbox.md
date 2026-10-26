---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/errorbox"
framework: "mlx-swift/MLX"
---

# ErrorBox

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

Boxed error type usable with [`withError(_:)`](./witherror%28_%29-2wfiu.md).

## Declaration

```swift
final class ErrorBox
```

#### Overview

For example:

```swift
try withError { error in
    let a = MLXArray(0 ..< 10, [2, 5])
    let b = MLXArray(0 ..< 15, [3, 5])

    // no errors yet
    try error.check()

    // this will trigger a broadcast error
    let x = a + b

    // explicitly check for errors or return from the block
    try error.check()
    return x
}
```

In some cases it may be more convenient to use the [`withError(_:)`](./witherror%28_%29-6g4wn.md) form that doesn’t expose this value – any error will be thrown when the block exits.

## Topics

### Instance Properties
- [var firstError: (any Error)?](./errorbox/firsterror.md)
  The first error encountered, if any.
### Instance Methods
- [func check() throws](./errorbox/check%28%29.md)
  Throw the [`firstError`](./errorbox/firsterror.md) if set, otherwise do nothing.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/errorbox)*