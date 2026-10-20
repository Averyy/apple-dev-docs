# version

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

The structure version number. For this structure,the version should be `0`.

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
var version: UInt32
```

```c
unsigned int version;
```

## See Also

### Instance Properties
- [var evaluate: CGFunctionEvaluateCallback?](./evaluate.md)
  The callback that evaluates the function.
- [var releaseInfo: CGFunctionReleaseInfoCallback?](./releaseinfo.md)
  If non-`NULL`,the callback used to release the `info` parameterpassed to [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](../cgfunction/init%28info,domaindimension,domain,rangedimension,range,callbacks%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/version)*