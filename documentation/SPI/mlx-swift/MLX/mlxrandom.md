---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom"
framework: "mlx-swift/MLX"
---

# MLXRandom

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Collection of functions related to random number generation.

## Declaration

```swift
enum MLXRandom
```

## Overview

Following [JAX’s PRNG design](https://jax.readthedocs.io/en/latest/jep/263-prng.html) we use a splittable version of Threefry, which is a counter-based PRNG.

Random sampling functions in MLX use an implicit global PRNG state by default. However, all functions take an optional key keyword argument for when more fine-grained control or explicit state management is needed.  Callers can also arrange for `Task` local random state – useful in multithreaded situations.

For example, you can generate random numbers with:

```swift
for _ in 0 ..< 3 {
  print(MLXRandom.uniform())
}
```

which will print a sequence of unique pseudo random numbers. Alternatively you can explicitly set the key:

```swift
let key = MLXRandom.key(0)
for _ in 0 ..< 3 {
  print(MLXRandom.uniform(key: key))
}
```

which will yield the same pseudo random number at each iteration as the key doesn’t change.

To get a new random number for each call you would [`split(key:stream:)`](./mlxrandom/split%28key,stream%29.md) the key:

```swift
var key = MLXRandom.key(0)
for _ in 0 ..< 3 {
  let (a, b) = MLXRandom.split(key: key)

  // use b to generate a different value each time
  print(MLXRandom.uniform(key: b))

  // new random state is a
  key = a
}
```

This will generate the same sequence of numbers each time (same starting key) but different values for each call.

As a convenience you can use [`MLXRandom.RandomState`](./mlxrandom/randomstate.md) to manage the key splitting and:

```swift
let state = RandomState(seed: 0)
for _ in 0 ..< 3 {
  print(MLXRandom.uniform(key: state))
}
```

Finally, if you need to control random state in deeply nested calls to `MLXRandom` or you need thread-safe random state for multi-threaded evaluation you can use [`withRandomState(_:body:)`](./withrandomstate%28_,body%29-18ob4.md).

```swift
await withTaskGroup { group in
    for i in 0 ..< 10 {
        group.addTask {
            let state = MLXRandom.RandomState(seed: UInt64(i))
            return withRandomState(state) {
                var t: Float = 0.0
                for _ in 0 ..< 100 {
                    t += uniform(0 ..< 1, [10, 10]).sum().item(Float.self)
                }
                return t
            }
        }
    }

    for await v in group {
        ...
    }
}
```

Each task will have separate [`MLXRandom.RandomState`](./mlxrandom/randomstate.md) that will be used implicitly (if no other key is passed in).

## Topics

### Classes
- [MLXRandom.RandomState](./mlxrandom/randomstate.md)
  Random state factory.
### Type Properties
- [static let globalState: MLXRandom.RandomState](./mlxrandom/globalstate.md)
  Global random state.
### Type Methods
- [static func bernoulli(some ScalarOrArray, (some Collection<Int>)?, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/bernoulli%28_,_,key,stream%29.md)
  Generate Bernoulli random values with a given `p` value.
- [static func bernoulli(some Collection<Int>, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/bernoulli%28_,key,stream%29.md)
  Generate Bernoulli random values with a `p` value of 0.5.
- [static func categorical(MLXArray, axis: Int, count: Int, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/categorical%28_,axis,count,key,stream%29.md)
  Sample `count` values from a categorical distribution.
- [static func categorical(MLXArray, axis: Int, shape: (some Collection<Int>)?, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/categorical%28_,axis,shape,key,stream%29.md)
  Sample from a categorical distribution.
- [static func gumbel(some Collection<Int>, dtype: DType, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/gumbel%28_,dtype,key,stream%29.md)
  Sample from the standard Gumbel distribution with a given `DType`.
- [static func gumbel(some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/gumbel%28_,type,key,stream%29.md)
  Sample from the standard Gumbel distribution.
- [static func key(UInt64) -> MLXArray](./mlxrandom/key%28_%29.md)
  Get a PRNG key from a seed.
- [static func laplace(some Collection<Int>, dtype: DType, loc: Float, scale: Float, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/laplace%28_,dtype,loc,scale,key,stream%29.md)
  Sample numbers from a Laplace distribution.
- [static func multivariateNormal(mean: MLXArray, covariance: MLXArray, shape: some Collection<Int>, dtype: DType, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/multivariatenormal%28mean,covariance,shape,dtype,key,stream%29.md)
  Generate jointly-normal random samples given a mean and covariance.
- [static func normal(some Collection<Int>, dtype: DType, loc: Float, scale: Float, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/normal%28_,dtype,loc,scale,key,stream%29.md)
  Generate normally distributed random numbers.
- [static func normal(some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, loc: Float, scale: Float, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/normal%28_,type,loc,scale,key,stream%29.md)
  Generate normally distributed random numbers.
- [static func permutation(MLXArray, axis: Int, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/permutation%28_,axis,key,stream%29.md)
  Generate a random permutation of the entries of an array.
- [static func permutation(Int, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/permutation%28_,key,stream%29.md)
  Generate a random permutation of integers from `0` to `max`.
- [static func randInt<T>(Range<T>, some Collection<Int>, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/randint%28_,_,key,stream%29.md)
  Generate random integers from the given interval using a `RangeExpression<Int>`.
- [static func randInt(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/randint%28low,high,_,key,stream%29.md)
  Generate random integers from the given interval (`low:` and `high:`).
- [static func randInt(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, type: (some HasDType & BinaryInteger).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/randint%28low,high,_,type,key,stream%29.md)
  Generate random integers from the given interval (`low:` and `high:`) with a given type, e.g. `Int8.self`.
- [static func seed(UInt64)](./mlxrandom/seed%28_%29.md)
  Seed the global PRNG.
- [static func split(key: MLXArray, into: Int, stream: StreamOrDevice) -> [MLXArray]](./mlxrandom/split%28key,into,stream%29.md)
  Split a PRNG key into sub keys.
- [static func split(key: MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./mlxrandom/split%28key,stream%29.md)
  Split a PRNG key into two keys and return a tuple.
- [static func truncatedNormal(Range<Float>, some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/truncatednormal%28_,_,type,key,stream%29-31qha.md)
  Generate values from a truncated normal distribution in a given `RangeExpression<Float>`.
- [static func truncatedNormal(Range<some HasDType & Comparable>, some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/truncatednormal%28_,_,type,key,stream%29-97urj.md)
  Generate values from a truncated normal distribution.
- [static func truncatedNormal(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, dtype: DType, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/truncatednormal%28low,high,_,dtype,key,stream%29.md)
  Generate values from a truncated normal distribution between `low` and `high` with a given `DType`.
- [static func truncatedNormal(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/truncatednormal%28low,high,_,type,key,stream%29.md)
  Generate values from a truncated normal distribution between `low` and `high`.
- [static func uniform(Range<Float>, some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/uniform%28_,_,type,key,stream%29-284c8.md)
  Generate uniformly distributed random numbers with a `RangeExpression<Float>` (specialization).
- [static func uniform(Range<some HasDType & Comparable>, some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/uniform%28_,_,type,key,stream%29-57r7y.md)
  Generate uniformly distributed random numbers with a `RangeExpression`.
- [static func uniform(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, dtype: DType, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/uniform%28low,high,_,dtype,key,stream%29.md)
  Generate uniformly distributed random numbers between `low` and `high` with a given `DType`.
- [static func uniform(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./mlxrandom/uniform%28low,high,_,type,key,stream%29.md)
  Generate uniformly distributed random numbers between `low` and `high`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom)*