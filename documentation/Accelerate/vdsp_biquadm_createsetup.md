# vDSP_biquadm_CreateSetup

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Builds a data structure that contains precalculated data for use by a single-precision, multichannel cascaded biquadratic filter function.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern vDSP_biquadm_SetupvDSP_biquadm_CreateSetup(const double *__coeffs, vDSP_Length __M, vDSP_Length __N);
```

## Return Value

A pointer to an allocated and initialized biquadratic filter object.

## Discussion

This function constructs and returns a biquadratic filter object from the coefficients that you specify. This function initializes the internal state of the setup object with all delay elements set to zero.

You define the `__Coefficients` array as a series of sections where each section contains a set of five coefficients for each channel. Specify the order of the coefficients as three feedforward coefficients followed by two feedback coefficients.

The following code shows an example of creating a biquadratic setup object that contains two sections:

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
let channelCount = vDSP_Length(1)

let setup = vDSP_biquadm_CreateSetup([
    section0.b0, section0.b1, section0.b2, section0.a1, section0.a2,
    section1.b0, section1.b1, section1.b2, section1.a1, section1.a2
],
                                     sectionCount,
                                     channelCount)
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
vDSP_Length channelCount = 1;

vDSP_biquadm_Setup setup = vDSP_biquadm_CreateSetup(coefficients,
                                                     sectionCount,
                                                     channelCount);
```

Interleave channel coefficients to create a biquadratic setup object for multiple channels. For example, the following code creates a biquadratic setup object that contains two sections for two channels:

```swift
    let section0_channel0 = (b0: [ … ], b1: [ … ], b2: [ … ], a1: [ … ], a2: [ … ])
    let section0_channel1 = (b0: [ … ], b1: [ … ], b2: [ … ], a1: [ … ], a2: [ … ])
    let section1_channel0 = (b0: [ … ], b1: [ … ], b2: [ … ], a1: [ … ], a2: [ … ])
    let section1_channel1 = (b0: [ … ], b1: [ … ], b2: [ … ], a1: [ … ], a2: [ … ])

    let sectionCount = vDSP_Length(2)
    let channelCount = vDSP_Length(2)

    let sectionCount = vDSP_Length(2)
    let channelCount = vDSP_Length(2)

    let setup = vDSP_biquadm_CreateSetup([
        section0_channel0.b0, section0_channel1.b0,
        section0_channel0.b1, section0_channel1.b1,
        section0_channel0.b2, section0_channel1.b2,
        section0_channel0.a1, section0_channel1.a1,
        section0_channel0.a2, section0_channel1.a2,
        
        section1_channel0.b0, section1_channel1.b0,
        section1_channel0.b1, section1_channel1.b1,
        section1_channel0.b2, section1_channel1.b2,
        section1_channel0.a1, section1_channel1.a1,
        section1_channel0.a2, section1_channel1.a2
    ],
                                         sectionCount,
                                         channelCount) 
```

This function allocates memory for its own use. To free the allocated memory, call the [`vDSP_biquadm_DestroySetup`](./vdsp_biquadm_destroysetup.md) function.

## Parameters

- `__coeffs`: The input array that contains the double-precision filter coefficients. The number of elements in the coefficients array must be `5 * __M * __N`.
- `__M`: The number of sections in the biquadratic filter.
- `__N`: The number of input-output channels.

## See Also

### Creating a multichannel biquadratic filter setup
- [typealias vDSP_biquadm_Setup](./vdsp_biquadm_setup.md)
  A data structure that contains precalculated data for use by a single-precision, multichannel cascaded biquadratic filter function.
- [vDSP_biquadm_CreateSetupD](./vdsp_biquadm_createsetupd.md)
  Builds a data structure that contains precalculated data for use by a double-precision, multichannel cascaded biquadratic filter function.
- [typealias vDSP_biquadm_SetupD](./vdsp_biquadm_setupd.md)
  A data structure that contains precalculated data for use by a double-precision, multichannel cascaded biquadratic filter function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_createsetup)*