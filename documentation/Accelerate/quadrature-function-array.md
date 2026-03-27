# quadrature_function_array

**Framework**: Accelerate  
**Kind**: typealias

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
typealias quadrature_function_array = (UnsafeMutableRawPointer?, Int, UnsafePointer<Double>, UnsafeMutablePointer<Double>) -> Void
```

#### Discussion

Y=F(X) one-dimensional real function, array form, double precision

Should set values y[i] = F(x[i]) for i=0..n-1.

## Parameters

- `arg`: User argument passed back to the function when evaluated
- `n`: Dimension of arrays X and Y
- `x`: Array of points to evaluate the function
- `y`: Array receiving the values

## See Also

- [struct quadrature_integrate_function](quadrature_integrate_function.md)
- [struct quadrature_integrate_options](quadrature_integrate_options.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature_function_array)*