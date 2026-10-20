# releaseInfo

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

If non-`NULL`,the callback used to release the `info` parameterpassed to [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](../cgfunction/init%28info,domaindimension,domain,rangedimension,range,callbacks%29.md).

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
var releaseInfo: CGFunctionReleaseInfoCallback?
```

```c
CGFunctionReleaseInfoCallback releaseInfo;
```

## See Also

### Instance Properties
- [var evaluate: CGFunctionEvaluateCallback?](./evaluate.md)
  The callback that evaluates the function.
- [var version: UInt32](./version.md)
  The structure version number. For this structure,the version should be `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/releaseinfo)*