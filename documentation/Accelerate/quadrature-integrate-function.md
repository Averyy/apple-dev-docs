# quadrature_integrate_function

**Framework**: Accelerate  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct quadrature_integrate_function
```

#### Overview

Describes a real function Y=F(X). Since most of the integration time is spent evaluating F, we allow the caller to provide a array callback, computing several values of F in a single call.

## Topics

### Initializers
- [init(fun: quadrature_function_array, fun_arg: UnsafeMutableRawPointer!)](quadrature_integrate_function/init(fun:fun_arg:).md)
### Instance Properties
- [var fun: quadrature_function_array](quadrature_integrate_function/fun.md)
- [var fun_arg: UnsafeMutableRawPointer!](quadrature_integrate_function/fun_arg.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias quadrature_function_array](quadrature_function_array.md)
- [struct quadrature_integrate_options](quadrature_integrate_options.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature_integrate_function)*