# CGFunctionEvaluateCallback

**Framework**: Core Graphics  
**Kind**: typealias

Performs custom operations on the supplied input data to produce output data.

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
typealias CGFunctionEvaluateCallback = (UnsafeMutableRawPointer?, UnsafePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Void
```

#### Discussion

The callback you write is responsible for implementing thecalculation of output values from the supplied input values. Forexample, if you want to implement a simple “squaring” functionof one input argument to one output argument, your evaluation functionmight be:

```objc
void evaluateSquare(void *info, const float *inData, float *outData)
{
    outData[0] = inData[0] * inData[0];
}
```

## Parameters

- `info`: The   parameter passed to  .
- `inData`: An array of floats. The size of the array is that specified by the   parameter passed to the   function.
- `outData`: An array of floats. The size of the array is that specified by the   parameter passed to the   function.

## See Also

- [struct CGFunctionCallbacks](cgfunctioncallbacks.md)
  A structure that contains callbacks needed by a `CGFunctionRef` object.
- [typealias CGFunctionReleaseInfoCallback](cgfunctionreleaseinfocallback.md)
  Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctionevaluatecallback)*