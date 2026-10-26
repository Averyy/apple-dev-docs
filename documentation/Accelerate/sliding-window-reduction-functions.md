# Sliding-window reduction functions

**Framework**: Accelerate  
**Role**: API Collection

Calculate maximum values and sums of values in a sliding window.

## Topics

### Sliding-window summation functions
- [static func slidingWindowSum<U>(U, usingWindowLength: Int) -> [Double]](./vdsp/slidingwindowsum%28_,usingwindowlength%29-2t1dc.md)
  Returns the double-precision sliding window sum of a vector.
- [static func slidingWindowSum<U>(U, usingWindowLength: Int) -> [Float]](./vdsp/slidingwindowsum%28_,usingwindowlength%29-reb8.md)
  Returns the single-precision sliding window sum of a vector.
- [static func slidingWindowSum<U, V>(U, usingWindowLength: Int, result: inout V)](./vdsp/slidingwindowsum%28_,usingwindowlength,result%29-i972.md)
  Calculates the double-precision sliding window sum of a vector.
- [static func slidingWindowSum<U, V>(U, usingWindowLength: Int, result: inout V)](./vdsp/slidingwindowsum%28_,usingwindowlength,result%29-5tg0h.md)
  Calculates the single-precision sliding window sum of a vector.
- [vDSP_vswsum](./vdsp_vswsum.md)
  Finds the sum of values in a sliding window at each possible position in a single-precision input vector.
- [vDSP_vswsumD](./vdsp_vswsumd.md)
  Finds the sum of values in a sliding window at each possible position in a double-precision input vector.
### Sliding-window maximum functions
- [vDSP_vswmax](./vdsp_vswmax.md)
  Finds the maximum value in a sliding window at each possible position in a single-precision input vector.
- [vDSP_vswmaxD](./vdsp_vswmaxd.md)
  Finds the maximum value in a sliding window at each possible position in a double-precision input vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sliding-window-reduction-functions)*