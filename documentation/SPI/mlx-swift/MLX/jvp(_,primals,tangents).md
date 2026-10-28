---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/jvp(_:primals:tangents:)"
framework: "mlx-swift/MLX"
---

# jvp(_:primals:tangents:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the Jacobian-vector product.

## Declaration

```swift
func jvp(_ f: @escaping ([MLXArray]) -> [MLXArray], primals: some Collection<MLXArray>, tangents: some Collection<MLXArray>) -> ([MLXArray], [MLXArray])
```

## Return Value

Array of the Jacobian-vector products which is the same in number, shape and type of the outputs of `f`

## Discussion

This computes the product of the Jacobian of a function `f` evaluated at `primals` with the `tangents`.

## Parameters

- `f`: Function which takes an array of [`MLXArray`](./mlxarray.md) and returns an array of [`MLXArray`](./mlxarray.md)
- `primals`: Array of [`MLXArray`](./mlxarray.md) at which to evaluate the Jacobian
- `tangents`: Array of [`MLXArray`](./mlxarray.md) which are the “vector” in the Jacobian-vector product.  The `tangents` should be the same in number, shape and type as the inputs of `f`, e.g. the `primals`

## See Also

### Evaluation and Transformation
- [func eval(MLXArray...)](./eval%28_%29-91pbd.md)
  Evaluate one or more `MLXArray`
- [func eval(some Collection<MLXArray>)](./eval%28_%29-45gpq.md)
  Evaluate one or more `MLXArray`
- [func eval(Any...)](./eval%28_%29-3b2g9.md)
  Evaluate one or more `MLXArray`.
- [func eval(some Sequence<Any>)](./eval%28_%29-3odmu.md)
  Evaluate one or more `MLXArray`.
- [func asyncEval(some Collection<MLXArray>)](./asynceval%28_%29-488lb.md)
  Evaluate one or more `MLXArray` asynchronously.
- [func asyncEval(Any...)](./asynceval%28_%29-6j4zg.md)
  Evaluate one or more `MLXArray` asynchronously.
- [func asyncEval(some Sequence<Any>)](./asynceval%28_%29-2zqay.md)
  Evaluate one or more `MLXArray` asynchronously.
- [func grad((MLXArray) -> MLXArray) -> (MLXArray) -> MLXArray](./grad%28_%29-r8dv.md)
- [func grad((MLXArray) -> [MLXArray]) -> (MLXArray) -> [MLXArray]](./grad%28_%29-7z6i.md)
- [func grad(([MLXArray]) -> [MLXArray], argumentNumbers: some Collection<Int>) -> ([MLXArray]) -> [MLXArray]](./grad%28_,argumentnumbers%29-5qg53.md)
- [func grad(([MLXArray]) -> MLXArray, argumentNumbers: some Collection<Int>) -> ([MLXArray]) -> MLXArray](./grad%28_,argumentnumbers%29-qlix.md)
- [func valueAndGrad<T>((NestedDictionary<String, MLXArray>, T) -> [MLXArray]) -> (NestedDictionary<String, MLXArray>, T) -> ([MLXArray], NestedDictionary<String, MLXArray>)](./valueandgrad%28_%29.md)
  Returns a function that computes the gradient and result of `f`, computing the gradient with respect to the [`NestedDictionary`](./nesteddictionary.md).
- [func valueAndGrad(([MLXArray]) -> [MLXArray], argumentNumbers: some Collection<Int>) -> ([MLXArray]) -> ([MLXArray], [MLXArray])](./valueandgrad%28_,argumentnumbers%29.md)
- [func stopGradient(MLXArray, stream: StreamOrDevice) -> MLXArray](./stopgradient%28_,stream%29.md)
  Stop gradients from being computed.
- [func vjp(([MLXArray]) -> [MLXArray], primals: some Collection<MLXArray>, cotangents: some Collection<MLXArray>) -> ([MLXArray], [MLXArray])](./vjp%28_,primals,cotangents%29.md)
  Compute the vector-Jacobian product.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/jvp(_:primals:tangents:))*