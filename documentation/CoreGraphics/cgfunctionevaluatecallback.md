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

- `info`: The `info` parameter passed to [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](cgfunction/init(info:domaindimension:domain:rangedimension:range:callbacks:).md).
- `inData`: An array of floats. The size of the array is that specified by the `domainDimension` parameter passed to the [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](cgfunction/init(info:domaindimension:domain:rangedimension:range:callbacks:).md) function.
- `outData`: An array of floats. The size of the array is that specified by the `rangeDimension` parameter passed to the [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](cgfunction/init(info:domaindimension:domain:rangedimension:range:callbacks:).md) function.

## See Also

- [struct CGFunctionCallbacks](cgfunctioncallbacks.md)
  A structure that contains callbacks needed by a `CGFunctionRef` object.
- [typealias CGFunctionReleaseInfoCallback](cgfunctionreleaseinfocallback.md)
  Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctionevaluatecallback)*