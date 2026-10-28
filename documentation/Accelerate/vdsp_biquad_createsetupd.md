# vDSP_biquad_CreateSetupD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Builds a data structure that contains precalculated data for use by a double-precision cascaded biquadratic filter function.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern vDSP_biquad_SetupDvDSP_biquad_CreateSetupD(const double *__Coefficients, vDSP_Length __M);
```

## Return Value

A pointer to an allocated and initialized biquadratic filter object.

## Discussion

This function constructs and returns a biquadratic filter object from the coefficients that you specify.

You define the `__Coefficients` array as a series of sections with each containing a set of five coefficients. Specify the order of the coefficients as three feedforward coefficients followed by two feedback coefficients.

The following code shows an example of creating a biquad setup object that contains two sections:

**Swift**:

```swift
let section0 = (b0: 0.984764420,
                b1: -1.969528840,
                b2: 0.984764420,
                a1: -1.969331359,
                a2: 0.969726321)

let section1 = (b0: 0.984764420,
                b1: -1.969528840,
                b2: 0.984764420,
                a1: -1.955243388,
                a2: 0.969726321)

let sectionCount = vDSP_Length(2)

let setup = vDSP_biquad_CreateSetupD([
    section0.b0, section0.b1, section0.b2, section0.a1, section0.a2,
    section1.b0, section1.b1, section1.b2, section1.a1, section1.a2
],
                                     sectionCount)
```

**Objective-C**:

```objc
double coefficients[10] = {
    // section 0: `b0`, `b1`, `b2`, `a1`, `a2`
    0.984764420, -1.969528840, 0.984764420, -1.969331359, 0.969726321,
    // section 1: `b0`, `b1`, `b2`, `a1`, `a2`
    0.984764420, -1.969528840, 0.984764420, -1.955243388, 0.969726321
};

vDSP_Length sectionCount = 2;

vDSP_biquad_SetupD setup = vDSP_biquad_CreateSetupD(coefficients, sectionCount);
```

This function allocates memory for its own use. You must call the [`vDSP_biquad_DestroySetupD`](./vdsp_biquad_destroysetupd.md) function to free the allocated memory.

## Parameters

- `__Coefficients`: The input array that contains the double-precision filter coefficients. The number of elements in the coefficients array must be five times the number of sections in the biquad filter.
- `__M`: The number of sections in the biquad filter.

## See Also

### Creating a single-channel biquadratic filter setup
- [vDSP_biquad_CreateSetup](./vdsp_biquad_createsetup.md)
  Builds a data structure that contains precalculated data for use by a single-precision cascaded biquadratic filter function.
- [typealias vDSP_biquad_Setup](./vdsp_biquad_setup.md)
  A data structure that contains precalculated data for use by the single-precision cascaded biquadratic IIR filter function.
- [typealias vDSP_biquad_SetupD](./vdsp_biquad_setupd.md)
  A data structure that contains precalculated data for use by the double-precision cascaded biquadratic IIR filter function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquad_createsetupd)*