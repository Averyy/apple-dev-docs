---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx"
framework: "mlx-swift/MLX"
---

# MLX

**Framework**: mlx-swift/MLX  
**Kind**: module  
**Role**: Framework

MLX Swift is a Swift API for MLX.

## Mentions

- [Converting From Python](./converting-python.md)
- [Installation](./install.md)
- [Troubleshooting](./troubleshooting.md)

## Overview

MLX is an array framework for machine learning on Apple silicon. MLX Swift expands MLX to the Swift language, making research and experimentation easier on Apple silicon.

The Swift API closely follows the [C++ and Python MLX APIs](https://ml-explore.github.io/mlx/build/html/index.html), which in turn closely follow NumPy with a few exceptions. Here are some useful pages showing how MLX Swift works and is different from python:

- [Converting From Python](./converting-python.md) – information about converting Python code and differences between Python and Swift
- [Indexing](./indexing.md) – information about array indexing
- [Arithmetic](./arithmetic.md) – information about array arithmetic

The main differences between MLX and NumPy are:

- **Composable function transformations**: MLX has composable function transformations for automatic differentiation, automatic vectorization, and computation graph optimization.
- **[Lazy Evaluation](./lazy-evaluation.md)**: Computations in MLX are lazy. Arrays are only materialized when needed.
- **Multi-device**: Operations can run on any of the supported devices (CPU, GPU, …)

The design of MLX is inspired by frameworks like [PyTorch](https://pytorch.org/), [Jax](https://github.com/google/jax), and [ArrayFire](https://arrayfire.org/). A notable difference from these frameworks and MLX is the [Unified Memory](./unified-memory.md). Arrays in MLX live in shared memory. Operations on MLX arrays can be performed on any of the supported device types without performing data copies. Currently supported device types are the CPU and GPU.

## Wired Memory

MLX includes a process-wide wired memory coordinator for GPU workloads. Use `WiredMemoryManager` and `WiredMemoryTicket` to coordinate wired limit changes across concurrent tasks, and implement `WiredMemoryPolicy` to define how limits are computed.

MLX ships generic policies like `WiredSumPolicy` and `WiredMaxPolicy`. For LLM-oriented defaults (such as fixed budgets or admission gating), see MLXLMCommon in mlx-swift-lm.

Tickets can represent active work (`kind: .active`) or long-lived reservations (`kind: .reservation`) so you can account for model weights without keeping the wired limit elevated while idle.

```swift
let policy = WiredSumPolicy()

// Optional: reserve model weights without keeping the limit elevated while idle.
let weights = policy.ticket(size: weightsBytes, kind: .reservation)
_ = await weights.start()

// Raise the limit only while inference is active.
let ticket = policy.ticket(size: kvBytes, kind: .active)
try await ticket.withWiredLimit {
    // run inference
}
```

See [Wired Memory Management](./wired-memory.md) for configuration, best practices, and policy guidance.

## Other MLX Packages

- [MLXNN](../MLXNN/MLXNN.md)
- [MLXOptimizers](../MLXOptimizers/MLXOptimizers.md)
- [Python `mlx`](https://ml-explore.github.io/mlx/build/html/index.html)

## Topics

### MLX
- [Installation](./install.md)
  How to install and use.
- [Troubleshooting](./troubleshooting.md)
  Help with problems you might run into.
- [MLX Swift Examples](./examples.md)
  Swift example code for MLX and MLXNN.
- [Converting From Python](./converting-python.md)
  Common patterns from python and mapping `mlx` function names.
- [Numpy Style Broadcasting](./broadcasting.md)
  How different size arrays can be used together.
- [Lazy Evaluation](./lazy-evaluation.md)
  Computation in `MLX` is lazy.  Understand when the graph is evaluated.
- [Unified Memory](./unified-memory.md)
  `MLX` takes advantage of the shared memory between the CPU and GPU.
- [Vectorization](./vmap.md)
  Automatic vectorization with `vmap`.
- [Compilation](./compilation.md)
  MLX has a [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) function transformation which compiles computation graphs. Function compilation results in smaller graphs by merging common work and fusing certain operations. In many cases this can lead to big improvements in run-time and memory use.
- [Using Streams](./using-streams.md)
  Controlling where your computations are evaluated.
- [Running on iOS](./running-on-ios.md)
  Considerations for running on iOS and general memory tuning.
- [Wired Memory Management](./wired-memory.md)
  Coordinate a process-wide wired memory limit for GPU workloads.
### MLXArray
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
### Free Functions
- [Free Functions](./free-functions.md)
  Free functions in MLX.
### Memory
- [enum GPU](./gpu.md)
  API for controlling GPU related features.
- [actor WiredMemoryManager](./wiredmemorymanager.md)
  Central coordinator for process-wide wired memory limits.
- [struct WiredMemoryTicket](./wiredmemoryticket.md)
  Handle for coordinating wired memory changes across concurrent work.
- [protocol WiredMemoryPolicy](./wiredmemorypolicy.md)
  Policy for computing a process-global wired memory limit.
- [struct WiredMemoryEvent](./wiredmemoryevent.md)
  Debug event emitted by [`WiredMemoryManager`](./wiredmemorymanager.md) when coordinating wired memory changes.
### Data Types
- [enum DType](./dtype.md)
  Enum wrapping `Cmlx.mlx_array_dtype`.
- [protocol HasDType](./hasdtype.md)
  Protocol for types that can provide a [`DType`](./dtype.md)
- [protocol ScalarOrArray](./scalarorarray.md)
  Protocol for promoting a value (e.g. a scalar) to an MLXArray.
- [protocol NestedArrayElement](./nestedarrayelement.md)
  A value that can appear in a nested array used to create an [`MLXArray`](./mlxarray.md).
### Parameter Types
- [struct IntOrPair](./intorpair.md)
  Parameter for convolutions allowing single integers or tuples.
- [struct IntOrTriple](./intortriple.md)
  Parameter for convolutions allowing single integers or triples.
- [enum IntOrArray](./intorarray.md)
  Parameter for convolutions allowing single integers or arrays.
- [enum FloatOrArray](./floatorarray.md)
  Parameter for taking a single or multiple Float values.
### Nested Data
- [struct NestedDictionary](./nesteddictionary.md)
  Nested structure of arrays, dictionaries and values.
- [enum NestedItem](./nesteditem.md)
  Backing storage for [`NestedDictionary`](./nesteddictionary.md).
- [protocol IndentedDescription](./indenteddescription.md)
  Protocol for types that can provide an indented description, e.g. nested types.
### Streams and Devices
- [struct StreamOrDevice](./streamordevice.md)
  Parameter type for all MLX operations.
- [class Device](./device.md)
  Representation of a Device in MLX.
- [enum DeviceType](./devicetype.md)
  Type of device.
- [class Stream](./stream.md)
  A stream of evaluation attached to a particular device.
### Distributed
- [enum MLXDistributed](./mlxdistributed.md)
  Communication operations for running MLX across multiple processes.
### Classes
- [class ErrorBox](./errorbox.md)
  Boxed error type usable with [`withError(_:)`](./witherror%28_%29-2wfiu.md).
- [class FunctionExporterMultiple](./functionexportermultiple.md)
  A helper for [`exportFunctions(to:shapeless:_:build:)`](./exportfunctions%28to,shapeless,_,build%29.md).
- [class FunctionExporterSingle](./functionexportersingle.md)
  A helper for [`exportFunction(to:shapeless:_:)`](./exportfunction%28to,shapeless,_%29.md).
- [class ImportedFunction](./importedfunction.md)
  Helper for [`importFunction(from:)`](./importfunction%28from%29.md) – this holds the imported function.
- [class MLXLogger](./mlxlogger.md)
  Thin wrapper for logging in MLX and MLX libraries.  This provides a hook for library code if it needs logging without adding a dependency or requiring a certain logging backend.
- [class NodeNamer](./nodenamer.md)
  Assigns human readable names to arrays in a compute graph.
### Protocols
- [protocol Evaluatable](./evaluatable.md)
  An object that can be passed to [`eval(_:)`](./eval%28_%29-45gpq.md) and can produce a list of interior [`MLXArray`](./mlxarray.md) to be evaluated.
- [protocol KernelTemplateArg](./kerneltemplatearg.md)
  Marker protocol for types that can be used in the `template` of a kernel call.
- [protocol MLXArrayIndex](./mlxarrayindex.md)
  Protocol for values usable as an index with [`MLXArray`](./mlxarray.md).
- [protocol MLXLogHandler](./mlxloghandler.md)
  Protocol for backing of MLXLogger.
- [protocol RandomStateOrKey](./randomstateorkey.md)
  Protocol for types that can be used as a provider of random keys, e.g. for [`MLXRandom`](./mlxrandom.md).
- [protocol Updatable](./updatable.md)
  An object that can provide a list of the [`MLXArray`](./mlxarray.md) in its inner state.
### Structures
- [struct ArrayAt](./arrayat.md)
  Intermediate type for [`at`](./mlxarray/at.md).
- [struct ArrayAtIndices](./arrayatindices.md)
  Intermediate type for [`at`](./mlxarray/at.md).
- [struct MLXEllipsisIndex](./mlxellipsisindex.md)
- [struct MLXNewAxisIndex](./mlxnewaxisindex.md)
- [struct MLXSlice](./mlxslice.md)
  Representation of a slice in [`MLXArray`](./mlxarray.md) indexing operations.
- [struct OSLogHandler](./osloghandler.md)
  On systems that support it, a log handler that is backed by OSLog.
- [struct StderrHandler](./stderrhandler.md)
  A logger that logs to `stderr`.
- [struct WiredMaxPolicy](./wiredmaxpolicy.md)
  Policy that uses the maximum active ticket size and adds it to the baseline.
- [struct WiredMemoryManagerConfiguration](./wiredmemorymanagerconfiguration.md)
  Configuration knobs for `WiredMemoryManager` behavior.
- [struct WiredSumPolicy](./wiredsumpolicy.md)
  Policy that sums active ticket sizes and adds them to the baseline.
### Functions
- [func CustomFunction(() -> ([MLXArray]) -> [MLXArray]) -> ([MLXArray]) -> [MLXArray]](./customfunction%28_%29.md)
- [func Forward(([MLXArray]) -> [MLXArray]) -> MLXCustomFunctionComponent](./forward%28_%29.md)
- [func RoPE(MLXArray, dimensions: Int, traditional: Bool, base: Float?, scale: Float, offset: Int, freqs: MLXArray?, stream: StreamOrDevice) -> MLXArray](./rope%28_,dimensions,traditional,base,scale,offset,freqs,stream%29-49hsu.md)
  Optimized implementation of `NN.RoPE`.
- [func RoPE(MLXArray, dimensions: Int, traditional: Bool, base: Float?, scale: Float, offset: MLXArray, freqs: MLXArray?, stream: StreamOrDevice) -> MLXArray](./rope%28_,dimensions,traditional,base,scale,offset,freqs,stream%29-94hyd.md)
  Optimized implementation of `NN.RoPE` with array offset for batched inference.
- [func VJP(([MLXArray], [MLXArray]) -> [MLXArray]) -> MLXCustomFunctionComponent](./vjp%28_%29.md)
- [func arange(Int, Int, step: Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./arange%28_,_,step,dtype,stream%29-1amf4.md)
  Generate values in the half-open interval `[start, stop)` spaced by `step` with a given [`DType`](./dtype.md).
- [func arange(Double, Double, step: Double, dtype: DType, stream: StreamOrDevice) -> MLXArray](./arange%28_,_,step,dtype,stream%29-5ly9b.md)
  Generate values in the half-open interval `[start, stop)` spaced by `step` (floating point version).
- [func arange(Int, Int, step: Int, stream: StreamOrDevice) -> MLXArray](./arange%28_,_,step,stream%29.md)
  Generate values in the half-open interval `[start, stop)` spaced by `step`.
- [func arange(Double, dtype: DType, stream: StreamOrDevice) -> MLXArray](./arange%28_,dtype,stream%29-340a5.md)
  Generate values in the half-open interval `[0, stop)` (floating point version).
- [func arange(Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./arange%28_,dtype,stream%29-3umul.md)
  Generate values in the half-open interval `[0, stop)` with a given [`DType`](./dtype.md).
- [func arange(Int, stream: StreamOrDevice) -> MLXArray](./arange%28_,stream%29.md)
  Generate values in the half-open interval `[0, stop)`.
- [func bartlett(Int, stream: StreamOrDevice) -> MLXArray](./bartlett%28_,stream%29.md)
  Return the Bartlett window.
- [func bernoulli(some ScalarOrArray, (some Collection<Int>)?, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./bernoulli%28_,_,key,stream%29.md)
  Generate Bernoulli random values with a given `p` value.
- [func bernoulli(some Collection<Int>, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./bernoulli%28_,key,stream%29.md)
  Generate Bernoulli random values with a `p` value of 0.5.
- [func blackman(Int, stream: StreamOrDevice) -> MLXArray](./blackman%28_,stream%29.md)
  Return the Blackman window.
- [func categorical(MLXArray, axis: Int, count: Int, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./categorical%28_,axis,count,key,stream%29.md)
  Sample `count` values from a categorical distribution.
- [func categorical(MLXArray, axis: Int, shape: (some Collection<Int>)?, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./categorical%28_,axis,shape,key,stream%29.md)
  Sample from a categorical distribution.
- [func checkedEval(some Sequence<Any>) throws](./checkedeval%28_%29-64rcz.md)
  Variant of [`eval(_:)`](./eval%28_%29-91pbd.md) that checks for errors in MLX and throws.
- [func checkedEval(Any...) throws](./checkedeval%28_%29-7a4cs.md)
  Variant of [`eval(_:)`](./eval%28_%29-45gpq.md) that checks for errors in MLX and throws.
- [func cholesky(MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./cholesky%28_,upper,stream%29.md)
  Compute the Cholesky decomposition of a real symmetric positive semi-definite matrix.
- [func choleskyInv(MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./choleskyinv%28_,upper,stream%29.md)
  Compute the inverse of a real symmetric positive semi-definite matrix using it’s Cholesky decomposition.
- [func clip(MLXArray, min: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./clip%28_,min,stream%29.md)
  Clip the values of the array between the given minimum and maximum.
- [func compile(inputs: [any Updatable], outputs: [any Updatable], shapeless: Bool, (MLXArray, MLXArray, MLXArray) -> MLXArray) -> (MLXArray, MLXArray, MLXArray) -> MLXArray](./compile%28inputs,outputs,shapeless,_%29-36fp4.md)
  Overload of [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) that takes three [`MLXArray`](./mlxarray.md) and produces a single [`MLXArray`](./mlxarray.md).
- [func contiguous(MLXArray, allowColMajor: Bool, stream: StreamOrDevice) -> MLXArray](./contiguous%28_,allowcolmajor,stream%29.md)
  Force an array to be row contiguous. Copy if necessary.
- [func cross(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./cross%28_,_,axis,stream%29.md)
  Compute the cross product of two arrays along a specified axis.
- [func det(MLXArray, stream: StreamOrDevice) -> MLXArray](./det%28_,stream%29.md)
  Compute the determinant of a square matrix.
- [func diff(MLXArray, n: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./diff%28_,n,axis,stream%29.md)
  The n-th discrete difference along the given axis.
- [func eig(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./eig%28_,stream%29.md)
  Compute the eigenvalues and eigenvectors of a square matrix.
- [func eigh(MLXArray, UPLO: String, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./eigh%28_,uplo,stream%29.md)
  Compute the eigenvalues and eigenvectors of a complex Hermitian or real symmetric matrix.
- [func eigvals(MLXArray, stream: StreamOrDevice) -> MLXArray](./eigvals%28_,stream%29.md)
  Compute the eigenvalues of a square matrix.
- [func eigvalsh(MLXArray, UPLO: String, stream: StreamOrDevice) -> MLXArray](./eigvalsh%28_,uplo,stream%29.md)
  Compute the eigenvalues of a complex Hermitian or real symmetric matrix.
- [func exportFunction(to: URL, shapeless: Bool, ([MLXArray]) -> [MLXArray]) -> FunctionExporterSingle](./exportfunction%28to,shapeless,_%29.md)
  Export a function to a `.mlxfn` file.
- [func exportFunctions(to: URL, shapeless: Bool, ([MLXArray]) -> [MLXArray], build: (FunctionExporterMultiple) throws -> Void) throws](./exportfunctions%28to,shapeless,_,build%29.md)
  Export multiple traces of a function to a `.mlxfn` file.
- [func exportToDot([MLXArray], namer: NodeNamer?) -> String](./exporttodot%28_,namer%29.md)
  A [GraphViz](https://graphviz.org) `DOT` representation of the compute graph that produces `outputs`.
- [func eye(Int, m: Int?, k: Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./eye%28_,m,k,dtype,stream%29.md)
  Create an identity matrix or a general diagonal matrix given a [`DType`](./dtype.md).
- [func fft(MLXArray, n: Int?, axis: Int, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./fft%28_,n,axis,norm,stream%29.md)
  One dimensional discrete Fourier Transform.
- [func fft2(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./fft2%28_,s,axes,norm,stream%29.md)
  Two dimensional discrete Fourier Transform.
- [func fftfreq(Int, d: Double, stream: StreamOrDevice) -> MLXArray](./fftfreq%28_,d,stream%29.md)
  The sample frequencies of a discrete Fourier Transform.
- [func fftn(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./fftn%28_,s,axes,norm,stream%29.md)
  n-dimensional discrete Fourier Transform.
- [func fftshift(MLXArray, axes: [Int]?, stream: StreamOrDevice) -> MLXArray](./fftshift%28_,axes,stream%29.md)
  Shift the zero-frequency component to the center of the spectrum.
- [func flatten(MLXArray, startAxis: Int, endAxis: Int, stream: StreamOrDevice) -> MLXArray](./flatten%28_,startaxis,endaxis,stream%29.md)
  Flatten an array.
- [func flipped(MLXArray, axes: [Int]?, stream: StreamOrDevice) -> MLXArray](./flipped%28_,axes,stream%29.md)
  Reverse the order of elements along the given axes.
- [func flipped(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./flipped%28_,axis,stream%29.md)
  Reverse the order of elements along the given axis.
- [func fromFP8(MLXArray, dtype: DType, stream: StreamOrDevice) -> MLXArray](./fromfp8%28_,dtype,stream%29.md)
  Convert an E4M3 FP8 array to the given floating-point [`DType`](./dtype.md).
- [func full(some Collection<Int>, values: MLXArray, dtype: DType, stream: StreamOrDevice) -> MLXArray](./full%28_,values,dtype,stream%29.md)
  Construct an array with the given value and a given [`DType`](./dtype.md).
- [func gatherMatmul(MLXArray, MLXArray, lhsIndices: MLXArray?, rhsIndices: MLXArray?, sortedIndices: Bool, stream: StreamOrDevice) -> MLXArray](./gathermatmul%28_,_,lhsindices,rhsindices,sortedindices,stream%29.md)
- [func gatherQuantizedMatmul(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, lhsIndices: MLXArray?, rhsIndices: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, sortedIndices: Bool, stream: StreamOrDevice) -> MLXArray](./gatherquantizedmatmul%28_,_,scales,biases,lhsindices,rhsindices,transpose,groupsize,bits,mode,sortedindices,stream%29.md)
- [func graphDescription([MLXArray], namer: NodeNamer?) -> String](./graphdescription%28_,namer%29.md)
  A textual description of the compute graph that produces `outputs`.
- [func gumbel(some Collection<Int>, dtype: DType, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./gumbel%28_,dtype,key,stream%29.md)
  Sample from the standard Gumbel distribution with a given `DType`.
- [func gumbel(some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./gumbel%28_,type,key,stream%29.md)
  Sample from the standard Gumbel distribution.
- [func hamming(Int, stream: StreamOrDevice) -> MLXArray](./hamming%28_,stream%29.md)
  Return the Hamming window.
- [func hanning(Int, stream: StreamOrDevice) -> MLXArray](./hanning%28_,stream%29.md)
  Return the Hanning window.
- [func identity(Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./identity%28_,dtype,stream%29.md)
  Create a square identity matrix with a given [`DType`](./dtype.md).
- [func ifft(MLXArray, n: Int?, axis: Int, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./ifft%28_,n,axis,norm,stream%29.md)
  One dimensional inverse discrete Fourier Transform.
- [func ifft2(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./ifft2%28_,s,axes,norm,stream%29.md)
  Two dimensional inverse discrete Fourier Transform.
- [func ifftn(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./ifftn%28_,s,axes,norm,stream%29.md)
  n-dimensional inverse discrete Fourier Transform.
- [func ifftshift(MLXArray, axes: [Int]?, stream: StreamOrDevice) -> MLXArray](./ifftshift%28_,axes,stream%29.md)
  The inverse of [`fftshift(_:axes:stream:)`](./fftshift%28_,axes,stream%29.md).
- [func importFunction(from: URL) throws -> ImportedFunction](./importfunction%28from%29.md)
  Imports a function from a `.mlxfn` file.
- [func inv(MLXArray, stream: StreamOrDevice) -> MLXArray](./inv%28_,stream%29.md)
  Compute the inverse of a square matrix.
- [func irfft(MLXArray, n: Int?, axis: Int, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./irfft%28_,n,axis,norm,stream%29.md)
  Inverse one dimensional discrete Fourier Transform on a real input.
- [func irfft2(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./irfft2%28_,s,axes,norm,stream%29.md)
  Inverse two dimensional discrete Fourier Transform on a real input.
- [func irfftn(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./irfftn%28_,s,axes,norm,stream%29.md)
  Inverse n-dimensional discrete Fourier Transform on a real input.
- [func key(UInt64) -> MLXArray](./key%28_%29.md)
  Get a PRNG key from a seed.
- [func kron(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./kron%28_,_,stream%29.md)
  Compute the Kronecker product of two arrays `a` and `b`.
- [func laplace(some Collection<Int>, dtype: DType, loc: Float, scale: Float, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./laplace%28_,dtype,loc,scale,key,stream%29.md)
  Sample numbers from a Laplace distribution.
- [func layerNorm(MLXArray, weight: MLXArray?, bias: MLXArray?, eps: Float, stream: StreamOrDevice) -> MLXArray](./layernorm%28_,weight,bias,eps,stream%29.md)
  Layer normalization.
- [func loadArrays(data: Data, stream: StreamOrDevice) throws -> [String : MLXArray]](./loadarrays%28data,stream%29.md)
  Load dictionary of [`MLXArray`](./mlxarray.md) from a `safetensors` `Data`.
- [func loadArraysAndMetadata(data: Data, stream: StreamOrDevice) throws -> ([String : MLXArray], [String : String])](./loadarraysandmetadata%28data,stream%29.md)
  Load dictionary of [`MLXArray`](./mlxarray.md) and metadata from a `safetensors` `Data`.
- [func lu(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray, MLXArray)](./lu%28_,stream%29.md)
  Compute the LU factorization of the given matrix `A`.
- [func lu_factor(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./lu_factor%28_,stream%29.md)
  Computes a compact representation of the LU factorization.
- [func meshGrid(some Collection<MLXArray>, sparse: Bool, indexing: MeshGridIndexing, stream: StreamOrDevice) -> [MLXArray]](./meshgrid%28_,sparse,indexing,stream%29.md)
  Generate multidimensional coordinate grids from 1-D coordinate arrays
- [func multivariateNormal(mean: MLXArray, covariance: MLXArray, shape: some Collection<Int>, dtype: DType, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./multivariatenormal%28mean,covariance,shape,dtype,key,stream%29.md)
  Generate jointly-normal random samples given a mean and covariance.
- [func norm(MLXArray, ord: MLXLinalg.NormKind?, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axes,keepdims,stream%29.md)
  Matrix or vector norm.
- [func norm(MLXArray, ord: Double, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axis,keepdims,stream%29-23aay.md)
  Matrix or vector norm.
- [func norm(MLXArray, ord: Double, axis: IntOrArray?, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axis,keepdims,stream%29-8enew.md)
  Matrix or vector norm.
- [func norm(MLXArray, ord: MLXLinalg.NormKind?, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axis,keepdims,stream%29-9izss.md)
  Matrix or vector norm.
- [func norm(MLXArray, ord: MLXLinalg.NormKind?, axis: IntOrArray?, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axis,keepdims,stream%29-9umyu.md)
  Matrix or vector norm.
- [func normal(some Collection<Int>, dtype: DType, loc: Float, scale: Float, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./normal%28_,dtype,loc,scale,key,stream%29.md)
  Generate normally distributed random numbers.
- [func normal(some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, loc: Float, scale: Float, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./normal%28_,type,loc,scale,key,stream%29.md)
  Generate normally distributed random numbers.
- [func ones(some Collection<Int>, dtype: DType, stream: StreamOrDevice) -> MLXArray](./ones%28_,dtype,stream%29.md)
  Construct an array of ones with a given [`DType`](./dtype.md)
- [func pinv(MLXArray, stream: StreamOrDevice) -> MLXArray](./pinv%28_,stream%29.md)
  Compute the (Moore-Penrose) pseudo-inverse of a matrix.
- [func positive(MLXArray, stream: StreamOrDevice) -> MLXArray](./positive%28_,stream%29.md)
  Element-wise unary plus. Returns a copy of the input.
- [func putAlong(MLXArray, MLXArray, values: MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./putalong%28_,_,values,axis,stream%29.md)
  Put values along an axis at the specified indices.
- [func putAlong(MLXArray, MLXArray, values: MLXArray, stream: StreamOrDevice) -> MLXArray](./putalong%28_,_,values,stream%29.md)
  Put values along an axis at the specified indices in a flattened array.
- [func qr(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./qr%28_,stream%29.md)
  The QR factorization of the input matrix.
- [func randInt(Range<some HasDType & BinaryInteger>, some Collection<Int>, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./randint%28_,_,key,stream%29.md)
  Generate random integers from the given interval using a `RangeExpression<Int>`.
- [func randInt(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./randint%28low,high,_,key,stream%29.md)
  Generate random integers from the given interval (`low:` and `high:`).
- [func randInt(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, type: (some HasDType & BinaryInteger).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./randint%28low,high,_,type,key,stream%29.md)
  Generate random integers from the given interval (`low:` and `high:`) with a given type, e.g. `Int8.self`.
- [func resolve(key: (some RandomStateOrKey)?) -> MLXArray](./resolve%28key%29.md)
  Resolve the given key to a concrete MLXArray (random key).
- [func rfft(MLXArray, n: Int?, axis: Int, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./rfft%28_,n,axis,norm,stream%29.md)
  One dimensional discrete Fourier Transform on a real input.
- [func rfft2(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./rfft2%28_,s,axes,norm,stream%29.md)
  Two dimensional real discrete Fourier Transform.
- [func rfftfreq(Int, d: Double, stream: StreamOrDevice) -> MLXArray](./rfftfreq%28_,d,stream%29.md)
  The sample frequencies of a discrete Fourier Transform on a real input.
- [func rfftn(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./rfftn%28_,s,axes,norm,stream%29.md)
  n-dimensional real discrete Fourier Transform.
- [func rmsNorm(MLXArray, weight: MLXArray, eps: Float, stream: StreamOrDevice) -> MLXArray](./rmsnorm%28_,weight,eps,stream%29.md)
  Root Mean Square normalization (RMS norm).
- [func saveToData(arrays: [String : MLXArray], metadata: [String : String]) throws -> Data](./savetodata%28arrays,metadata%29.md)
  Save dictionary of arrays in `safetensors` format into `Data`.
- [func scaledDotProductAttention(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXArray?, memoryEfficientThreshold: Int?, stream: StreamOrDevice) -> MLXArray](./scaleddotproductattention%28queries,keys,values,scale,mask,memoryefficientthreshold,stream%29.md)
  A fast implementation of multi-head attention: `O = softmax(Q @ K.T, dim=-1) @ V`
- [func search(sorted: MLXArray, values: MLXArray, side: SearchSortedSide, stream: StreamOrDevice) -> MLXArray](./search%28sorted,values,side,stream%29.md)
  Find the indices that keep `sorted` sorted when inserting `values`.
- [func seed(UInt64)](./seed%28_%29.md)
  Seed the global PRNG.
- [func slogdet(MLXArray, stream: StreamOrDevice) -> (sign: MLXArray, logabsdet: MLXArray)](./slogdet%28_,stream%29.md)
  Compute the sign and natural log of the absolute value of the determinant of a square matrix.
- [func solve(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./solve%28_,_,stream%29.md)
  Compute the solution to a system of linear equations `AX = B`.
- [func solveTriangular(MLXArray, MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./solvetriangular%28_,_,upper,stream%29.md)
  Computes the solution of a triangular system of linear equations `AX = B`.
- [func split(key: MLXArray, into: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28key,into,stream%29.md)
  Split a PRNG key into sub keys.
- [func split(key: MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./split%28key,stream%29.md)
  Split a PRNG key into two keys and return a tuple.
- [func stride(from: Int?, to: Int?, by: Int?) -> MLXSlice](./stride%28from,to,by%29.md)
  Replacement for `Swift.stride(from:to:by:)` for MLXArray indexing.
- [func svd(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray, MLXArray)](./svd%28_,stream%29.md)
  The Singular Value Decomposition (SVD) of the input matrix.
- [func tensordot(MLXArray, MLXArray, axes: (some Collection<Int>, some Collection<Int>), stream: StreamOrDevice) -> MLXArray](./tensordot%28_,_,axes,stream%29-5ne6c.md)
  Compute tensor dot product.
- [func toFP8(MLXArray, stream: StreamOrDevice) -> MLXArray](./tofp8%28_,stream%29.md)
  Convert a floating-point array to E4M3 FP8 bytes.
- [func tri(Int, m: Int?, k: Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./tri%28_,m,k,dtype,stream%29.md)
  An array with ones at and below the given diagonal and zeros elsewhere and a given [`DType`](./dtype.md).
- [func triInv(MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./triinv%28_,upper,stream%29.md)
  Compute the inverse of a triangular square matrix.
- [func trunc(MLXArray, stream: StreamOrDevice) -> MLXArray](./trunc%28_,stream%29.md)
  Element-wise truncation towards zero.
- [func truncatedNormal(Range<Float>, some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./truncatednormal%28_,_,type,key,stream%29-7d8ep.md)
  Generate values from a truncated normal distribution in a given `RangeExpression<Float>`.
- [func truncatedNormal(Range<some HasDType & Comparable>, some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./truncatednormal%28_,_,type,key,stream%29-7mahq.md)
  Generate values from a truncated normal distribution.
- [func truncatedNormal(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, dtype: DType, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./truncatednormal%28low,high,_,dtype,key,stream%29.md)
  Generate values from a truncated normal distribution between `low` and `high` with a given `DType`.
- [func truncatedNormal(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./truncatednormal%28low,high,_,type,key,stream%29.md)
  Generate values from a truncated normal distribution between `low` and `high`.
- [func unflatten(MLXArray, axis: Int, shape: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./unflatten%28_,axis,shape,stream%29.md)
  Unflatten an axis of an array to a shape.
- [func uniform(Range<some HasDType & Comparable>, some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./uniform%28_,_,type,key,stream%29-7r5z8.md)
  Generate uniformly distributed random numbers with a `RangeExpression`.
- [func uniform(Range<Float>, some Collection<Int>, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./uniform%28_,_,type,key,stream%29-8apf7.md)
  Generate uniformly distributed random numbers with a `RangeExpression<Float>` (specialization).
- [func uniform(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, dtype: DType, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./uniform%28low,high,_,dtype,key,stream%29.md)
  Generate uniformly distributed random numbers between `low` and `high` with a given `DType`.
- [func uniform(low: some ScalarOrArray, high: some ScalarOrArray, (some Collection<Int>)?, type: (some HasDType & BinaryFloatingPoint).Type, key: (some RandomStateOrKey)?, stream: StreamOrDevice) -> MLXArray](./uniform%28low,high,_,type,key,stream%29.md)
  Generate uniformly distributed random numbers between `low` and `high`.
- [func unstacked(MLXArray, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./unstacked%28_,axis,stream%29.md)
  Split an array into a sequence of arrays along the given axis.
- [func vecdot(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./vecdot%28_,_,axis,stream%29.md)
  Compute the vector dot product of two arrays along an axis.
- [func vmap(([MLXArray]) -> [MLXArray], inAxes: some Sequence<Optional<Int>>, outAxes: some Sequence<Optional<Int>>) -> ([MLXArray]) -> [MLXArray]](./vmap%28_,inaxes,outaxes%29-124np.md)
  Returns a vectorized version of `f()`.
- [func vmap((MLXArray) -> MLXArray, inAxes: Int?, outAxes: Int?) -> (MLXArray) -> MLXArray](./vmap%28_,inaxes,outaxes%29-3v2jj.md)
  Overload of [`vmap(_:inAxes:outAxes:)`](./vmap%28_,inaxes,outaxes%29-3v2jj.md) for a single [`MLXArray`](./mlxarray.md) input and output.
- [func vmap((MLXArray, MLXArray) -> MLXArray, inAxes: (Int?, Int?), outAxes: Int?) -> (MLXArray, MLXArray) -> MLXArray](./vmap%28_,inaxes,outaxes%29-5rcj4.md)
  Overload of [`vmap(_:inAxes:outAxes:)`](./vmap%28_,inaxes,outaxes%29-5rcj4.md) for two [`MLXArray`](./mlxarray.md) inputs and a single [`MLXArray`](./mlxarray.md) output.
- [func withError<R>((ErrorBox) throws -> R) throws -> R](./witherror%28_%29-2wfiu.md)
  Evaluate the block and convert MLX errors into Swift `throws` with explicit visibility of the error.
- [func withError<R>(() async throws -> R) async throws -> R](./witherror%28_%29-4tvdu.md)
  Evaluate the block and convert MLX errors into Swift `throws` on block exit (async).
- [func withError<R>(() throws -> R) throws -> R](./witherror%28_%29-6g4wn.md)
  Evaluate the block and convert MLX errors into Swift `throws` on block exit.
- [func withError<R>((ErrorBox) async throws -> R) async throws -> R](./witherror%28_%29-7f0hv.md)
  Evaluate the block and convert MLX errors into Swift `throws` with explicit visibility of the error (async).
- [func withErrorHandler<R>((String) -> Void, () throws -> R) rethrows -> R](./witherrorhandler%28_,_%29-4ll5b.md)
  Evaluate the block with a scoped MLX error handler.
- [func withErrorHandler<R>((String) -> Void, () async throws -> R) async rethrows -> R](./witherrorhandler%28_,_%29-67l6g.md)
  Evaluate the block with a scoped MLX error handler (async).
- [func withRandomState<R>(MLXRandom.RandomState, body: () async throws -> R) async rethrows -> R](./withrandomstate%28_,body%29-18ob4.md)
  Use the given [`MLXRandom.RandomState`](./mlxrandom/randomstate.md) scoped to the current task and body.
- [func withRandomState<R>(MLXRandom.RandomState, body: () throws -> R) rethrows -> R](./withrandomstate%28_,body%29-6i2p1.md)
  Use the given [`MLXRandom.RandomState`](./mlxrandom/randomstate.md) scoped to the current task and body.
- [func zeros(some Collection<Int>, dtype: DType, stream: StreamOrDevice) -> MLXArray](./zeros%28_,dtype,stream%29.md)
  Construct an array of zeros with a given [`DType`](./dtype.md)
### Type Aliases
- [typealias MLXLogHandlerFactory](./mlxloghandlerfactory.md)
### Enumerations
- [enum ConvolveMode](./convolvemode.md)
  Mode for [`convolve(_:_:mode:stream:)`](./convolve%28_,_,mode,stream%29.md)
- [enum FFTNorm](./fftnorm.md)
  Normalization mode for discrete Fourier Transforms.
- [enum LoadSaveError](./loadsaveerror.md)
- [enum LogLevel](./loglevel.md)
- [enum MLXArrayIndexOperation](./mlxarrayindexoperation.md)
  MLXArray index operations.
- [enum MLXCustomFunctionBuilder](./mlxcustomfunctionbuilder.md)
- [enum MLXCustomFunctionComponent](./mlxcustomfunctioncomponent.md)
- [enum MLXError](./mlxerror.md)
  Error type for caught errors during [`withError(_:)`](./witherror%28_%29-6g4wn.md).
- [enum MLXFFT](./mlxfft.md)
- [enum MLXFast](./mlxfast.md)
- [enum MLXLinalg](./mlxlinalg.md)
- [enum MLXRandom](./mlxrandom.md)
  Collection of functions related to random number generation.
- [enum Memory](./memory.md)
  Properties to control the the memory allocation and buffer reuse.
- [enum MeshGridIndexing](./meshgridindexing.md)
  Indexing mode for [`meshGrid(_:sparse:indexing:stream:)`](./meshgrid%28_,sparse,indexing,stream%29.md).
- [enum PadMode](./padmode.md)
  Mode for [`padded(_:width:mode:value:stream:)`](./padded%28_,width,mode,value,stream%29.md)
- [enum QuantizationMode](./quantizationmode.md)
  Quantization modes for weight compression in neural networks.
- [enum SearchSortedSide](./searchsortedside.md)
- [enum WiredMemoryTicketKind](./wiredmemoryticketkind.md)
  Describes whether a ticket represents active work or a long-lived reservation.
### Extended Modules
- [ComplexModule](./complexmodule.md)
- [Swift](./swift.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx)*