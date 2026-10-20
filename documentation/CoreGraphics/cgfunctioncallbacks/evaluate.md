# evaluate

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

The callback that evaluates the function.

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
var evaluate: CGFunctionEvaluateCallback?
```

```c
CGFunctionEvaluateCallback evaluate;
```

## See Also

### Instance Properties
- [var releaseInfo: CGFunctionReleaseInfoCallback?](./releaseinfo.md)
  If non-`NULL`,the callback used to release the `info` parameterpassed to [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](../cgfunction/init%28info,domaindimension,domain,rangedimension,range,callbacks%29.md).
- [var version: UInt32](./version.md)
  The structure version number. For this structure,the version should be `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/evaluate)*