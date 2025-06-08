# Using vDSP for vector-based arithmetic

**Framework**: Accelerate

Increase the performance of common mathematical tasks with vDSP vector-vector and vector-scalar operations.

#### Overview

vDSP provides a suite of general-purpose, high-performance arithmetic functions that are alternatives to `for` loops and `map` when applying operations on collections of floating-point values.

For example, the code below multiplies the element-wise sum of two arrays by a scalar value:

```swift
let a: [Float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let b: [Float] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
let c: Float = 2

let d = zip(a, b).map {
    ($0.0 + $0.1) * c
}

// d = [22.0, 44.0, 66.0, 88.0, 110.0, 132.0, 154.0, 176.0, 198.0, 220.0]
```

The vDSP version of the same operation runs significantly faster.

```swift
let d = [Float](unsafeUninitializedCapacity: a.count) {
    buffer, initializedCount in
    
    vDSP.multiply(addition: (a, b),
                  c,
                  result: &buffer)
    
    initializedCount = a.count
}

// d = [22.0, 44.0, 66.0, 88.0, 110.0, 132.0, 154.0, 176.0, 198.0, 220.0]
```

Many vDSP functions have a variant that returns the result.

```swift
let a: [Float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let b: [Float] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
let c: Float = 2

let d = vDSP.multiply(addition: (a, b),
                      c)
```

##### Available Arithmetic Functions

The following table summarizes the basic arithmetic functions available in vDSP. All functions are available in single- and double-precision variants.

In the  column, a subscript (for example, `a[i]`) indicates a vector, and no subscript (for example, `a`) indicates a scalar value.

| Operation | Function |
| --- | --- |
| `c[i] = a[i] + b` | [`add(_:_:)`](vdsp/add(_:_:)-53nh9.md) |
| `c[i] = a[i] + b[i]` | [`add(_:_:)`](vdsp/add(_:_:)-7swvf.md) |
| `c[i] = a[i] - b[i]` | [`subtract(_:_:)`](vdsp/subtract(_:_:)-9xmo8.md) |
| `c[i] = a[i] * b` | [`multiply(_:_:)`](vdsp/multiply(_:_:)-993yp.md) |
| `c[i] = a[i] * b[i]` | [`multiply(_:_:)`](vdsp/multiply(_:_:)-9zgw.md) |
| `c[i] = a[i] / b` | [`divide(_:_:)`](vdsp/divide(_:_:)-1uqmz.md) |
| `c[i] = a / b[i]` | [`divide(_:_:)`](vdsp/divide(_:_:)-70npt.md) |
| `o0[i] = i1[i] + i0[i]` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `o1[i] = i1[i] - i0[i]` | [`addSubtract(_:_:addResult:subtractResult:)`](vdsp/addsubtract(_:_:addresult:subtractresult:)-avzd.md) |
| `c[i] = a[i] / b[i]` | [`divide(_:_:)`](vdsp/divide(_:_:)-6nfsi.md) |
| `d[i] = (a[i] + b[i]) * c` | [`multiply(addition:_:)`](vdsp/multiply(addition:_:)-4fnbx.md) |
| `d[i] = (a[i] + b[i]) * c[i]` | [`multiply(addition:_:)`](vdsp/multiply(addition:_:)-7t59.md) |
| `d[i] = (a[i] - b[i]) * c` | [`multiply(subtraction:_:)`](vdsp/multiply(subtraction:_:)-106pt.md) |
| `d[i] = (a[i] - b[i]) * c[i]` | [`multiply(subtraction:_:)`](vdsp/multiply(subtraction:_:)-6y7g6.md) |
| `d[i] = (a[i] * b[i]) + c` | [`add(multiplication:_:)`](vdsp/add(multiplication:_:)-36vhq.md) |
| `d[i] = (a[i] * b) + c[i]` | [`add(multiplication:_:)`](vdsp/add(multiplication:_:)-7aut1.md) |
| `d[i] = (a[i] * b[i]) + c[i]` | [`add(multiplication:_:)`](vdsp/add(multiplication:_:)-9bgb2.md) |
| `d[i] = (a[i] * b[i]) - c[i]` | [`subtract(multiplication:_:)`](vdsp/subtract(multiplication:_:)-6u3sp.md) |
| `e[i] = (a[i] * b) + (c[i] * d)` | [`add(multiplication:multiplication:)`](vdsp/add(multiplication:multiplication:)-8rjh8.md) |
| `e[i] = (a[i] + b[i]) * (c[i] + d[i])` | [`multiply(addition:addition:)`](vdsp/multiply(addition:addition:)-1voy8.md) |
| `e[i] = (a[i] * b[i]) - (c[i] * d[i])` | [`subtract(multiplication:multiplication:)`](vdsp/subtract(multiplication:multiplication:)-1ghyu.md) |
| `e[i] = (a[i] - b[i]) * (c[i] - d[i])` | [`multiply(subtraction:subtraction:)`](vdsp/multiply(subtraction:subtraction:)-1rnom.md) |
| `e[i] = (a[i] + b[i]) * (c[i] - d[i])` | [`multiply(addition:subtraction:)`](vdsp/multiply(addition:subtraction:)-6h89l.md) |

## See Also

- [Controlling vDSP operations with stride](controlling-vdsp-operations-with-stride.md)
  Operate selectively on the elements of a vector at regular intervals.
- [Using linear interpolation to construct new data points](using-linear-interpolation-to-construct-new-data-points.md)
  Fill the gaps in arrays of numerical data using linear interpolation.
- [Resampling a signal with decimation](resampling-a-signal-with-decimation.md)
  Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.
- [vDSP](vdsp-library.md)
  Perform basic arithmetic operations and common digital signal processing (DSP) routines on large vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/using-vdsp-for-vector-based-arithmetic)*