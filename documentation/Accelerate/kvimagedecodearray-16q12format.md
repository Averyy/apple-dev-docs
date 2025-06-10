# kvImageDecodeArray_16Q12Format

**Framework**: Accelerate  
**Kind**: var

Predefined decode array constant to use with 16Q12-formatted data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kvImageDecodeArray_16Q12Format: UnsafePointer<CGFloat>!
```

#### Discussion

Data in 16Q12 format consists of a signed 16-bit fixed-point integer. This integer is implicitly divided by 2¹² to give a range of [-8,8]  (`SHRT_MIN``/4096`,`SHRT_MAX``/4096`). The type is present to allow 8-bit content to be converted into other colorspaces and operated on without undue loss of precision or loss of color gamut due to clamping. This is identified by address. Copying the values here causes a Core Graphics (CG) format to be instead interpreted as an unsigned 16-bit format.

Pixels in 16Q12 format don’t follow CG image format conventions in two respects. First, the format is signed; second, the alpha channel is also subject to the decode array transform, meaning that 0 is transparent and 4096 is opaque. Consequently, all buffers that use this format must be tagged with the [`kvImageDecodeArray_16Q12Format`](kvimagedecodearray_16q12format.md) decode array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimagedecodearray_16q12format)*