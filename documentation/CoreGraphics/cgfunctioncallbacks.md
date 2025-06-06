# CGFunctionCallbacks

**Framework**: Core Graphics  
**Kind**: struct

A structure that contains callbacks needed by a `CGFunctionRef` object.

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
struct CGFunctionCallbacks
```

## Topics

### Initializers
- [init()](cgfunctioncallbacks/init.md)
- [init(version: UInt32, evaluate: CGFunctionEvaluateCallback?, releaseInfo: CGFunctionReleaseInfoCallback?)](cgfunctioncallbacks/init(version:evaluate:releaseinfo:).md)
### Instance Properties
- [var evaluate: CGFunctionEvaluateCallback?](cgfunctioncallbacks/evaluate.md)
  The callback that evaluates the function.
- [var releaseInfo: CGFunctionReleaseInfoCallback?](cgfunctioncallbacks/releaseinfo.md)
  If non-`NULL`,the callback used to release the `info` parameterpassed to [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](cgfunction/init(info:domaindimension:domain:rangedimension:range:callbacks:).md).
- [var version: UInt32](cgfunctioncallbacks/version.md)
  The structure version number. For this structure,the version should be `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CGFunctionEvaluateCallback](cgfunctionevaluatecallback.md)
  Performs custom operations on the supplied input data to produce output data.
- [typealias CGFunctionReleaseInfoCallback](cgfunctionreleaseinfocallback.md)
  Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks)*