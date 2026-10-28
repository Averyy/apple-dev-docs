---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/converting-python"
framework: "mlx-swift/MLX"
---

# Converting From Python

**Framework**: mlx-swift/MLX  
**Role**: Article

Common patterns from python and mapping `mlx` function names.

## Indexing

[`MLXArray`](./mlxarray.md) supports all the same indexing (see [Indexing](./indexing.md)) as the python `mx.array`, though in some cases they are written differently. In all cases both `MLXArray` and `mx.array` indexing strive to match [numpy indexing](https://numpy.org/doc/stable/user/basics.indexing.html).

Here is a mapping of some observed calls:

| Python code | Swift Code |
| --- | --- |
| `array[10]` | `array[10]` |
| `array[-1]` | `array[-1]` – this works on [`MLXArray`](./mlxarray.md) but not swift arrays in general. |
| `array.shape[0]` | `array.dim(0)` or `array.shape[0]` |
| `array.shape[-1]` | `array.dim(-1)` |
| `array[1, 2, 3]` | `array[1, 2, 3]` |
| `array[2:8]` | `array[2 ..< 8]` |
| `array[:, :8, 8:]` | `array[0..., ..<8, 8...]` |
| `array[array2]` | `array[array2]` |
| `array[array2, array3]` | `array[array2, array3]` – [numpy style advanced indexing](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing) |
| `array[None]` | `array[.newAxis]` |
| `array[:, None]` | `array[0..., .newAxis]` |
| `array[..., None]` | `array[.ellipsis, .newAxis]` |
| `array[:, -1, :]` | `array[0..., -1, 0...]` |
| `array[..., ::2]` | `array[.ellipsis, .stride(by: 2)]` |
| `array[::-1]` | `array[.stride(by: -1)]` – reverse first dimension of array |
| `array[..., ::-1]` | `array[.ellipsis, stride(by: -1)]` – reverse last dimension of array |
| `array.shape[:-1]` | `array.shape.dropLast()` |

See [Indexing](./indexing.md) for more information.

## Name Mapping

### Swift Naming

Note that the element-wise logical operations such as:

- [`.==(_:_:)`](./mlxarray/doteqeq%28_,_%29-56m0a.md)
- [`.==(_:_:)`](./mlxarray/doteqeq%28_,_%29-79hbc.md)

are named using the Swift convention for SIMD operations, e.g. `.==`, `.<`, etc.  These operators produce a new [`MLXArray`](./mlxarray.md) with `true`/`false` values for the elementwise comparison.

Functions and method are typically named in a similar fashion changing `snake_case` to `camelCase`.  A few exceptions to that rule follow swift naming for functions that have no side effects.  For example:

- `flatten()` becomes [`flattened(_:start:end:stream:)`](./flattened%28_,start,end,stream%29.md)
- `reshape()` becomes [`reshaped(_:_:stream:)`](./reshaped%28_,_,stream%29-96lgr.md)
- `moveaxis()` becomes [`movedAxis(_:source:destination:stream:)`](./movedaxis%28_,source,destination,stream%29.md)

and so on.

### mx.array methods

Here is a mapping of python `mx.array` methods to their [`MLXArray`](./mlxarray.md) counterparts.
Note: some of the symbols are not linkable.

| `mx.array` method | [`MLXArray`](./mlxarray.md) method |
| --- | --- |
| `__init__` | see [Initialization](./initialization.md) |
| `__repr__` | [`description`](./mlxarray/description.md) |
| `__eq__` | [`.==(_:_:)`](./mlxarray/doteqeq%28_,_%29-56m0a.md) |
| `size` | [`size`](./mlxarray/size.md) |
| `ndim` | [`ndim`](./mlxarray/ndim.md) |
| `itemsize` | [`itemSize`](./mlxarray/itemsize.md) |
| `nbytes` | [`nbytes`](./mlxarray/nbytes.md) |
| `shape` | [`shape`](./mlxarray/shape.md) or [`shape2`](./mlxarray/shape2.md) … [`shape4`](./mlxarray/shape4.md) (destructuring) |
| `dtype` | [`dtype`](./mlxarray/dtype.md) |
| `item` | [`item(_:)`](./mlxarray/item%28_%29.md) |
| `tolist` | [`asArray(_:)`](./mlxarray/asarray%28_%29.md) |
| `astype` | [`MLXArray`](./mlxarray.md) or [`asType(_:stream:)`](./mlxarray/astype%28_,stream%29-6d44y.md) |
| `__getitem__` | [`MLXArray`](./mlxarray.md) |
| `__len__` | [`count`](./mlxarray/count.md) |
| `__iter__` | implements `Sequence` |
| `__add__` | [`+(_:_:)`](./mlxarray/plus%28_,_%29-1rv98.md) |
| `__iadd__` | [`MLXArray`](./mlxarray.md) |
| `__sub__` | [`MLXArray`](./mlxarray.md) |
| `__isub__` | [`MLXArray`](./mlxarray.md) |
| `__mul__` | [`*(_:_:)`](./mlxarray/star%28_,_%29-1z2ck.md) |
| `__imul__` | [`MLXArray`](./mlxarray.md) |
| `__truediv__` | [`/(_:_:)`](./mlxarray/op%28_,_%29-6ijef.md) |
| `__div__` | [`/(_:_:)`](./mlxarray/op%28_,_%29-6ijef.md) |
| `__idiv__` | [`MLXArray`](./mlxarray.md) |
| `__floordiv__` | [`floorDivide(_:stream:)`](./mlxarray/floordivide%28_,stream%29.md) |
| `__mod__` | [`%(_:_:)`](./mlxarray/op%28_,_%29-3ubwd.md) |
| `__eq__` | [`.==(_:_:)`](./mlxarray/doteqeq%28_,_%29-56m0a.md) |
| `__lt__` | [`.<(_:_:)`](./mlxarray/dotop%28_,_%29-9rzup.md) |
| `__le__` | [`.<=(_:_:)`](./mlxarray/dotopeq%28_,_%29-2a0s9.md) |
| `__gt__` | [`.>(_:_:)`](./mlxarray/dotop%28_,_%29-fwi1.md) |
| `__ge__` | [`.>=(_:_:)`](./mlxarray/dotopeq%28_,_%29-2gqml.md) |
| `__ne__` | [`.!=(_:_:)`](./mlxarray/dotnoteq%28_,_%29-mbw0.md) |
| `__neg__` | [`MLXArray`](./mlxarray.md) |
| `__bool__` | [`all(keepDims:stream:)`](./mlxarray/all%28keepdims,stream%29.md) + [`item()`](./mlxarray/item%28%29.md) |
| `__repr__` | [`description`](./mlxarray/description.md) |
| `__matmul__` | [`matmul(_:stream:)`](./mlxarray/matmul%28_,stream%29.md) |
| `__pow__` | [`**(_:_:)`](./mlxarray/starstar%28_,_%29-8xxt3.md) |
| `abs` | [`abs(stream:)`](./mlxarray/abs%28stream%29.md) |
| `all` | [`all(axes:keepDims:stream:)`](./mlxarray/all%28axes,keepdims,stream%29.md) |
| `any` | [`any(axes:keepDims:stream:)`](./mlxarray/any%28axes,keepdims,stream%29.md) |
| `argmax` | [`argMax(axis:keepDims:stream:)`](./mlxarray/argmax%28axis,keepdims,stream%29.md) |
| `argmin` | [`argMin(axis:keepDims:stream:)`](./mlxarray/argmin%28axis,keepdims,stream%29.md) |
| `cos` | [`cos(stream:)`](./mlxarray/cos%28stream%29.md) |
| `cummax` | [`cummax(axis:reverse:inclusive:stream:)`](./mlxarray/cummax%28axis,reverse,inclusive,stream%29.md) |
| `cummin` | [`cummin(axis:reverse:inclusive:stream:)`](./mlxarray/cummin%28axis,reverse,inclusive,stream%29.md) |
| `cumprod` | [`cumprod(axis:reverse:inclusive:dtype:stream:)`](./mlxarray/cumprod%28axis,reverse,inclusive,dtype,stream%29.md) |
| `cumsum` | [`cumsum(axis:reverse:inclusive:dtype:stream:)`](./mlxarray/cumsum%28axis,reverse,inclusive,dtype,stream%29.md) |
| `exp` | [`exp(stream:)`](./mlxarray/exp%28stream%29.md) |
| `flatten` | [`flattened(start:end:stream:)`](./mlxarray/flattened%28start,end,stream%29.md) |
| `log` | [`log(stream:)`](./mlxarray/log%28stream%29.md) |
| `log10` | [`log10(stream:)`](./mlxarray/log10%28stream%29.md) |
| `log1p` | [`log1p(stream:)`](./mlxarray/log1p%28stream%29.md) |
| `log2` | [`log2(stream:)`](./mlxarray/log2%28stream%29.md) |
| `logsumexp` | [`logSumExp(axes:keepDims:stream:)`](./mlxarray/logsumexp%28axes,keepdims,stream%29.md) |
| `max` | [`max(axes:keepDims:stream:)`](./mlxarray/max%28axes,keepdims,stream%29.md) |
| `mean` | [`mean(axes:keepDims:stream:)`](./mlxarray/mean%28axes,keepdims,stream%29.md) |
| `min` | [`min(axes:keepDims:stream:)`](./mlxarray/min%28axes,keepdims,stream%29.md) |
| `moveaxis` | [`movedAxis(source:destination:stream:)`](./mlxarray/movedaxis%28source,destination,stream%29.md) |
| `prod` | [`product(axes:keepDims:stream:)`](./mlxarray/product%28axes,keepdims,stream%29.md) |
| `reciprocal` | [`reciprocal(stream:)`](./mlxarray/reciprocal%28stream%29.md) |
| `reshape` | [`reshaped(_:stream:)`](./mlxarray/reshaped%28_,stream%29-2mzhh.md) |
| `round` | [`round(decimals:stream:)`](./mlxarray/round%28decimals,stream%29.md) |
| `rsqrt` | [`rsqrt(stream:)`](./mlxarray/rsqrt%28stream%29.md) |
| `sin` | [`sin(stream:)`](./mlxarray/sin%28stream%29.md) |
| `split` | [`split(parts:axis:stream:)`](./mlxarray/split%28parts,axis,stream%29.md) or [`split(axis:stream:)`](./mlxarray/split%28axis,stream%29.md) (destructuring) |
| `sqrt` | [`sqrt(stream:)`](./mlxarray/sqrt%28stream%29.md) |
| `square` | [`square(stream:)`](./mlxarray/square%28stream%29.md) |
| `squeeze` | [`squeezed(axes:stream:)`](./mlxarray/squeezed%28axes,stream%29.md) |
| `sum` | [`sum(axes:keepDims:stream:)`](./mlxarray/sum%28axes,keepdims,stream%29.md) |
| `swapaxes` | [`swappedAxes(_:_:stream:)`](./mlxarray/swappedaxes%28_,_,stream%29.md) |
| `T` | [`T`](./mlxarray/t.md) |
| `transpose` | [`transposed(_:stream:)`](./mlxarray/transposed%28_,stream%29.md) |
| `var` | [`variance(axes:keepDims:ddof:stream:)`](./mlxarray/variance%28axes,keepdims,ddof,stream%29.md) |

### mx free functions

This is a mapping of `mx` free functions to their [MLX](./MLX.md) counterparts.

| `mx.array` free function | [MLX](./MLX.md) free function |
| --- | --- |
| `abs` | [`abs(_:stream:)`](./abs%28_,stream%29.md) |
| `add` | [`add(_:_:stream:)`](./add%28_,_,stream%29.md) |
| `all` | [`all(_:axes:keepDims:stream:)`](./all%28_,axes,keepdims,stream%29.md) |
| `allclose` | [`allClose(_:_:rtol:atol:equalNaN:stream:)`](./allclose%28_,_,rtol,atol,equalnan,stream%29.md) |
| `any` | [`any(_:axes:keepDims:stream:)`](./any%28_,axes,keepdims,stream%29.md) |
| `arange` | [`arange(_:_:step:stream:)`](./arange%28_,_,step,stream%29.md) |
| `arccos` | [`acos(_:stream:)`](./acos%28_,stream%29.md) |
| `arccosh` | [`acosh(_:stream:)`](./acosh%28_,stream%29.md) |
| `arcsin` | [`asin(_:stream:)`](./asin%28_,stream%29.md) |
| `arcsinh` | [`asinh(_:stream:)`](./asinh%28_,stream%29.md) |
| `arctan` | [`atan(_:stream:)`](./atan%28_,stream%29.md) |
| `arctanh` | [`atanh(_:stream:)`](./atanh%28_,stream%29.md) |
| `argmax` | [`argMax(_:axis:keepDims:stream:)`](./argmax%28_,axis,keepdims,stream%29.md) |
| `argmin` | [`argMin(_:axis:keepDims:stream:)`](./argmin%28_,axis,keepdims,stream%29.md) |
| `argpartition` | [`argPartition(_:kth:axis:stream:)`](./argpartition%28_,kth,axis,stream%29.md) |
| `argsort` | [`argSort(_:axis:stream:)`](./argsort%28_,axis,stream%29.md) |
| `array_equal` | [`arrayEqual(_:_:equalNAN:stream:)`](./arrayequal%28_,_,equalnan,stream%29.md) |
| `as_strided` | [`asStrided(_:_:strides:offset:stream:)`](./asstrided%28_,_,strides,offset,stream%29.md) |
| `broadcast_to` | [`broadcast(_:to:stream:)`](./broadcast%28_,to,stream%29.md) |
| `ceil` | [`ceil(_:stream:)`](./ceil%28_,stream%29.md) |
| `clip` | [`clip(_:min:max:stream:)`](./clip%28_,min,max,stream%29.md) |
| `concatenate` | [`concatenated(_:axis:stream:)`](./concatenated%28_,axis,stream%29.md) |
| `conv1d` | [`conv1d(_:_:stride:padding:dilation:groups:stream:)`](./conv1d%28_,_,stride,padding,dilation,groups,stream%29.md) |
| `conv2d` | [`conv2d(_:_:stride:padding:dilation:groups:stream:)`](./conv2d%28_,_,stride,padding,dilation,groups,stream%29.md) |
| `convolve` | [`convolve(_:_:mode:stream:)`](./convolve%28_,_,mode,stream%29.md) |
| `cos` | [`cos(_:stream:)`](./cos%28_,stream%29.md) |
| `cosh` | [`cosh(_:stream:)`](./cosh%28_,stream%29.md) |
| `cummax` | [`cummax(_:axis:reverse:inclusive:stream:)`](./cummax%28_,axis,reverse,inclusive,stream%29.md) |
| `cummin` | [`cummin(_:axis:reverse:inclusive:stream:)`](./cummin%28_,axis,reverse,inclusive,stream%29.md) |
| `cumprod` | [`cumprod(_:axis:reverse:inclusive:dtype:stream:)`](./cumprod%28_,axis,reverse,inclusive,dtype,stream%29.md) |
| `cumsum` | [`cumsum(_:axis:reverse:inclusive:dtype:stream:)`](./cumsum%28_,axis,reverse,inclusive,dtype,stream%29.md) |
| `dequantize` | [`dequantized(_:scales:biases:groupSize:bits:mode:globalScale:dtype:stream:)`](./dequantized%28_,scales,biases,groupsize,bits,mode,globalscale,dtype,stream%29.md) |
| `divide` | [`divide(_:_:stream:)`](./divide%28_,_,stream%29.md) |
| `equal` | [`equal(_:_:stream:)`](./equal%28_,_,stream%29.md) |
| `erf` | [`erf(_:stream:)`](./erf%28_,stream%29.md) |
| `erfinv` | [`erfInverse(_:stream:)`](./erfinverse%28_,stream%29.md) |
| `exp` | [`exp(_:stream:)`](./exp%28_,stream%29.md) |
| `expand_dims` | [`expandedDimensions(_:axes:stream:)`](./expandeddimensions%28_,axes,stream%29.md) |
| `eye` | [`eye(_:m:k:type:stream:)`](./mlxarray/eye%28_,m,k,type,stream%29.md) |
| `flatten` | [`flattened(_:start:end:stream:)`](./flattened%28_,start,end,stream%29.md) |
| `floor` | [`floor(_:stream:)`](./floor%28_,stream%29.md) |
| `floor_divide` | [`floorDivide(_:_:stream:)`](./floordivide%28_,_,stream%29.md) |
| `full` | [`full(_:values:type:stream:)`](./mlxarray/full%28_,values,type,stream%29.md) |
| `greater` | [`greater(_:_:stream:)`](./greater%28_,_,stream%29.md) |
| `greater_equal` | [`greaterEqual(_:_:stream:)`](./greaterequal%28_,_,stream%29.md) |
| `identity` | [`identity(_:type:stream:)`](./mlxarray/identity%28_,type,stream%29.md) |
| `less` | [`less(_:_:stream:)`](./less%28_,_,stream%29.md) |
| `less_equal` | [`lessEqual(_:_:stream:)`](./lessequal%28_,_,stream%29.md) |
| `linspace` | [`MLXArray`](./mlxarray.md) |
| `load` | [`loadArray(url:stream:)`](./loadarray%28url,stream%29.md) and [`loadArrays(url:stream:)`](./loadarrays%28url,stream%29.md) |
| `log` | [`log(_:stream:)`](./log%28_,stream%29.md) |
| `log10` | [`log10(_:stream:)`](./log10%28_,stream%29.md) |
| `log1p` | [`log1p(_:stream:)`](./log1p%28_,stream%29.md) |
| `log2` | [`log2(_:stream:)`](./log2%28_,stream%29.md) |
| `logaddexp` | [`logAddExp(_:_:stream:)`](./logaddexp%28_,_,stream%29.md) |
| `logical_not` | [`logicalNot(_:stream:)`](./logicalnot%28_,stream%29.md) |
| `logsumexp` | [`logSumExp(_:axes:keepDims:stream:)`](./logsumexp%28_,axes,keepdims,stream%29.md) |
| `matmul` | [`matmul(_:_:stream:)`](./matmul%28_,_,stream%29.md) |
| `max` | [`max(_:axes:keepDims:stream:)`](./max%28_,axes,keepdims,stream%29.md) |
| `maximum` | [`maximum(_:_:stream:)`](./maximum%28_,_,stream%29.md) |
| `mean` | [`mean(_:axes:keepDims:stream:)`](./mean%28_,axes,keepdims,stream%29.md) |
| `min` | [`min(_:axes:keepDims:stream:)`](./min%28_,axes,keepdims,stream%29.md) |
| `minimum` | [`minimum(_:_:stream:)`](./minimum%28_,_,stream%29.md) |
| `moveaxis` | [`movedAxis(_:source:destination:stream:)`](./movedaxis%28_,source,destination,stream%29.md) |
| `multiply` | [`multiply(_:_:stream:)`](./multiply%28_,_,stream%29.md) |
| `negative` | [`negative(_:stream:)`](./negative%28_,stream%29.md) |
| `not_equal` | [`notEqual(_:_:stream:)`](./notequal%28_,_,stream%29.md) |
| `ones` | [`ones(_:type:stream:)`](./mlxarray/ones%28_,type,stream%29.md) |
| `ones_like` | [`ones(like:dtype:stream:)`](./mlxarray/ones%28like,dtype,stream%29.md) |
| `pad` | [`padded(_:width:mode:value:stream:)`](./padded%28_,width,mode,value,stream%29.md) |
| `partition` | [`partitioned(_:kth:axis:stream:)`](./partitioned%28_,kth,axis,stream%29.md) |
| `power` | [`pow(_:_:stream:)`](./pow%28_,_,stream%29-8ie9c.md) |
| `prod` | [`product(_:axes:keepDims:stream:)`](./product%28_,axes,keepdims,stream%29.md) |
| `qqmm` | [`quantizedQuantizedMM(_:_:scales:groupSize:bits:mode:globalScaleX:globalScaleW:stream:)`](./quantizedquantizedmm%28_,_,scales,groupsize,bits,mode,globalscalex,globalscalew,stream%29.md) |
| `quantize` | [`quantized(_:groupSize:bits:mode:globalScale:stream:)`](./quantized%28_,groupsize,bits,mode,globalscale,stream%29.md) |
| `quantized_matmul` | [`quantizedMM(_:_:scales:biases:transpose:groupSize:bits:mode:stream:)`](./quantizedmm%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md) |
| `reciprocal` | [`reciprocal(_:stream:)`](./reciprocal%28_,stream%29.md) |
| `remainder` | [`remainder(_:_:stream:)`](./remainder%28_,_,stream%29.md) |
| `repeat` | [`repeated(_:count:axis:stream:)`](./repeated%28_,count,axis,stream%29.md) |
| `reshape` | [`reshaped(_:_:stream:)`](./reshaped%28_,_,stream%29-9w4n3.md) |
| `round` | [`round(_:decimals:stream:)`](./round%28_,decimals,stream%29.md) |
| `rsqrt` | [`rsqrt(_:stream:)`](./rsqrt%28_,stream%29.md) |
| `save` | [`save(array:url:stream:)`](./save%28array,url,stream%29.md) and [`save(arrays:metadata:url:stream:)`](./save%28arrays,metadata,url,stream%29.md) |
| `save_safetensors` | [`save(arrays:metadata:url:stream:)`](./save%28arrays,metadata,url,stream%29.md) |
| `savez` | not supported |
| `savez_compressed` | not supported |
| `sigmoid` | [`sigmoid(_:stream:)`](./sigmoid%28_,stream%29.md) |
| `sign` | [`sign(_:stream:)`](./sign%28_,stream%29.md) |
| `sin` | [`sin(_:stream:)`](./sin%28_,stream%29.md) |
| `sinh` | [`sinh(_:stream:)`](./sinh%28_,stream%29.md) |
| `softmax` | [`softmax(_:axes:precise:stream:)`](./softmax%28_,axes,precise,stream%29.md) |
| `sort` | [`sorted(_:axis:stream:)`](./sorted%28_,axis,stream%29.md) |
| `split` | [`split(_:parts:axis:stream:)`](./split%28_,parts,axis,stream%29.md) |
| `sqrt` | [`sqrt(_:stream:)`](./sqrt%28_,stream%29.md) |
| `square` | [`square(_:stream:)`](./square%28_,stream%29.md) |
| `squeeze` | [`squeezed(_:axes:stream:)`](./squeezed%28_,axes,stream%29.md) |
| `stack` | [`stacked(_:axis:stream:)`](./stacked%28_,axis,stream%29.md) |
| `stop_gradient` | [`stopGradient(_:stream:)`](./stopgradient%28_,stream%29.md) |
| `subtract` | [`subtract(_:_:stream:)`](./subtract%28_,_,stream%29.md) |
| `sum` | [`sum(_:axes:keepDims:stream:)`](./sum%28_,axes,keepdims,stream%29.md) |
| `swapaxes` | [`swappedAxes(_:_:_:stream:)`](./swappedaxes%28_,_,_,stream%29.md) |
| `take` | [`take(_:_:axis:stream:)`](./take%28_,_,axis,stream%29.md) |
| `take_along_axis` | [`takeAlong(_:_:axis:stream:)`](./takealong%28_,_,axis,stream%29.md) |
| `tan` | [`tan(_:stream:)`](./tan%28_,stream%29.md) |
| `tanh` | [`tanh(_:stream:)`](./tanh%28_,stream%29.md) |
| `topk` | [`top(_:k:axis:stream:)`](./top%28_,k,axis,stream%29.md) |
| `transpose` | [`transposed(_:axes:stream:)`](./transposed%28_,axes,stream%29.md) |
| `tri` | [`tri(_:m:k:type:stream:)`](./mlxarray/tri%28_,m,k,type,stream%29.md) |
| `tril` | [`tril(_:k:stream:)`](./tril%28_,k,stream%29.md) |
| `triu` | [`triu(_:k:stream:)`](./triu%28_,k,stream%29.md) |
| `var` | [`variance(_:axes:keepDims:ddof:stream:)`](./variance%28_,axes,keepdims,ddof,stream%29.md) |
| `where` | [`which(_:_:_:stream:)`](./which%28_,_,_,stream%29.md) |
| `zeros` | [`zeros(_:type:stream:)`](./mlxarray/zeros%28_,type,stream%29.md) |
| `zeros_like` | [`zeros(like:dtype:stream:)`](./mlxarray/zeros%28like,dtype,stream%29.md) |

## See Also

### MLX
- [Installation](./install.md)
  How to install and use.
- [Troubleshooting](./troubleshooting.md)
  Help with problems you might run into.
- [MLX Swift Examples](./examples.md)
  Swift example code for MLX and MLXNN.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/converting-python)*