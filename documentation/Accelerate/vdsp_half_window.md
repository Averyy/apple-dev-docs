# vDSP_HALF_WINDOW

**Framework**: Accelerate  
**Kind**: var

Specifies that the window should only contain the bottom half of the values (`0` to `(N+1)/2`).

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
var vDSP_HALF_WINDOW: Int { get }
```

## See Also

- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [static func window<T>(ofType: T.Type, usingSequence: vDSP.WindowSequence, count: Int, isHalfWindow: Bool) -> [T]](vdsp/window(oftype:usingsequence:count:ishalfwindow:).md)
  Returns an array that contains the specified window.
- [static func formWindow<V>(usingSequence: vDSP.WindowSequence, result: inout V, isHalfWindow: Bool)](vdsp/formwindow(usingsequence:result:ishalfwindow:)-6cmve.md)
  Populates a double-precision vector with a specified window.
- [static func formWindow<V>(usingSequence: vDSP.WindowSequence, result: inout V, isHalfWindow: Bool)](vdsp/formwindow(usingsequence:result:ishalfwindow:)-9dls5.md)
  Populates a single-precision vector with a specified window.
- [vDSP.WindowSequence](vdsp/windowsequence.md)
  Constants that specify window sequence functions.
- [var vDSP_HANN_DENORM: Int](vdsp_hann_denorm.md)
  Specifies a denormalized Hann window.
- [var vDSP_HANN_NORM: Int](vdsp_hann_norm.md)
  Specifies a normalized Hann window


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_half_window)*