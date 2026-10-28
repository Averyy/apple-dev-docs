---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/vjp(_:primals:cotangents:)"
framework: "mlx-swift/MLX"
---

# vjp(_:primals:cotangents:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the vector-Jacobian product.

## Declaration

```swift
func vjp(_ f: @escaping ([MLXArray]) -> [MLXArray], primals: some Collection<MLXArray>, cotangents: some Collection<MLXArray>) -> ([MLXArray], [MLXArray])
```

## Return Value

Array of the vector-Jacobian products which is the same in number, shape and type of the outputs of `f`

## Discussion

Computes the product of the `cotangents` with the Jacobian of a function `f` evaluated at `primals`.

## Parameters

- `f`: Function which takes an array of [`MLXArray`](./mlxarray.md) and returns an array of [`MLXArray`](./mlxarray.md)
- `primals`: Array of [`MLXArray`](./mlxarray.md) at which to evaluate the Jacobian
- `cotangents`: Array of [`MLXArray`](./mlxarray.md) which are the “vector” in the vector-Jacobian product.  The `cotangents` should be the same in number, shape and type as the outputs of `f`

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
- [func jvp(([MLXArray]) -> [MLXArray], primals: some Collection<MLXArray>, tangents: some Collection<MLXArray>) -> ([MLXArray], [MLXArray])](./jvp%28_,primals,tangents%29.md)
  Compute the Jacobian-vector product.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/vjp(_:primals:cotangents:))*