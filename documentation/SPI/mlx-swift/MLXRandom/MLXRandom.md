---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom"
framework: "mlx-swift/MLXRandom"
---

# MLXRandom

**Framework**: mlx-swift/MLXRandom  
**Kind**: module  
**Role**: Framework

## Topics

### Variables
- [let deprecationWarning: Void](./deprecationwarning.md)
### Functions
- [func bernoulli(any ScalarOrArray, [Int]?, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./bernoulli%28_,_,key,stream%29.md)
  Generate Bernoulli random values with a given `p` value.
- [func bernoulli([Int], key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./bernoulli%28_,key,stream%29.md)
  Generate Bernoulli random values with a `p` value of 0.5.
- [func categorical(MLXArray, axis: Int, count: Int, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./categorical%28_,axis,count,key,stream%29.md)
  Sample `count` values from a categorical distribution.
- [func categorical(MLXArray, axis: Int, shape: [Int]?, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./categorical%28_,axis,shape,key,stream%29.md)
  Sample from a categorical distribution.
- [func gumbel([Int], dtype: DType, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./gumbel%28_,dtype,key,stream%29.md)
  Sample from the standard Gumbel distribution with a given `DType`.
- [func gumbel<T>([Int], type: T.Type, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./gumbel%28_,type,key,stream%29.md)
  Sample from the standard Gumbel distribution.
- [func key(UInt64) -> MLXArray](./key%28_%29.md)
  Get a PRNG key from a seed.
- [func laplace([Int], dtype: DType, loc: Float, scale: Float, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./laplace%28_,dtype,loc,scale,key,stream%29.md)
  Sample numbers from a Laplace distribution.
- [func multivariateNormal(mean: MLXArray, covariance: MLXArray, shape: [Int], dtype: DType, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./multivariatenormal%28mean,covariance,shape,dtype,key,stream%29.md)
  Generate jointly-normal random samples given a mean and covariance.
- [func normal([Int], dtype: DType, loc: Float, scale: Float, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./normal%28_,dtype,loc,scale,key,stream%29.md)
  Generate normally distributed random numbers.
- [func normal<T>([Int], type: T.Type, loc: Float, scale: Float, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./normal%28_,type,loc,scale,key,stream%29.md)
  Generate normally distributed random numbers.
- [func randInt<T>(Range<T>, [Int], key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./randint%28_,_,key,stream%29.md)
  Generate random integers from the given interval using a `RangeExpression<Int>`.
- [func randInt(low: any ScalarOrArray, high: any ScalarOrArray, [Int]?, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./randint%28low,high,_,key,stream%29.md)
  Generate random integers from the given interval (`low:` and `high:`).
- [func randInt<T>(low: any ScalarOrArray, high: any ScalarOrArray, [Int]?, type: T.Type, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./randint%28low,high,_,type,key,stream%29.md)
  Generate random integers from the given interval (`low:` and `high:`) with a given type, e.g. `Int8.self`.
- [func seed(UInt64)](./seed%28_%29.md)
  Seed the global PRNG.
- [func split(key: MLXArray, into: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28key,into,stream%29.md)
  Split a PRNG key into sub keys.
- [func split(key: MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./split%28key,stream%29.md)
  Split a PRNG key into two keys and return a tuple.
- [func truncatedNormal<T>(Range<Float>, [Int], type: T.Type, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./truncatednormal%28_,_,type,key,stream%29-62jwe.md)
  Generate values from a truncated normal distribution in a given `RangeExpression<Float>`.
- [func truncatedNormal<R, T>(Range<R>, [Int], type: T.Type, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./truncatednormal%28_,_,type,key,stream%29-8vjij.md)
  Generate values from a truncated normal distribution.
- [func truncatedNormal(low: any ScalarOrArray, high: any ScalarOrArray, [Int]?, dtype: DType, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./truncatednormal%28low,high,_,dtype,key,stream%29.md)
  Generate values from a truncated normal distribution between `low` and `high` with a given `DType`.
- [func truncatedNormal<T>(low: any ScalarOrArray, high: any ScalarOrArray, [Int]?, type: T.Type, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./truncatednormal%28low,high,_,type,key,stream%29.md)
  Generate values from a truncated normal distribution between `low` and `high`.
- [func uniform<R, T>(Range<R>, [Int], type: T.Type, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./uniform%28_,_,type,key,stream%29-10gj2.md)
  Generate uniformly distributed random numbers with a `RangeExpression`.
- [func uniform<T>(Range<Float>, [Int], type: T.Type, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./uniform%28_,_,type,key,stream%29-4d6d2.md)
  Generate uniformly distributed random numbers with a `RangeExpression<Float>` (specialization).
- [func uniform(low: any ScalarOrArray, high: any ScalarOrArray, [Int]?, dtype: DType, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./uniform%28low,high,_,dtype,key,stream%29.md)
  Generate uniformly distributed random numbers between `low` and `high` with a given `DType`.
- [func uniform<T>(low: any ScalarOrArray, high: any ScalarOrArray, [Int]?, type: T.Type, key: MLXArray?, stream: StreamOrDevice) -> MLXArray](./uniform%28low,high,_,type,key,stream%29.md)
  Generate uniformly distributed random numbers between `low` and `high`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom)*