# CGFunctionCallbacks

**Framework**: Core Graphics  
**Kind**: struct  
**Role**: Structure

A structure that contains callbacks needed by a `CGFunctionRef` object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CGFunctionCallbacks
```

```c
struct CGFunctionCallbacks;
```

## Topics

### Initializers
- [init()](./cgfunctioncallbacks/init%28%29.md)
- [init(version: UInt32, evaluate: CGFunctionEvaluateCallback?, releaseInfo: CGFunctionReleaseInfoCallback?)](./cgfunctioncallbacks/init%28version,evaluate,releaseinfo%29.md)
### Instance Properties
- [var evaluate: CGFunctionEvaluateCallback?](./cgfunctioncallbacks/evaluate.md)
  The callback that evaluates the function.
- [var releaseInfo: CGFunctionReleaseInfoCallback?](./cgfunctioncallbacks/releaseinfo.md)
  If non-`NULL`,the callback used to release the `info` parameterpassed to [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](./cgfunction/init%28info,domaindimension,domain,rangedimension,range,callbacks%29.md).
- [var version: UInt32](./cgfunctioncallbacks/version.md)
  The structure version number. For this structure,the version should be `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Callbacks
- [typealias CGFunctionEvaluateCallback](./cgfunctionevaluatecallback.md)
  Performs custom operations on the supplied input data to produce output data.
- [typealias CGFunctionReleaseInfoCallback](./cgfunctionreleaseinfocallback.md)
  Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks)*