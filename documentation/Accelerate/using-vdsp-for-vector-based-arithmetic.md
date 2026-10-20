# Using vDSP for vector-based arithmetic

**Framework**: Accelerate  
**Role**: Article

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

// The `d` equals [22.0, 44.0, 66.0, 88.0, 110.0, 132.0, 154.0, 176.0, 198.0, 220.0].
```

The vDSP version of the same operation runs significantly faster.

**Swift**:

```swift
let d = [Float](unsafeUninitializedCapacity: a.count) {
    buffer, initializedCount in
    
    vDSP.multiply(addition: (a, b),
                  c,
                  result: &buffer)
    
    initializedCount = a.count
}

// The `d` equals [22.0, 44.0, 66.0, 88.0, 110.0, 132.0, 154.0, 176.0, 198.0, 220.0].
```

**Objective-C**:

```objc
float d[10];

// Compute `d[i] = (a[i] + b[i]) * c`.
vDSP_vasm(a, 1, b, 1, &c, d, 1, 10);

// The `d` equals [22, 44, 66, 88, 110, 132, 154, 176, 198, 220].
```

Many vDSP functions have a variant that returns the result.

**Swift**:

```swift
let a: [Float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let b: [Float] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
let c: Float = 2

let d = vDSP.multiply(addition: (a, b),
                      c)
```

**Objective-C**:

```objc
// The low-level vDSP C interface has no result-returning variant; it
// always writes to a caller-supplied output buffer.
float a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
float b[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
float c = 2;
float d[10];

// Compute `d[i] = (a[i] + b[i]) * c`.
vDSP_vasm(a, 1, b, 1, &c, d, 1, 10);
```

##### Available arithmetic functions

The following table summarizes the basic arithmetic functions available in vDSP. All functions are available in single- and double-precision variants.

In the *Operation* column, a subscript (for example, `a[i]`) indicates a vector, and no subscript (for example, `a`) indicates a scalar value.

The *C function* column links to the equivalent low-level C interface. The Swift `vDSP` overlay (for example, [`multiply(_:_:)`](./vdsp/multiply%28_,_%29-993yp.md)) has no Objective-C interface; from C, call the underlying `vDSP_*` function shown here. Each C function also has a double-precision variant with a `D` suffix (for example, `vDSP_vsaddD`).

| Operation | Function | C function |
| --- | --- | --- |
| `c[i] = a[i] + b` | [`add(_:_:)`](./vdsp/add%28_,_%29-53nh9.md) | [`vDSP_vsadd`](./vdsp_vsadd.md) |
| `c[i] = a[i] + b[i]` | [`add(_:_:)`](./vdsp/add%28_,_%29-7swvf.md) | [`vDSP_vadd`](./vdsp_vadd.md) |
| `c[i] = a[i] - b[i]` | [`subtract(_:_:)`](./vdsp/subtract%28_,_%29-9xmo8.md) | [`vDSP_vsub`](./vdsp_vsub.md) |
| `c[i] = a[i] * b` | [`multiply(_:_:)`](./vdsp/multiply%28_,_%29-993yp.md) | [`vDSP_vsmul`](./vdsp_vsmul.md) |
| `c[i] = a[i] * b[i]` | [`multiply(_:_:)`](./vdsp/multiply%28_,_%29-9zgw.md) | [`vDSP_vmul`](./vdsp_vmul.md) |
| `c[i] = a[i] / b` | [`divide(_:_:)`](./vdsp/divide%28_,_%29-1uqmz.md) | [`vDSP_vsdiv`](./vdsp_vsdiv.md) |
| `c[i] = a / b[i]` | [`divide(_:_:)`](./vdsp/divide%28_,_%29-70npt.md) | [`vDSP_svdiv`](./vdsp_svdiv.md) |
| `o0[i] = i1[i] + i0[i]` ![](https://developer.apple.com/tutorials/images/com.apple.accelerate/spacer.png) `o1[i] = i1[i] - i0[i]` | [`addSubtract(_:_:addResult:subtractResult:)`](./vdsp/addsubtract%28_,_,addresult,subtractresult%29-avzd.md) | [`vDSP_vaddsub`](./vdsp_vaddsub.md) |
| `c[i] = a[i] / b[i]` | [`divide(_:_:)`](./vdsp/divide%28_,_%29-6nfsi.md) | [`vDSP_vdiv`](./vdsp_vdiv.md) |
| `d[i] = (a[i] + b[i]) * c` | [`multiply(addition:_:)`](./vdsp/multiply%28addition,_%29-4fnbx.md) | [`vDSP_vasm`](./vdsp_vasm.md) |
| `d[i] = (a[i] + b[i]) * c[i]` | [`multiply(addition:_:)`](./vdsp/multiply%28addition,_%29-7t59.md) | [`vDSP_vam`](./vdsp_vam.md) |
| `d[i] = (a[i] - b[i]) * c` | [`multiply(subtraction:_:)`](./vdsp/multiply%28subtraction,_%29-106pt.md) | [`vDSP_vsbsm`](./vdsp_vsbsm.md) |
| `d[i] = (a[i] - b[i]) * c[i]` | [`multiply(subtraction:_:)`](./vdsp/multiply%28subtraction,_%29-6y7g6.md) | [`vDSP_vsbm`](./vdsp_vsbm.md) |
| `d[i] = (a[i] * b[i]) + c` | [`add(multiplication:_:)`](./vdsp/add%28multiplication,_%29-36vhq.md) | [`vDSP_vmsa`](./vdsp_vmsa.md) |
| `d[i] = (a[i] * b) + c[i]` | [`add(multiplication:_:)`](./vdsp/add%28multiplication,_%29-7aut1.md) | [`vDSP_vsma`](./vdsp_vsma.md) |
| `d[i] = (a[i] * b[i]) + c[i]` | [`add(multiplication:_:)`](./vdsp/add%28multiplication,_%29-9bgb2.md) | [`vDSP_vma`](./vdsp_vma.md) |
| `d[i] = (a[i] * b[i]) - c[i]` | [`subtract(multiplication:_:)`](./vdsp/subtract%28multiplication,_%29-6u3sp.md) | [`vDSP_vmsb`](./vdsp_vmsb.md) |
| `e[i] = (a[i] * b) + (c[i] * d)` | [`add(multiplication:multiplication:)`](./vdsp/add%28multiplication,multiplication%29-8rjh8.md) | [`vDSP_vsmsma`](./vdsp_vsmsma.md) |
| `e[i] = (a[i] + b[i]) * (c[i] + d[i])` | [`multiply(addition:addition:)`](./vdsp/multiply%28addition,addition%29-1voy8.md) | [`vDSP_vaam`](./vdsp_vaam.md) |
| `e[i] = (a[i] * b[i]) - (c[i] * d[i])` | [`subtract(multiplication:multiplication:)`](./vdsp/subtract%28multiplication,multiplication%29-1ghyu.md) | [`vDSP_vmmsb`](./vdsp_vmmsb.md) |
| `e[i] = (a[i] - b[i]) * (c[i] - d[i])` | [`multiply(subtraction:subtraction:)`](./vdsp/multiply%28subtraction,subtraction%29-1rnom.md) | [`vDSP_vsbsbm`](./vdsp_vsbsbm.md) |
| `e[i] = (a[i] + b[i]) * (c[i] - d[i])` | [`multiply(addition:subtraction:)`](./vdsp/multiply%28addition,subtraction%29-6h89l.md) | [`vDSP_vasbm`](./vdsp_vasbm.md) |

## See Also

### Signal Processing Essentials
- [Controlling vDSP operations with stride](./controlling-vdsp-operations-with-stride.md)
  Operate selectively on the elements of a vector at regular intervals.
- [Using linear interpolation to construct new data points](./using-linear-interpolation-to-construct-new-data-points.md)
  Fill the gaps in arrays of numerical data using linear interpolation.
- [Resampling a signal with decimation](./resampling-a-signal-with-decimation.md)
  Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.
- [vDSP](./vdsp-library.md)
  Perform basic arithmetic operations and common digital signal processing (DSP) routines on large vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/using-vdsp-for-vector-based-arithmetic)*